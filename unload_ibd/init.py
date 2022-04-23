# -*- coding: utf-8 -*-
# 有系统表的从系统表中读取表结构信息放到sqlite中(或不取),没有系统表的从sql文件或ini文件中获取系统表信息存储到sqlite中,
# 再 从sqlite库里读取表结构 ,来初始化表结构. sqlite中的 table 和 column表
import sqlite3, struct, os, pymysql
import table_struct, page

s = struct.unpack


# 获取文件头信息
def first_page(data):
    file_info = table_struct.File_Info();
    fmt_1 = '>'
    header = s(">4IQHQI", data[0:38])
    if header[0] != 0 and header[1] == 0 and header[5] == 8:
        fsp = s(">3I", data[38:50])
        file_info.ts_id = fsp[0]
        file_info.blk_sum = fsp[2]
        file_info.blk_size = 16384
    return file_info


# 获取boot页信息
def boot_info(f):
    f.seek(16384 * 7)
    data = f.read(16384)
    data = s(">3Q7I", data[38:90])
    sys_tables_page = data[5]
    sys_columns_page = data[7]
    sys_indexes_page = data[8]
    sys_fields_page = data[9]
    return sys_tables_page, sys_columns_page, sys_indexes_page, sys_fields_page


db1 = table_struct.st_db()  # 实例化表结构对象


def init_sys():
    # 读取sqlite数据库表，获得配置信息 和 表结构信息
    db = './db_info.db'  # 数据库文件名称    =========================
    conn = sqlite3.connect(db);
    cursor = conn.cursor()
    cursor.execute("select db_name,tab_name,tab_type,tab_id,ind_id,ts_no,col_sum from tab_info;")
    values_tab = cursor.fetchall()  # 返回数据为二维数组
    db1.tab_sum = len(values_tab)
    type = {1248: 'varchar', 1332: 'char', 616: 'datetime', 614: 'timestamp', 607: 'int', 612: 'bigint'}
    for i in range(0, db1.tab_sum):  # 初始化表结构
        table1 = table_struct.st_table()
        table1.db_name = values_tab[i][0]
        table1.tab_name = values_tab[i][1]
        table1.tab_type = values_tab[i][2]
        table1.tab_obj_id = values_tab[i][3]
        table1.index_id = values_tab[i][4]
        table1.ts_no = values_tab[i][5]
        table1.col_sum = values_tab[i][6]
        cursor.execute("select c.* from tab_info t,col_info c where c.tab_id = t.tab_id and \
        t.tab_id=%d order by c.col_id" % table1.tab_obj_id)
        values_col = cursor.fetchall()
        if len(values_col) == 0:
            table1.col_sum = 0
        var_len_sum = 0  # 变长列数
        for ii in range(table1.col_sum):
            column1 = table_struct.st_column()
            column1.tab_obj_id = values_col[ii][1]
            column1.col_id = values_col[ii][2]
            column1.col_name = values_col[ii][3]
            col_mtype = values_col[ii][4]
            column1.col_type = type[col_mtype]
            column1.col_len = values_col[ii][5]
            column1.pkey_is = values_col[ii][9]
            column1.varlen_is = values_col[ii][10]
            column1.col_unsign = values_col[ii][11]
            table1.col.append(column1)
            table1.col_1.append(column1)
            if col_mtype == 1248:
                var_len_sum = var_len_sum + 1
        table1.var_len_sum = var_len_sum

        # 初始化记录结构,倒换列顺序. 先主键后结构列后普通列
        pkey_id = 0  # 主键数量/编号
        for ii in range(len(table1.col_1)):
            col = table1.col_1[ii]
            if col.pkey_is == 1:  # 如果是主键
                pkey_id += 1
                table1.col_1.insert(pkey_id - 1, col)
                del table1.col_1[ii + 1]
        TXID = table_struct.st_column()
        TXID.col_name = 'TXID'
        TXID.col_id = -1
        TXID.col_len = 6
        TXID.notnull_is = 0
        TXID.varlen_is = 0
        RPID = table_struct.st_column()
        RPID.col_name = 'RPID'
        RPID.col_id = -2
        RPID.col_len = 7
        RPID.notnull_is = 0
        RPID.varlen_is = 0
        table1.col_1.insert(pkey_id, TXID)
        table1.col_1.insert(pkey_id + 1, RPID)
        db1.tab.append(table1)
    cursor.close()
    conn.close()


