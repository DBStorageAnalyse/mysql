# -*- coding: utf-8 -*-
# 解析 innodb库文件， 和 table_del.py 一起使用
# 做 库删除，表删除 的恢复， 按tab_id, idx_id 解析数据页。
import time, struct, sqlite3
import init, table_del

s = struct.unpack


class Unload_DB():
    def __init__(self):  # 解析函数
        super(Unload_DB, self).__init__()
        self.files = []

    # 文件信息
    def file_init(self, fn):
        self.files = []
        for f_name in fn:  # 每个文件头信息
            f = open(f_name, 'rb')
            data = f.read(16384)
            file_info = init.first_page(data)
            file_info.f_name = f_name
            file_info.file = f
            file_info.version = '5.x'
            self.files.append(file_info)
        return self.files

    # 正常解析 ibdata1 文件
    def unload_db(self, file_infos, db):
        print("Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        f = file_infos[0].file
        sys_tables_page, sys_columns_page, sys_indexes_page, sys_fields_page = init.boot_info(f)
        sys_tables, sys_columns, sys_indexes, sys_fields = init.sys_tables(f, sys_tables_page, sys_columns_page,
                                                                           sys_indexes_page, sys_fields_page)
        # sys_tables,sys_columns,sys_indexes,sys_fields = init.sys_tables(f,8,10,11,12)
        print("初始化 系统表 over ...\n")
        tab, db_all = init.init_all(f, sys_tables, sys_columns, sys_indexes, sys_fields)
        print("初始化 普通表 over ...\n")
        # tab_data = init.unload_tab(f,tab,db)
        # print("unload all over...\n")
        return tab, db_all  # db_all 只是存储了库名

    # 获取表结构,存储到sqlite
    def tab_info(self, tab, db):
        print('开始 获取表结构到sqlite ...')
        db = './db_1.db'  # 数据库文件名称
        f = open(db, 'w');
        f.close()
        conn = sqlite3.connect(db);
        cursor = conn.cursor()
        cursor.execute('create table tab_info(id integer primary key,db_name,tab_name,tab_type,tab_id,ind_id,col_sum)')
        cursor.execute(
            'create table col_info(id integer primary key,tab_id,col_id,col_name,col_type,col_len,prec,scale,notnull_is,pkey_is,var_len_is,unsign_is)')
        for table in tab:
            cursor.execute(
                "insert into tab_info(db_name,tab_name,tab_type,tab_id,ind_id,col_sum) values('%s','%s',%d,%d,%d,%d)" % \
                (table.db_name, table.tab_name, 0, table.tab_obj_id, table.index_id, table.col_sum))
            for col in table.col:
                if col.tab_obj_id == table.tab_obj_id:
                    cursor.execute(
                        "insert into col_info(tab_id,col_id,col_name,col_type,col_len,prec,scale,notnull_is,pkey_is,var_len_is,unsign_is) values(%d,%d,'%s','%s',%d,%d,%d,%d,%d,%d,%d)" % \
                        (table.tab_obj_id, col.col_id, col.col_name, col.col_type, col.col_len, col.prec, col.scale,
                         col.notnull_is, col.pkey_is, col.varlen_is, col.col_unsign))
        #   conn.commit()
        conn.commit()
        print('获取表结构到sqlite 完成...')

    # 正常解析表,解一个表
    def unload_tab(self, file_infos, table, db):
        f = file_infos[0].file
        tab_data = init.unload_tab(f, table, db)
        return tab_data

    # 正常解析表,解一个库的所有表,导出到dump文件
    def unload_all_tab(self, file_infos, table, db):
        f = file_infos[0].file
        tab_data = init.unload_tab1(f, table, db)
        return tab_data


# 遍历 ibdata1 文件，解析删除的表
def unload_innodb_del(f_name, db):
    f = open(f_name, 'rb')
    f_name1 = r'G:\mysql\ibdata1'  # 系统表文件
    f1 = open(f_name1, 'rb')
    tab = table_del.init_all_tab(db)  # 通过表结构db，初始化表结构  # 推荐，常用. 此db中要手工的加入 idx_id
    # tab = table_del.init_all_tab_2(f1)   # 通过暴力解析系统表初始化表结构, 好的 ibdata1有双份。需要手工筛选出正确的

    print('初始化 普通表 over...\n')
    table_del.unload_tab(f, tab, '')
    print("unload all over...")
    f.close()


def mysql(f_name, db):  # 解析 innodb 删除的表，删除记录，删除表，删除库。
    unload_innodb_del(f_name, db)


db = r'test/tab_3.db'  # 通过table_frm.py 从sql获取此db
f_name = r'G:\mysql\ibdata1'  # ibd_all
mysql(f_name, db)  # 解析删除的表
