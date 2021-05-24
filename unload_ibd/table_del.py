# -*- coding: utf-8 -*-
import os.path, struct, sqlite3
import page, init, table_struct

s = struct.unpack


# 通过db初始化表结构，此sqlite的db是通过table_frm.py解析建表sql转换成的。
def init_all_tab(db):
    conn = sqlite3.connect(db)  # 打开数据库
    cursor = conn.cursor()
    cursor.execute("select * from tab_info ")
    # id,db_name,tab_name,tab_id,ind_id,ts_no,col_sum,nullable_sum,var_len_sum
    values_tab = cursor.fetchall()  # 返回数据为二维数组
    tab_all = []
    for i in range(len(values_tab)):  # 初始化表结构
        table1 = table_struct.st_table()
        table1.tab_name = values_tab[i][2]
        table1.tab_obj_id = values_tab[i][4]
        table1.index_id = values_tab[i][5]
        table1.ts_no = values_tab[i][6]
        table1.col_sum = values_tab[i][7]
        table1.nullable_sum = values_tab[i][8]
        table1.var_len_sum = values_tab[i][9]
        cursor.execute("select c.* from tab_info t,col_info c where c.tab_id = t.tab_id and \
                        t.tab_id=%d order by c.col_id" % table1.tab_obj_id)
        # id,tab_id,col_id,col_name,col_type,col_len,prec,scale,notnull_is,pkey_is,var_len_is,unsign_is
        values_col = cursor.fetchall()
        if len(values_col) == 0:
            table1.col_sum = 0
        for ii in range(table1.col_sum):
            column1 = table_struct.st_column()
            column1.tab_obj_id = values_col[ii][1]
            column1.col_id = values_col[ii][2]
            column1.col_name = values_col[ii][3]
            column1.col_type = values_col[ii][4]
            column1.col_len = values_col[ii][5]
            column1.notnull_is = values_col[ii][8]
            column1.pkey_is = values_col[ii][9]
            column1.varlen_is = values_col[ii][10]
            column1.col_unsign = values_col[ii][11]

            if column1.pkey_is == 1:  # 主键
                column1.notnull_is = 1
                table1.pkey_sum += 1
            table1.col.append(column1)
        # 初始化记录结构,倒换列顺序. 先主键后结构列后普通列
        table1.col.sort(key=lambda x: (x.col_id))
        if table1.pkey_sum == 0:
            ROWID = table_struct.st_column()
            ROWID.col_name = 'ROWID'
            ROWID.col_id = -3
            ROWID.col_len = 6
            ROWID.notnull_is = 1
            table1.col_1.append(ROWID)
        else:
            for i3 in range(0, table1.col_sum):  # 处理主键列
                if table1.col[i3].pkey_is == 1:
                    column1 = table1.col[i3]
                    table1.col_1.append(column1)
        TXID = table_struct.st_column()
        TXID.col_name = 'TXID'
        TXID.col_id = -1
        TXID.col_len = 6
        TXID.notnull_is = 1
        RPID = table_struct.st_column()
        RPID.col_name = 'RPID'
        RPID.col_id = -2
        RPID.col_len = 7
        RPID.notnull_is = 1
        table1.col_1.append(TXID)
        table1.col_1.append(RPID)
        for i4 in range(0, table1.col_sum):  # 处理普通列
            if table1.col[i4].pkey_is != 1:
                column1 = table1.col[i4]
                table1.col_1.append(column1)
        s1 = 'CREATE TABLE ' + str(table1.tab_name) + '('  # 建表语句
        ss = ''
        for ii in range(0, table1.col_sum):
            if ii == table1.col_sum - 1:  # 建表语句
                ss += '%s' % table1.col[ii].col_name
            else:
                ss += '%s,' % table1.col[ii].col_name
        table1.sql = ss  # s1 + ss + ');\n'

        tab_all.append(table1)
    cursor.close()
    conn.close()

    return tab_all


# 通过解析系统表初始化表结构
def init_all_tab_2(f):  # f要求把这4个系统表的所有页面都放里面
    init.init_sys()
    sys_tables = page_scan(f, 0, init.db1.tab[0])
    sys_columns = page_scan(f, 0, init.db1.tab[1])
    sys_indexes = page_scan(f, 0, init.db1.tab[2])
    sys_fields = page_scan(f, 0, init.db1.tab[3])
    print("初始化 系统表 over ...\n")
    tab, db_all = init.init_all(f, sys_tables, sys_columns, sys_indexes, sys_fields)
    return tab  # db_all 只是存储了库名


# 扫描所有页面，解析匹配到的页
def page_scan(f, pgfirst, table):  # 扫描所有页面，解析匹配到的页
    page_size = 16384
    f_size = os.path.getsize(f.name)  # 获取文件大小，只能处理文件,不能磁盘
    f_pg_size = f_size // page_size
    next_page = pgfirst
    rec_sum = 0
    tab_data = []
    while (next_page < f_pg_size):  # 下一页不溢出
        pos1 = (next_page) * page_size
        f.seek(pos1)  # 要判断返回值，是否成功
        data = f.read(page_size)
        data1 = data[0:page_size]
        data_0 = s('>I', data1[4:8])  # page_no
        data2 = s('>I', data1[12:16])  # next_page
        data0 = s('>I', data1[8:12])  # pre_page
        data3 = s('>I', data1[34:38])  # ts_no
        data4 = s('>Q', data1[66:74])  # index_id
        data5 = s('>H', data1[64:66])  # index_level
        data6 = s('>H', data1[42:44])  # rec_sum0
        data7 = s('>H', data1[54:56])  # rec_sum1
        rec_sum0 = data6[0]
        if rec_sum0 > 32768:
            rec_sum0 -= 32768
        rec_sum += data7[0]
        if data4[0] == table.index_id and data5[0] == 0:  # level 0
            #      print('page_no:%d,pre:%d,next:%d,ts_no:%d,obj_id:%d,level:%d,rec_sum0:%d,rec_sum1:%d,rec_sum:%d '%(data_0[0],data0[0],data2[0],data3[0],data4[0],data5[0],rec_sum0,data7[0],rec_sum))
            if table.index_id in (1, 2, 3, 4):
                page1 = page.rec_redundant(f, data1, table)  # 解析redundant记录
            else:
                page1 = page.rec_compact(f, data1, table)  # 解析compact记录
            tab_data.append(page1)
        next_page = next_page + 1
    return tab_data


# 解析表,并保存。 按 表id 或 页面中的index_id 去扫描解析
def unload_tab(f, tab, db):
    for i1 in range(0, len(tab)):
        tab_obj_id = tab[i1].tab_obj_id  # tab_id，内部id
        index_id = tab[i1].index_id  # index_id，即数据页中的id
        tab_data = [];
        db = ''
        #  if tab_obj_id == 1690 :  # 表id   6915
        if index_id == 2201:  # 2199  2201
            print(tab[i1].sql)
            tab_data = page_scan(f, 0, tab[i1])  # 扫描所有页面，解析匹配到的页
            print('table:%s 解析完成' % (tab[i1].tab_name))
            init.save_data2(tab[i1], tab_data, db)  # 保存数据到mysql数据库
