# -*- coding: utf-8 -*-
# 测试
import os.path,struct,sqlite3,binascii
import table_struct,pymssql,page
s = struct.unpack

def page_link1(f,pgfirst): #　文件，要解析的页链的起始页面号， 测试 链接
    f1 = open(r'C:\Users\zsz\PycharmProjects\mysql\unload_ibd\test\sys_file_4','w+b')
    page_size = 16384
    f_size = os.path.getsize(f.name)  # 获取文件大小，只能处理文件,不能磁盘
    f_pg_size = f_size//page_size
    next_page = pgfirst
    rec_sum = 0
    while(next_page != 0 and next_page<f_pg_size):  # 下一页不溢出
        pos1 = (next_page)*page_size
        f.seek(pos1)  # 要判断返回值，是否成功
        data = f.read(page_size)
        data1 = data[0:page_size]
        data2 = s('>I',data1[12:16])    # next_page
        data0 = s('>I',data1[8:12])     # pre_page
        data3 = s('>I',data1[34:38])    # ts_no
        data4 = s('>Q',data1[66:74])    # index_id
        data5 = s('>H',data1[64:66])    # index_level
        data6 = s('>H',data1[42:44])    # rec_sum0
        data7 = s('>H',data1[54:56])    # rec_sum1
        rec_sum += data7[0]
        if data4[0]==4 and data5[0]== 0 :   # obj_id,level
            print('page_no:%d,pre:%d,next:%d,ts_no:%d,obj_id:%d,level:%d,rec_sum0:%d,rec_sum1:%d,rec_sum:%d '%(next_page,data0[0],data2[0],data3[0],data4[0],data5[0],data6[0],data7[0],rec_sum))
      #  page1 = page.record(data1,table)  # 解析页面记录.  ***************
            f1.write(data)
        next_page += 1    # 下一页的页号
    f1.close()

def string_handle():
    f = open(r'C:\Users\zsz\Desktop\clob\xlsx_1','rb')    # 输入
    f1 = open(r'C:\Users\zsz\Desktop\clob\xx','w+b')
 #   f1 = open(r'.\role.txt','w',encoding='utf-8')       # 输出
    fsize = os.path.getsize(f.name)
    f.seek(0)
    data = f.read(fsize)
    data_out = ''
    for i in range(10):
        data1 = data[i:i+1]
        data2 = data[i+1:i+2]
        data0=data2+data1
        i = i+2
        data_out = str(data0,encoding="utf-16")
     #   data_out = data_out.encode('ascii')
       # sdata=struct.pack('c',data_out)

        data_out = binascii.a2b_uu(data_out)
       # data_out = binascii.b2a_uu(data0)
   # data_out = binascii.b2a_uu(data1)    # unhexlify b2a_uu
   # data_out = str(data0,encoding="ascii").strip()   # utf-8，gbk,ascii

        f1.write(data_out)



f_name = r'C:\Users\zsz\PycharmProjects\mysql\unload_ibd\test\ibdata'
f = open(f_name,'rb')
pgfirst = 1
page_link1(f,pgfirst)

#string_handle()