# 链式解析page
def page_link(f, pgfirst, table):  # 文件，页链的起始页面号，表
    page_size = 16384
    f_size = os.path.getsize(f.name)  # 获取文件大小，只能处理文件,不能磁盘
    f_pg_size = f_size // 16384
    next_page = pgfirst
    tab_data = []
    # 其实走索引，没有用横向页链(即上下页)
    while (next_page != 0 and next_page < f_pg_size):  # 下一页不溢出
        pos1 = (next_page) * page_size
        f.seek(pos1)  # 要判断返回值，是否成功
        data = f.read(page_size)
        data1 = data[0:page_size]
        data3 = s('>I', data1[70:74])  # tab_id
        if data3[0] in (1, 2, 3, 4):
            page1 = page.rec_redundant(f, data1, table)  # 解析系统表页面记录.  ***************
        else:
            page1 = page.rec_compact(f, data1, table)  # 解析普通表页面记录.  ***************
        tab_data.append(page1)
        data2 = s('>I', data1[12:16])
        next_page = data2[0]
    return tab_data


# 解析sys系统表
def sys_tables(f, sys_tables_page, sys_columns_page, sys_indexes_page, sys_fields_page):
    init_sys()
    sys_tables = page_link(f, sys_tables_page, db1.tab[0])
    sys_columns = page_link(f, sys_columns_page, db1.tab[1])
    sys_indexes = page_link(f, sys_indexes_page, db1.tab[2])
    sys_fields = page_link(f, sys_fields_page, db1.tab[3])
    return sys_tables, sys_columns, sys_indexes, sys_fields


# 初始化 普通表
def init_all(f, sys_tables, sys_columns, sys_indexes, sys_fields):
    tab_all = [];
    db_all = []
    for i1 in range(len(sys_tables)):
        for ii1 in range(len(sys_tables[i1].record)):
            obj_id = sys_tables[i1].record[ii1].col_data1[1]  # object_id，内部id
            tab_name = sys_tables[i1].record[ii1].col_data1[0]
            a = tab_name.find('/', 0, -1)
            b = a + 1
            if a == -1:
                a = 0;
                b = 0
            db_name = tab_name[0:a]
            tab_name = tab_name[b:]
            if db_name != '':
                db_all.append(db_name)
            obj_type = sys_tables[i1].record[ii1].col_data1[3]
            ts_no = sys_tables[i1].record[ii1].col_data1[6]
            tab = tab_info(sys_columns, sys_indexes, sys_fields, obj_id, tab_name)  # 初始化一个表的表结构
            tab.ts_no = ts_no
            tab.db_name = db_name
            # if tab_name[0:9] == 'shanghai/':
            #    print('tab_id:%d,tab_name:%s,col_sum:%d,index_id:%d,ts_no:%d,pgfirst:%d'%(obj_id,tab_name,tab.col_sum,tab.index_id,ts_no,tab.pgfirst))
            tab_all.append(tab)
            print('tab_id:%d,tab_name:%s.%s,col_sum:%d,index_id:%d,ts_no:%d,pgfirst:%d' % (
                tab.tab_obj_id, db_name, tab.tab_name, tab.col_sum, tab.index_id, tab.ts_no, tab.pgfirst))
    news_ids = list(set(db_all))  # 去重
    news_ids.sort()
    db_all = news_ids
    tab_all.sort(key=lambda x: (x.tab_name))  # 排序 。支持多关键字排序

    return tab_all, db_all  # 所有的表结构


