# -*- coding: utf-8 -*-
# 定义 表结构

class File_Info():
    def __init__(self):
        self.endian = ''  # 平台软件的字节顺序(大小端),0:小端,1:大端
        self.f_name = ''  # 文件路径
        self.f_no = 0  # 文件号
        self.file = 0
        self.f_type = ''  # 文件类型
        self.blk_size = 0  # 文件的块/页 大小 (B)
        self.blk_sum = 0  # 文件的块/页 总数
        self.DBID = 0  # 数据库ID
        self.ts_id = 0  # 表空间ID
        self.ts_name = ''  # 表空间名
        self.version = ''  # 版本
        self.big_ts = 0  # 是否是大文件
        self.os = ''  # OS信息
        self.boot = 0  # 启动页


class st_db:
    def __init__(self):
        self.db_id = 0  # 数据库 ID
        self.db_version = ''  # 数据库版本
        self.page_size = 0  # 页面大小
        self.endian = 0  # 大小端. 0小端,1大端
        self.os = ''  # OS信息
        self.tab_sum = 1  # 表的数量
        self.tab = []  # 表


class st_table:
    def __init__(self):
        self.db_id = 0  # 数据库 ID
        self.db_name = ''  # 数据库名
        self.tab_version = ''  # 表版本
        self.tab_type = 0  # 表的类型
        self.tab_obj_id = 0  # 表的 object_id
        self.tab_name = ''  # 表名  #有的表只有object_id没有表名
        self.col_sum = 0  # 表的总列数
        self.nullable_sum = 0  # 可为空的总列数
        self.var_len_sum = 0  # 变长列的总列数
        self.col = []  # 列信息
        self.col_1 = []  # 数据页中的列结构信息
        self.pkey_sum = 0  # 主键总列数
        self.created = ''  # 表的创建时间
        self.ts_no = 0  # 表的表空间号
        self.index_id = 0  # 表的集索引id
        self.index_col = []  # 主键索引的列信息
        self.pgfirst = 0


class st_column:
    def __init__(self):
        self.tab_obj_id = 0  # 表的object_id
        self.col_id = 0  # 列id
        self.col_name = ''  # 列名
        self.col_type = ''  # 列的主数据类型
        self.col_len = 0  # 列长度
        self.prec = 0  # 精度
        self.scale = 0  # 小数位数
        self.collationid = 0  # 排序规则编号
        self.seed = 0  # 自增种子.  标识种子+标识增量
        self.def_data = 'NULL'  # 默认值
        self.col_unsign = 0  # 是否是有符号 0:有符号，1：无符号
        self.notnull_is = 0  # 是否可为空,1是不可为空，0是可为空
        self.varlen_is = 0  # 是否是变长
        self.pkey_is = 0  # 是否是主键


class st_page:
    def __init__(self):
        self.check1 = 0  # 校验和1
        self.page_no = 0  # 页面编号
        self.page_prev = 0  # 上一页
        self.page_next = 0  # 下一页
        self.page_type = 0  # 页面类型
        self.tablespace_id = 0  # 表空间ID
        self.slot_sum = 0  # 页面中slot数量
        self.rec_sum0 = 0  # 页面中的记录数量
        self.rec_sum1 = 0  # 页面中用户记录数量
        self.page_level = 0  # 页面level
        self.page_index_id = 0  # 页面所属的索引ID
        self.page_slot = []  # 页尾结构
        self.record = []  # 页面中的记录 结构


class st_rec_compact:
    def __init__(self):
        self.rec_off = 0  # 记录的起始偏移
        self.null_map = 0
        self.rec_h0 = 0
        self.rec_h1 = 0
        self.rec_h2 = 0
        self.col_data1 = []  # 记录的解析后正常列数据
        self.col_data2 = []  # 记录的解析后列数据
