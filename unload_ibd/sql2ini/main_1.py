# -*- coding: cp936 -*-
__author__ = 'x'

import re
import ConfigParser
import os
import sys


# 将table信息写入文件
def save_table(table):
    conf = ConfigParser.ConfigParser()
    # 写入数据库信息
    conf.add_section('database')
    conf.set('database', 'db_type', 30)
    # 写入表信息
    conf.add_section('table_%d' % table.num)
    conf.set('table_%d' % table.num, 'table_name', table.table_name)
    conf.set('table_%d' % table.num, 'table_type', table.table_type)
    conf.set('table_%d' % table.num, 'column_sum', table.column_sum)
    conf.set('table_%d' % table.num, 'nullmap_is', table.nullmap_is)
    # 写入列信息
    column_num = 0
    for column in table.columns:
        conf.add_section('column_%d' % column_num)
        conf.set('column_%d' % column_num, 'column_name', column.column_name)
        conf.set('column_%d' % column_num, 'column_data_type', column.column_data_type)
        conf.set('column_%d' % column_num, 'column_length', column.column_length)
        conf.set('column_%d' % column_num, 'column_var_is', column.column_var_is)
        conf.set('column_%d' % column_num, 'column_define', column.column_define)
        conf.set('column_%d' % column_num, 'column_pkey_is', column.column_pkey_is)
        conf.set('column_%d' % column_num, 'column_nullable_is', column.column_nullable_is)
        column_num += 1
    conf.write(file('%s\\table_%d.ini' % (conf_dir, table.num), 'w'))


class Column:
    def __init__(self):
        self.column_name = ''
        self.column_data_type = ''
        self.column_length = 0
        self.column_var_is = 1
        self.column_define = ''
        self.column_pkey_is = 0
        self.column_nullable_is = 1  # 是否可以为空，1是0否


class Table:
    def __init__(self, num, name):
        self.num = num  # 表编号，从1开始
        self.table_name = name
        self.table_type = 1  # 暂时（2015年1月5日）只有这一个选项
        self.columns = list()

    @property
    def column_sum(self):
        return len(self.columns)

    @property
    def nullmap_is(self):
        nullable = False
        for column in self.columns:
            nullable = nullable or (column.column_nullable_is == 1)
        return int(nullable)


# 获取主键名列表
def parse_primary_key(create_stmt):
    str_keys = re.search(r'PRIMARY KEY \((.*)\)', create_stmt)
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


def parse_nullable(column_stmt):
    if re.search("NOT NULL", column_stmt):
        return 0
    else:
        return 1


def parse_len(type_name, column_stmt):
    type_len = {'text': -1, 'mediumtext': -1, 'longtext': -1, 'date': 4, 'datetime': 5, 'timestamp': 4, 'smallint': 2,
                'decimal': 10, 'int': 4, 'bigint': 8, 'float': 4, 'double': 8, 'enum': 4}
    if type_name in type_len:
        return type_len[type_name]
    else:
        return int(re.search(r'\w+\((\d+)\)', column_stmt).group(1))


# 从create语句中提取列信息
def parse_create_stmt(create_stmt):
    pkeys = parse_primary_key(create_stmt)
    iter = re.finditer(r'\n  `(\w+)` (\w+).*', create_stmt)
    columns = list()
    for m in iter:
        column = Column()
        column.column_name = m.group(1)
        column.column_data_type = m.group(2)
        column.column_length = parse_len(m.group(2), m.group())
        column.column_var_is = int(m.group(2) in ('varchar', 'char'))  # 变长类型
        column.column_define = parse_default_value(m.group())
        column.column_pkey_is = int(m.group(1) in pkeys)
        column.column_nullable_is = parse_nullable(m.group())
        columns.append(column)
    return columns


def parse_engine(create_stmt):
    return re.search(r'ENGINE=(\w+)', create_stmt).group(1)


sql_file_name = 'obdvin_log.sql'
if len(sys.argv) > 1:
    sql_file_name = sys.argv[1]
conf_dir = re.search(r'(.*)\.sql', sql_file_name).group(1)

f = open(sql_file_name)
data = f.read()
os.makedirs(conf_dir)
# 用于匹配create块
pattern_create_stmt = re.compile(r'CREATE TABLE `(\w+)` \(\n(.+\n)*')

iter = pattern_create_stmt.finditer(data)
table_num = 1
for m in iter:
    if parse_engine(m.group()) not in ('InnoDB'):
        continue
    table = Table(table_num, m.group(1))
    table.columns = parse_create_stmt(m.group())
    save_table(table)
    table_num += 1