# 初始化 普通表的表结构
def tab_info(sys_columns, sys_indexes, sys_fields, obj_id, tab_name):
    table1 = table_struct.st_table()
    table1.tab_obj_id = obj_id
    table1.tab_name = tab_name
    pk_name = []
    # 需要用 sys_indexes 和 sys_columns 获取表的列信息
    for i2 in range(len(sys_indexes)):  # 获取索引信息，主键信息
        for ii2 in range(len(sys_indexes[i2].record)):
            if sys_indexes[i2].record[ii2].col_data1[0] == obj_id and sys_indexes[i2].record[ii2].col_data1[4] in (
                    1, 3):
                table1.pgfirst = sys_indexes[i2].record[ii2].col_data1[6]
                table1.index_id = sys_indexes[i2].record[ii2].col_data1[1]
                #    table1.index_col_sum = sys_indexes[i2].record[ii2].col_data1[3]
                for i3 in range(len(sys_fields)):
                    for ii3 in range(len(sys_fields[i3].record)):
                        if sys_indexes[i2].record[ii2].col_data1[1] == sys_fields[i3].record[ii3].col_data1[0]:
                            pk_name.append(sys_fields[i3].record[ii3].col_data1[2])  # 主键列名
                    #      print('table:%s 的主键：%s,%s'%(tab_name,sys_fields[i3].record[ii3].col_data1[1],sys_fields[i3].record[ii3].col_data1[2]))
                break
    type = {12000: 'varchar', 12015: 'varchar', 13254: 'char', 1264: 'longtext', 5252: 'text', \
            3016: 'bit', 3254: 'binary', 4015: 'varbinary', 6254: 'set', \
            6010: 'date', 6011: 'time', 6012: 'datetime', 6013: 'year', 6007: 'timestamp', \
            6001: 'tinyint', 6002: 'smallint', 6003: 'int', 6008: 'bigint', 6009: 'mediumint', \
            9004: 'float', 10005: 'double', 3246: 'decimal'}
    for i in range(len(sys_columns)):  # 获取 列信息
        for ii in range(len(sys_columns[i].record)):
            if sys_columns[i].record[ii].col_data1[0] == obj_id:
                column1 = table_struct.st_column()
                column1.tab_obj_id = sys_columns[i].record[ii].col_data1[0]
                column1.col_id = sys_columns[i].record[ii].col_data1[1]
                column1.col_name = sys_columns[i].record[ii].col_data1[2]
                column1.col_len = sys_columns[i].record[ii].col_data1[5]
                col_prec = sys_columns[i].record[ii].col_data1[6]
                col_mtype = sys_columns[i].record[ii].col_data1[3]
                col_ptype = sys_columns[i].record[ii].col_data1[4]
                col_ptype_1 = col_ptype & 255
                type_10 = col_mtype * 1000 + col_ptype_1
                if type_10 > 12000 and type_10 < 13000:
                    type_10 = 12000
                elif type_10 > 13000:
                    type_10 = 13254
                if type_10 in type:
                    column1.col_type = type[type_10]
                if obj_id == 19:  # 测试用，显示一个表的列信息,obj_id = tab_id
                    print(column1.col_id, column1.col_name, column1.col_type,
                          'len:%d,mtype:%d,ptype:%d,p:%d' % (column1.col_len, col_mtype, col_ptype_1, col_ptype))
                column1.notnull_is = (col_ptype >> 8) % 2  # 1：not null,0:nullable
                unsign = (col_ptype >> 9) % 2  # 1：无符号数
                column1.col_unsign = unsign
                if column1.notnull_is == 0:  # ullable
                    table1.nullable_sum += 1
                if col_mtype in (5, 12, 13):  # 变长列
                    column1.varlen_is = 1
                    table1.var_len_sum += 1
                if column1.col_name in pk_name:  # 主键
                    column1.pkey_is = 1
                    table1.pkey_sum += 1
                table1.col.append(column1)
    table1.col_sum = len(table1.col)
    table1.col.sort(key=lambda x: (x.col_id))
    if table1.pkey_sum == 0:
        ROWID = table_struct.st_column()
        ROWID.col_name = 'ROWID'
        ROWID.col_id = -3
        ROWID.col_len = 6
        ROWID.notnull_is = 1
        table1.col_1.append(ROWID)
        table1.index_col.append(ROWID)
    else:
        for i5 in range(table1.col_sum):  # 处理主键列
            if table1.col[i5].pkey_is == 1:
                column1 = table1.col[i5]
                table1.col_1.append(column1)
                table1.index_col.append(column1)
    # 下边两列所有数据记录都有
    ind = table_struct.st_column()  # 索引记录中的最后一列，索引指针
    ind.col_name = 'ind'
    ind.col_id = -1
    ind.col_type = 'int'
    ind.col_len = 4
    ind.notnull_is = 1
    ind.varlen_is = 0
    ind.col_unsign = 1
    table1.index_col.append(ind)
    TXID = table_struct.st_column()
    TXID.col_name = 'TXID'
    TXID.col_id = -1
    TXID.col_len = 6
    TXID.notnull_is = 1
    TXID.varlen_is = 0
    RPID = table_struct.st_column()
    RPID.col_name = 'RPID'
    RPID.col_id = -2
    RPID.col_len = 7
    RPID.notnull_is = 1
    RPID.varlen_is = 0
    table1.col_1.append(TXID)
    table1.col_1.append(RPID)
    for i4 in range(table1.col_sum):  # 处理普通列
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
    return table1


