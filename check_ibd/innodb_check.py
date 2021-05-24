 # -*- coding: utf-8 -*-
# innodb page_check 校验算法
import struct,os
s = struct.unpack       # B,H,I,Q

class file_info:
    def __init__(self):
        self.f_name = ''    # 现在的物理路径
        self.f_no = 0
        self.g_no = 0
        self.f_size0 = 0    # 文件真实大小(文件系统属性中的)
        self.f_size1 = 0    # 文件头记录的总页数
        self.real_sum = 0   # 文件实际的总页数
        self.file_type = ''
        self.version = ''   # 现在版本
        self.db_name = ''
        self.err_pages = []

class err_page:
    def __init__(self):
        self.blk_no = 0            # 块号
        self.page_no = 0            # 页号
        self.page_type = 0            # 页类型
        self.chk_err = ''           # 错误信息

# 首页获取文件信息
def file_info_all(f):
    data = f.read(512)
    file_info1 = file_info()
    data_1  = s(">III",data[38:50])
    file_info1.f_name = f.name    # 获取文件名
    file_info1.file_type = 'ibd'
    file_info1.db_name = ''
    file_info1.f_no = data_1[0]
    file_info1.f_size0 = os.path.getsize(f.name)    # 文件大小
    file_info1.f_size1 = data_1[2]    # page_sum
    file_info1.version = '5.x'  # 现在版本
    return file_info1

# 页头特征值校验
def page_check_2(data): #
    fmt = '>4I2HIHQI'
    data = s(fmt,data[0:38])
    #
    if data[0] != 0  and data[4] == 0 and data[6] != 0  and \
        (data[7] in (17855,0,2,3,4,5,6,7,8,9,10,11,12)):  #
    # data[0] 校验,data[1] page_no,data[6] 日志位置LSN,data[7] page_type,data[8] 仅在(0,0)页使用 ,data[9] ts_no,
        if data[1] == 0 and data[2] == 0 and data[3] == 0 :  #包含首页，0类型页
            if data[9] == 0 and data[8] != 0:
                return 1
            elif data[9] != 0 and data[8] == 0:
                return 1
        elif data[1] != 0 and data[8] == 0 :
            return 1

# 页尾校验
def page_check_3(data):
    data1 = s('>I',data[16380:16384])
    data2 = s('>I',data[20:24])
    if data1[0]==data2[0] :
        return 1

# 页头 CRC 校验, 很慢
def page_check_1(data):
        chk = s('>I',data[0:4])
        checksum = 0
        checksum = ut_fold_binary(data[4:26]) + ut_fold_binary(data[38:16376])
        checksum = checksum&0xFFFFFFFF
        if chk == checksum :
            return 1
def ut_fold_ulint_pair(n1, n2):
         var = (n1^n2^1653893711) << 8
         var = var & 0xffffffff
         var = ((var + n1)^1463735687) + n2
         return var & 0xffffffff
def ut_fold_binary(data):
        fold = 0
        len1 = len(data)
        str_end	= len1&0xFFFFFFF8
        # 高位
        for i in range(0,str_end):
            aa = s('<B',data[(i):(i+1)])
            fold = ut_fold_ulint_pair(fold,aa[0])
        # 低位
        c = len1&7
        if c == 7:
            for i in range(0,7):
                aa = s('<B',data[str_end+i:str_end+i+1])
                fold = ut_fold_ulint_pair(fold, aa[0])
        elif c == 6:
            for i in range(0,6):
                aa = s('<B',data[str_end+i:str_end+i+1])
                fold = ut_fold_ulint_pair(fold, aa[0])
        elif c == 5:
            for i in range(0,5):
                aa = s('<B',data[str_end+i:str_end+i+1])
                fold = ut_fold_ulint_pair(fold, aa[0])
        elif c == 4:
            for i in range(0,4):
                aa = s('<B',data[str_end+i:str_end+i+1])
                fold = ut_fold_ulint_pair(fold, aa[0])
        elif c == 3:
            for i in range(0,3):
                aa = s('<B',data[str_end+i:str_end+i+1])
                fold = ut_fold_ulint_pair(fold, aa[0])
        elif c == 2:
            for i in range(0,2):
                aa = s('<B',data[str_end+i:str_end+i+1])
                fold = ut_fold_ulint_pair(fold, aa[0])
        elif c == 1:
            for i in range(0,1):
                aa = s('<B',data[str_end+i:str_end+i+1])
                fold = ut_fold_ulint_pair(fold, aa[0])
        return fold


