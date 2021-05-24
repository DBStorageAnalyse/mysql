# -*- coding: utf-8 -*-
# 表结构信息获取. 从建表sql中获取数据库信息，写出到sqlite
import re, sqlite3


class Column:
    def __init__(self):
        self.col_id = 0
        self.column_name = ''  # 列名
        self.data_type = ''  # 数据类型
        self.prec = 0  # 括号数1
        self.scale = 0  # 括号数2
        self.column_len = 0  # 数据长度
        self.var_len_is = 1  # 是否是边长
        self.define = ''  # 默认值
        self.notnull_is = 0  # 是否可以为空， 1不可为空
        self.col_unsign = 0  # 是否是有符号 0:有符号，1：无符号
        self.pkey_is = 0
    # self.enums = list() # enum 类型


class Table:
    def __init__(self, num, name):
        self.num = num  # 表编号，从1开始
        self.tab_name = name
        self.tab_id = 0  # 表的 obj_id
        self.index_id = 0  # 表的 index_id
        self.col = []

    @property
    def col_sum(self):
        return len(self.col)

    @property
    def nullable_sum(self):  # 可为空的列数
        nullable_sum = 0
        for column in self.col:
            if column.notnull_is == 0:
                nullable_sum += 1
        return int(nullable_sum)

    @property
    def var_len_sum(self):  # 变长列的列数
        var_len_sum = 0
        for column in self.col:
            if column.var_len_is == 1:
                var_len_sum += 1
        return int(var_len_sum)


# 列数据长度
def parse_len(type_name, column_stmt):
    type_len = {'text': 0, 'mediumtext': 0, 'longtext': 0, 'date': 3, 'datetime': 5, 'timestamp': 4, \
                'tinyint': 1, 'smallint': 2, 'mediumint': 3, 'int': 4, 'bigint': 8, 'float': 4, 'double': 8, 'enum': 4,
                'bit': 1}
    if type_name in type_len:
        return type_len[type_name]
    elif type_name == 'decimal':
        m1 = int(re.search(r'\((\d+),(\d+)\)', column_stmt).group(1))
        return (m1 + 1) // 2
    elif type_name == 'char':
        return int(re.search(r'\w+\((\d+)\)', column_stmt).group(1))  # mysql
    else:
        return 0


# 获取主键名列表
def parse_primary_key(create_stmt):
    str_keys = re.search(r'PRIMARY KEY .*\((.*)\)', create_stmt)  #
    if str_keys:
        return re.findall(r'`(\w+)`', str_keys.group(1))
    else:
        return list()


# 获取默认值
def parse_default_value(column_stmt):
    m = re.search('DEFAULT ([^ ,]*)', column_stmt)
    if m:
        return m.group(1)
    else:
        return 'NULL'


# 从create语句中提取列信息
def parse_create_stmt(create_stmt):
    pkeys = parse_primary_key(create_stmt)
    #  iter = re.finditer(r'\n`(\w+)`  (\w+).*', create_stmt)  #　可改, Navicat
    iter = re.finditer(r'\n  `(\w+)` (\w+).*', create_stmt)  # 可改, Navicat, phpMyAdmin SQL
    columns = [];
    col_id = 0
    for m in iter:  # 每一行
        column = Column()
        col_id += 1  # 列id
        column.col_id = col_id
        column.column_name = m.group(1)
        column.data_type = m.group(2)
        column.column_len = parse_len(m.group(2), m.group())
        column.var_len_is = int(m.group(2) in (
        'char', 'varchar', 'text', 'mediumtext', 'longtext', 'tinytext', 'longtblob', 'blob', 'mediumblob',
        'tinyblob'))  # 变长类型
        column.column_define = parse_default_value(m.group())
        column.pkey_is = int(m.group(1) in pkeys)
        if re.search("unsigned", m.group()):
            column.col_unsign = 1  # 1：col_unsign
        else:
            column.col_unsign = 0
        if re.search("NOT NULL", m.group()):
            column.notnull_is = 1  # 1：not null,0:nullable
        else:
            column.notnull_is = 0

        if column.data_type == 'decimal' or column.data_type == 'double':
            m1 = re.search(r'\((\d+),(\d+)\)', m.group())
            try:
                column.prec = int(m1.group(1))
                column.scale = int(m1.group(2))
            except AttributeError:  # double 用的默认（10,0）,sql中没有（）
                column.prec = 10
                column.scale = 0
        columns.append(column)
    return columns


# 将table信息写入sqlite的表中
def save_table2(table, out_db):
    conn = sqlite3.connect(out_db)  # 打开数据库
    cursor = conn.cursor()
    cursor.execute("insert into tab_info(tab_id,tab_name,col_sum,nullable_sum,var_len_sum) values(%d,'%s',%d,%d,%d)" % \
                   (table.num, table.tab_name, table.col_sum, table.nullable_sum, table.var_len_sum))
    for col in table.col:
        cursor.execute(
            "insert into col_info(tab_id,col_id,col_name,col_type,col_len,prec,scale,notnull_is,pkey_is,var_len_is,unsign_is) values(%d,%d,'%s','%s',%d,%d,%d,%d,%d,%d,%d)" % \
            (table.num, col.col_id, col.column_name, col.data_type, col.column_len, col.prec, col.scale, col.notnull_is,
             col.pkey_is, col.var_len_is, col.col_unsign))
    conn.commit()


# 主函数
def table_frm(sql_file_name, out_db):
    f = open(sql_file_name, encoding='utf-8')
    data = f.read()
    f1 = open(out_db, 'wb');
    f1.close()
    conn = sqlite3.connect(out_db)  # 打开数据库
    cursor = conn.cursor()
    cursor.execute(
        "create table tab_info(id integer primary key,db_name,tab_name,tab_type,tab_id,ind_id,ts_no,col_sum,nullable_sum,var_len_sum)")
    cursor.execute(
        "create table col_info(id integer primary key,tab_id,col_id,col_name,col_type,col_len,prec,scale,notnull_is,pkey_is,var_len_is,unsign_is)")
    pattern_create_stmt = re.compile(
        r'CREATE TABLE `(\w+)` \(\n(.+\n)*')  # 用于匹配mysql的标准create块, Navicat， phpMyAdmin SQL Dump
    #  pattern_create_stmt = re.compile(r'CREATE TABLE `(\w+)`.`(\w+)` \(\n(.+\n)*')
    iter = pattern_create_stmt.finditer(data)
    table_num = 1
    for m in iter:
        table = Table(table_num, m.group(1))
        table.col = parse_create_stmt(m.group())  # m.group() 一个create 语句
        save_table2(table, out_db)
        print("table:%s" % (table.tab_name))
        table_num += 1


sql_file_name = r'test/tab_3.txt'
out_db = r'test/tab_3.db'
table_frm(sql_file_name, out_db)

# phpMyAdmin SQL Dump的 主外键的说明是不同，是放在所有表创建完之后，创建索引的语句中。所以解析不了主键信息。