# 解析表，一个表
def unload_tab(f, tab, db):  # 解析表,把表数据存储在db中
    tab_id = tab.tab_obj_id  # object_id，内部id
    tab_data = []
    if tab_id != 0:  # 表id
        tab_data = page_link(f, tab.pgfirst, tab)  # 解析特定表的数据 （以链式）
        #   tab_data = test.page_link1(f,0,tab[i1])           # 遍历解析表的页面
        print('table:%s.%s 解析完成' % (tab.db_name, tab.tab_name))
    #   save_data2(tab,tab_data,'')      # 保存数据
    return tab_data


# 解析表，所有表. 不常用
def unload_tab1(f, tab, db):
    dump_1 = '''
    -- dump file by Innodb Unload 1.4 \n
    /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
    /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
    /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
    /*!40101 SET NAMES utf8 */;
    /*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
    /*!40103 SET TIME_ZONE='+00:00' */;
    /*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
    /*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
    /*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
    /*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */; \n\n'''
    dump_2 = '''\n
    UNLOCK TABLES;
    /*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
    /*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
    /*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
    /*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
    /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
    /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
    /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
    /*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */; \n'''
    #  db = r'.\aaa.txt'
    f1 = open(db, 'w', encoding='utf-8')
    f1.write(dump_1)
    for i1 in range(len(tab)):
        tab_id = tab[i1].tab_obj_id  # object_id，内部id
        tab_data = []
        if tab_id != 0:  # 表id
            tab_data = page_link(f, tab[i1].pgfirst, tab[i1])  # 解析特定表的数据 （以链式）
            #   tab_data = test.page_link1(f,0,tab[i1])           # 遍历解析表的页面
            print('table:%s.%s 解析完成' % (tab[i1].db_name, tab[i1].tab_name))
            save_data3(f1, tab[i1], tab_data, '')  # 保存数据到dump文件
    f1.write(dump_2)
    f1.close()
    tab_data = []
    print('dump 完成...')
    return tab_data


# 　本地化1：把表数据插入到sqlite
def save_data1(tab, tab_data, db):
    conn = sqlite3.connect(db)  # 打开数据库
    cursor = conn.cursor()
    print(tab.sql)
    cursor.execute(tab.sql)  # 创建解析的表，然后把解析的数据存储进去
    for i in range(0, len(tab_data)):
        for i1 in range(0, tab_data[i].rec_sum):
            ss = ''
            for i2 in range(0, tab.col_sum):
                if i2 == tab.col_sum - 1:
                    ss += '\'' + str(tab_data[i].record[i1].col_data1[i2]) + '\''
                else:
                    ss += '\'' + str(tab_data[i].record[i1].col_data1[i2]) + '\'' + ','
            print(ss)
            cursor.execute("insert into %s values( %s );" % (tab.tab_name, ss))  # 插入数据
    conn.commit()


