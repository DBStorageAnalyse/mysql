# -*- coding: utf-8 -*-
# mysql碎片导出为文件.由sqlite数据库表给出碎片位置.
from os import path
import sqlite3,time

# 导出单个文件
def data_out1(file_in,file_out,db_name,sql):
 # 源文件，目标文件，数据库.  非多文件
    begin = time.time()
    print("Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(begin)))
    f1 = open (file_in,'rb')
    f2 = open(file_out,'w+b')
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
   # cursor.execute("select offset_1,offset_2 from link_1  where file_no_1>0 order by page_no_1 ") # 导出碎片  offset,offset
    cursor.execute(sql) # 导出页面
    print('Select over,begin out...')
    page_size = 16384   # mysql 页大小
    buffer_size = 1073741824  # 1G
    for i, val in enumerate(cursor):
        print("正在导出碎片: %d \r"%(i+1),end="")
        start_pos = val[0]
        end_pos = val[1] + page_size
        seg_size = end_pos-start_pos
        if seg_size > buffer_size : # 大碎片，分块存
            loop1 = (end_pos - start_pos)//buffer_size
            for ii in range(0,loop1+1):
                if ii == loop1 :    # 最后的不足buffer的
                    f1.seek(start_pos+ii*buffer_size)
                    data = f1.read(end_pos - start_pos-ii*buffer_size)
                    f2.write(data)
                else:       # 碎片中的整buffer的
                    f1.seek(start_pos+ii*buffer_size)
                    data = f1.read(buffer_size)
                    f2.write(data)
        else:   # 小碎片，需要加个写缓存
            f1.seek(start_pos)
            data = f1.read(end_pos-start_pos)
            f2.write(data)
    conn.close()
    f_size = path.getsize(f2.name)
    f1.close(); f2.close()
    end = time.time()
    print("\nDatetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end)),end='')  # current time
    print("\tUsed time: %d:"%((end-begin)//3600) + time.strftime('%M:%S',time.localtime(end-begin))) # 用时
    print("File size: %6.2f G, I/O: %4.1f M/s"%(f_size/1024/1024/1024,f_size/1024/1024/(end-begin)))

# 导出为多ibd文件
def data_out2(file_in,file_out,db_name):  # 源文件，目标文件，数据库.  多ibd文件
    begin = time.time()
    print("Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(begin)))
    file_path = file_out
    f1 = open (file_in,'rb')
   # f2 = open(file_out,'w+b')
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("select * from bb  order by page_sum ") # 导出语句
    values = cursor.fetchall()  # 取出数据
    for i_1 in range(len(values)):
        ts_no = values[i_1][0]
        print(file_path+'\\tab_%s.ibd'%ts_no)
        file_out = file_path+'\\tab_%s.idb'%ts_no
        f2 = open(file_out,'w+b')
   #     cursor.execute("select offset_1,offset_2 from link_1 where file_no_1=%s order by page_no_1;"%ts_no) # 导出语句
        cursor.execute("select offset_1,offset_2 from innodb_page  order by page_no;") # 导出语句
        print('Select over,begin out...')
        buffer_size = 1024*1024*8  # 8M 的buffer
        page_size = 16384   # mysql 页大小
        for i, val in enumerate(cursor):
            print("正在导出碎片: %d \r "%i,end="")
            start_pos = val[0]
            end_pos = val[1] + page_size
            loop1 = (end_pos - start_pos)//buffer_size
            for ii in range(0,loop1+1):
                if ii == loop1 :    # 最后的不足buffer的
                    f1.seek(start_pos+ii*buffer_size)
                    data = f1.read(end_pos - start_pos-ii*buffer_size)
                    f2.write(data)
                else:       # 碎片中的整buffer的
                    f1.seek(start_pos+ii*buffer_size)
                    data = f1.read(buffer_size)  #
                    f2.write(data)
        f2.close()
    conn.close()
    f_size = path.getsize(f2.name)
    f1.close()

    end = time.time()
    print("\nDatetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end)),end='')  # current time
    print("\tUsed time: %d:"%((end-begin)//3600) + time.strftime('%M:%S',time.localtime(end-begin))) # 用时
    print("File size: %6.2f G, I/O: %4.1f M/s"%(f_size/1024/1024/1024,f_size/1024/1024/(end-begin)))


# file_in = "\\\\.\\PhysicalDrive0"
# ts_no=1891
# index_id=5996
# sql = "select offset,offset  from innodb_page where ts_no=%d and index_id=%d  group by page_no"%(ts_no,index_id)
# file_in = r'z:\ext4-1.img'
# file_out = r'E:\mysql_20160409\data\t_17\aaaa'
# db_name = r'E:\mysql_20160409\ext4_1.db'
# data_out1(file_in,file_out,db_name,sql)
# # #data_out2(file_in,file_out,db_name)

