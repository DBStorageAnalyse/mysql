#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time,struct

def frm_scan(f_name):
    s = struct.unpack
    f = open (f_name,'rb')
    print("Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.localtime())))
    print("Scan: %s"%f.name)
    print("说明： 9:MyISAM , 12:InnoDB")
    begin = time.clock()
    f_size = os.path.getsize(f.name)
    buff_size = 2*1024*1024  # baffer大小，8M
    page_size = 4096         #页面大小, 扫描步长也是page_size
    loop_1 = f_size//buff_size  # 2m 的块 数量
    loop_1_1 = f_size%buff_size # 2m 的余数
    loop_2 = buff_size//page_size   #2m 里的页数量
    loop_2_1 = loop_1_1//page_size  #2m 的余数的页面数量

    for i in range(0,loop_1+1):
        f.seek(i*buff_size)
        data = f.read(buff_size)
        progress = (i/loop_1)*100
        print("Buffer: %d/%d; Percent:%6.2f %% \r"%(i,loop_1,progress),end="")
        if(i == loop_1):   # 处理文件尾部不足buffer的块
            for iii in range(0,loop_2_1):
                pos1 = iii*page_size
                data0 = data[pos1:pos1+page_size]
                data1 = s("<4B3H",data0[0:10])
                data2 = s("<BIHI3BIHII",data0[27:55])
                a1 = data1[0]==254 and data1[1]==1 and data1[4]==3 and data1[5]==4096
                a2 = data2[0]==2 and data2[2]==1280 and data2[5]==0 and data2[7]==0 and data2[8]==0
                if a1==1 and a2==1 :
                    print("offset:%d, DB_type:%d, DB_version:%d "%((i*buff_size+pos1),data1[3],data2[10]))
        elif(i < loop_1):  # 处理文件的所有buffer块
            for ii in range(0,loop_2): #loop_2   B H I
                pos1 = ii*page_size
                data0 = data[pos1:pos1+page_size]
                data1 = s("<4B3H",data0[0:10])
                data2 = s("<BIHI3BIHII",data0[27:55])
                a1 = data1[0]==254 and data1[1]==1 and data1[4]==3 and data1[5]==4096
                a2 = data2[0]==2 and data2[2]==1280 and data2[5]==0 and data2[7]==0 and data2[8]==0
                if a1==1 and a2==1 :
                    print("offset:%d, DB_type:%d, DB_version:%d "%((i*buff_size+pos1),data1[3],data2[10]))
    end = time.clock()
    time0 = (end - begin)/60
    time1 = (end - begin)%60
    print("Over! used time: %dm:%ds"%(time0,time1))
    f.close()


f_name = r'C:\Users\zsz\Desktop\data1\3\MySQL Server 5.1\data\ibdata1'
frm_scan(f_name)