# 　本地化2: 把表数据导入到远程的mysl数据库
def save_data2(tab, tab_data, db):
    # conn = pymysql.connect(user='root', passwd='000000',host='10.3.9.50',db='SchemeBank_guojia',charset='utf8')
    # cursor = conn.cursor()
    f1 = open(r'test/%s.txt' % tab.tab_name, 'w', encoding='utf-8')
    print('开始导入 insert 到 文本文件')
    error_sum = 0
    for i in range(len(tab_data)):
        for i1 in range(len(tab_data[i].record)):
            ss = ''
            for i2 in range(tab.col_sum):  # 处理每一列
                if i2 == tab.col_sum - 1:
                    try:
                        if tab.col[i2].col_type in (
                                'char', 'varchar', 'text', 'date', 'datetime', 'timestamp', 'blob') and \
                                tab_data[i].record[i1].col_data1[i2] != 'NULL':
                            if tab_data[i].record[i1].col_data1[i2] == '':
                                ss += '\'\''
                            else:
                                ss += '\'%s\'' % tab_data[i].record[i1].col_data1[i2]
                        else:
                            ss += '%s' % tab_data[i].record[i1].col_data1[i2]
                    except IndexError as e:
                        ss += 'NULL'
                        print('%s,%s,Error: %s\n%s' % (i1, i2, e, ss))
                        #  print('Error: %s'%e)
                        continue
                else:
                    try:
                        if tab.col[i2].col_type in (
                                'char', 'varchar', 'text', 'date', 'datetime', 'timestamp', 'blob') and \
                                tab_data[i].record[i1].col_data1[i2] != 'NULL':
                            if tab_data[i].record[i1].col_data1[i2] == '':
                                ss += '\'\','
                            else:
                                ss += '\'%s\',' % tab_data[i].record[i1].col_data1[i2]
                        else:
                            ss += '%s,' % tab_data[i].record[i1].col_data1[i2]
                    except IndexError as e:
                        # ss = ''
                        ss += 'NULL,'
                        print('%s,%s,Error: %s\n%s' % (i1, i2, e, ss))
                        continue
            try:
                f1.write("insert into %s values(%s);\n" % (tab.tab_name, ss))
                print("insert into %s values(%s);" % (tab.tab_name, ss))  # 有些字符输出会有问题
            #  print("insert into %s(%s) values(%s);"%(tab.tab_name,tab.sql,ss))
            #  f1.write("insert into %s(%s) values(%s);\n"%(tab.tab_name,tab.sql,ss) )         # f1.write()
            # cursor.execute("insert into %s(%s) values(%s);"%(tab.tab_name,tab.sql,ss))      # 插入数据到mysql
            except (pymysql.err.InternalError, pymysql.err.DataError, UnicodeEncodeError) as e:
                print('Error: %s' % e)
                error_sum += 1
                continue
    #         conn.commit()
    # conn.close()
    print('表：%s 导入 文本\mysql 完成...error:%d' % (tab.tab_name, error_sum))


# 　本地化3: 把表数据导入到dump文本文件
def save_data3(f1, tab, tab_data, db):
    #  f1 = open(r'.\aaa.txt','w',encoding='utf-8')
    print('开始导入 表：%s 到 dump文件' % (tab.tab_name))
    error_sum = 0
    for i in range(len(tab_data)):
        for i1 in range(len(tab_data[i].record)):
            ss = ''
            for i2 in range(tab.col_sum):  # 处理每一列
                if i2 == tab.col_sum - 1:
                    try:
                        if tab.col[i2].col_type in (
                                'char', 'varchar', 'text', 'date', 'datetime', 'timestamp', 'blob') and \
                                tab_data[i].record[i1].col_data1[i2] != 'NULL':
                            if tab_data[i].record[i1].col_data1[i2] == '':
                                ss += '\'\''
                            else:
                                ss += '\'%s\'' % tab_data[i].record[i1].col_data1[i2]
                        else:
                            ss += '%s' % tab_data[i].record[i1].col_data1[i2]
                    except IndexError as e:
                        ss += 'NULL'
                        print('%s,%s,Error: %s' % (i1, i2, e))
                        #  print('Error: %s'%e)
                        continue
                else:
                    try:
                        if tab.col[i2].col_type in (
                                'char', 'varchar', 'text', 'date', 'datetime', 'timestamp', 'blob') and \
                                tab_data[i].record[i1].col_data1[i2] != 'NULL':
                            if tab_data[i].record[i1].col_data1[i2] == '':
                                ss += '\'\','
                            else:
                                ss += '\'%s\',' % tab_data[i].record[i1].col_data1[i2]
                        else:
                            ss += '%s,' % tab_data[i].record[i1].col_data1[i2]
                    except IndexError as e:
                        ss += 'NULL,'
                        print('%s,%s,Error: %s' % (i1, i2, e))
                        continue
            try:
                f1.write("insert into %s(%s) values(%s);\n" % (tab.tab_name, tab.sql, ss))  # f1.write()
            except (pymysql.err.InternalError, pymysql.err.DataError, UnicodeEncodeError) as e:
                print('Error: %s' % e)
                error_sum += 1
                continue

    print('表：%s dump 完成...error:%d' % (tab.tab_name, error_sum))
