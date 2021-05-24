#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mysql innodb 拼接碎片, 物理连续的页
import sqlite3,time,struct
import innodb_check

class values1:
    def __init__(self):
        self.f_set = 0
        self.page_no = 0
        self.file_no = 0

class values2:
    def __init__(self):
        self.page_sum = 1
        self.file_no_1 = 0
        self.offset_1 = 0
        self.page_no_1 = 0
        self.offset_2 = 0
        self.page_no_2 = 0

def link_1(db_name):     #数据库文件名称
    begin = time.time()
    print("1.select all. Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(begin)))  # current time
    page_size = 16384
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("select offset,page_no,ts_no from innodb_page")
    v_1 = []  # 初始化数据集
    v_2 = []  # 结果集
    values = cursor.fetchall()  # 取出数据
    print("2.bigen into memery. Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))  # current time

    for i in range(0,len(values)):
        if i%100000==0:
            progress = (i/len(values))*100
            print("i:%d/%d; Percent:%5.1f%%;  \r"%(i,len(values),progress),end="")
        aa_1 = values1()
        aa_1.offset = values[i][0]
        aa_1.page_no = values[i][1]
        aa_1.file_no = values[i][2]     # file_no 就是 ts_no
        v_1.append(aa_1)
        del aa_1
    v_1.append(v_1[0])
    del values
    len1 = len(v_1)
    page_sum = 0
    print("3.bigen 合并. Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))  # current time
    for i in range(0,len1-1):  #  太多了，注意性能，小心爆内存
        if i%100000==0:
            progress = (i/(len1+1))*100
            print("i:%d/%d; Percent:%5.1f%%;  \r"%(i,len1,progress),end="")
        if i == 0:
            aa_2 = values2()
            aa_2.file_no_1 = v_1[0].file_no
            aa_2.offset_1 = v_1[0].offset
            aa_2.page_no_1 = v_1[0].page_no
            v_2.append(aa_2)
            del aa_2
    #    拼碎片
        a = v_1[i].file_no == v_1[i+1].file_no and (v_1[i+1].offset - v_1[i].offset)/page_size == (v_1[i+1].page_no - v_1[i].page_no) \
            and (v_1[i+1].page_no - v_1[i].page_no) <= 8
        if a == 1 :
            if v_2[-1].page_sum == 1:
                v_2[-1].offset_1 = v_1[i].offset
                v_2[-1].page_no_1 = v_1[i].page_no
                v_2[-1].file_no_1 = v_1[i].file_no
                v_2[-1].page_sum = 2
        if a == 0 :
            v_2[-1].offset_2 = v_1[i].offset
            v_2[-1].page_no_2 = v_1[i].page_no
            v_2[-1].page_sum = v_2[-1].page_no_2 - v_2[-1].page_no_1 + 1
            aa_2 = values2()   # 下一个碎片开始
            aa_2.file_no_1 = v_1[i+1].file_no
            aa_2.offset_1 = v_1[i+1].offset
            aa_2.page_no_1 = v_1[i+1].page_no
            aa_2.offset_2 = v_1[i+1].offset
            aa_2.page_no_2 = v_1[i+1].page_no
            aa_2.page_sum = 1
            if i != len(v_1)-2 :
                v_2.append(aa_2)
            del aa_2
    del v_1
    # link_1记录片段信息：片段号，片段中页数，起始页信息(物理偏移，页号，文件号)，结束页信息(物理偏移，页号，文件号)
    cursor.execute("create table link_1(l1_id integer primary key,l2_id,per_off,tail_off,offset_1,offset_2,page_sum,page_no_1,page_no_2,file_no_1)")
    cursor.execute("create index link1_idx on link_1(offset_1,page_no_1,file_no_1)")   # 创建索引
    print("4.bigen insert. Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))  # current time
    for i in range(0,len(v_2)):
        cursor.execute("insert into link_1(page_sum,offset_1,page_no_1,offset_2,page_no_2,file_no_1) values(?,?,?,?,?,?)",\
                       (v_2[i].page_sum,v_2[i].offset_1,v_2[i].page_no_1,v_2[i].offset_2,v_2[i].page_no_2,v_2[i].file_no_1))
        if i%100000 == 0:
            conn.commit()
    conn.commit()
    cursor.close()
    conn.close()
    print("5.over. Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))  # current time

def link_2(f_name):
    f = open (f_name,'rb')
    db = './by_si.db'  #数据库文件名称  =============================================
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    #cursor.execute("select offset,page_no,ts_no from innodb_page")
    cursor.execute("select offset_1,offset_2,page_no_1,page_no_2,file_no_1 from link_1 order by file_no_1,page_no_1")
    values = cursor.fetchall()  # 取出数据
    v_1 = []
    v_2 = []
    page_size = 16384

    for i in range(0,values.__len__()):
        aa_1 = values2()
        aa_1.offset_1 = values[i][0]
        aa_1.offset_2 = values[i][1]
        aa_1.page_no_1 = values[i][2]
        aa_1.page_no_2 = values[i][3]
        aa_1.file_no_1 = values[i][4]
        v_1.append(aa_1)
        del aa_1
    v_1.append(v_1[0])
    page_sum = 0
    for i in range(0,v_1.__len__()-1):  #  太多了，注意性能，小心爆内存
        if i == 0:
            aa_2 = values2()
            v_2.append(aa_2)
            del aa_2
    #   拼碎片
        offset = v_1[i].offset_2 + page_size
        f.seek(offset)
        data1 = f.read(page_size)
        chk2 = innodb_check.page_check_2(data1)
        chk = struct.unpack('>I',data1[0:4])
        if chk2 == 1 :
            for ii in range(i,len(v_1)-1):
                if v_1[ii].page_no_1 > v_1[i].page_no_2 + 2 :
                    break
                bool =  v_1[i].file_no_1 == v_1[ii].file_no_1 and  v_1[i].page_no_2 == v_1[ii].page_no_2 - 2
                if bool == 1 :
                    pos = 0         # 进行半页面组合
                    f.seek(v_1[ii].offset_1 - page_size)
                    data2 = f.read(page_size)
                    for i in range(0,15):
                        data = data1[0,512*(i+1)] + data2[512*(i+1),512*(16)]
                        chk =innodb_check.page_check_1(data)
                        if chk == 1: # 通过校验
                            pos = i + 1
                    if pos != 0:
                        ok = 0

                    else :
                        ok = 0

                    if v_2[-1].page_sum == 1:
                        v_2[-1].offset_1 = v_1[i].offset_1
                        v_2[-1].page_no_1 = v_1[i].page_no_1
                        v_2[-1].file_no_1 = v_1[i].file_no_1
                        v_2[-1].page_sum = 2
                if bool == 0 :
                    v_2[-1].offset_2 = v_1[ii].offset_2
                    v_2[-1].page_no_2 = v_1[ii].page_no_2
                    v_2[-1].page_sum = v_2[-1].page_no_2 - v_2[-1].page_no_1 + 1
                    aa_2 = values2()   # 下一个碎片开始
                    aa_2.file_no_1 = v_1[i+1].file_no
                    aa_2.offset_1 = v_1[i+1].offset
                    aa_2.page_no_1 = v_1[i+1].page_no
                    aa_2.offset_2 = v_1[i+1].offset
                    aa_2.page_no_2 = v_1[i+1].page_no
                    aa_2.page_sum = 1
                    if i != v_1.__len__()-2 :
                        v_2.append(aa_2)
                    del aa_2



# db_name = r'C:\Users\zsz\PycharmProjects\mysql\test\mysql_1.db'
# link_1(db_name)
#
