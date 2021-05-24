# -*- coding: utf-8 -*-
import os
import frm_reader


# 引用官方工具 frm_reader
def frm_header2(frm_path):
    db_name = 'db_name'
    table_name = frm_path.split("/")[-1].split("\\")[-1].split(".")[0]  # 从文件名获取表名
    frm = frm_reader.FrmReader(db_name, table_name, frm_path, {})
    frm.show_statistics()  # 显示文件信息
    create_table_statement = frm.show_create_table_statement()  # 显示建表语句
    return create_table_statement


# 处理文件夹写下所有的frm， 把所有表的建表语句都写到一个sql文件里
def frm_all(dir_path, sql_path):
    sql_file = open(sql_path, 'w')
    frm_files = os.listdir(dir_path)
    for frm_path in frm_files:
        frm_path = os.path.join(dir_path, frm_path)
        print(frm_path)
        create_table_statement = frm_header2(frm_path)
        sql_file.write(create_table_statement + '\n\n')


dir_path = r'G:\mysql\mysql重要库数据表\dyun_swotbbs'  # uc_friends G:\mysql\mysql重要库数据表\dyun_swotbbs/katt2_activelogs.frm
sql_path = '%s.sql' % dir_path.split("/")[-1].split("\\")[-1]  # 库名.sql
frm_all(dir_path, sql_path)

# 生成sql文件后，再用 table_frm.py 解析转换到 db.
