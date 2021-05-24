#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  innodb 碎片扫描，生成sqlite中间库. innodb都是大端的. 此模块可以单独使用
from PyQt5.QtCore import QThread, pyqtSignal
import time, struct, sqlite3, logging
import innodb_check


# 扫描线程, 需要传参数
class Scan_1(QThread):  # 类Scan_1继承自 QThread
    PUP = pyqtSignal(int)  # 更新进度条的信号
    LUP = pyqtSignal(str)

    def __init__(self, parent=None):  # 解析函数
        super(Scan_1, self).__init__(parent)
        self.f_name = 0
        self.db_name = 0
        self.logging = 0
        self.start_off = 0
        self.end_off = 0
        self.endian = 0
        self.page_size = 0
        self.scan_size = 0
        self.file_infos = []

    def run(self):
        self.innodb_scan(self.f_name, self.db_name, self.logging, self.start_off, self.end_off, self.endian,
                         self.page_size, self.scan_size)

    # 扫描页面碎片
    def innodb_scan(self, f_name, db_name, logging, start_off, end_off, endian, page_size, scan_size):
        # f_name是要扫描的源文件，start_off扫描的起始偏移，[chk_level是校验等级]，db_name输出的db名
        # logging.basicConfig(level=logging.DEBUG,format='%(message)s',filename='%s_%s.log'%(db_name[:-3],time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))),filemode='w')
        s = struct.unpack
        begin = time.time()
        print("Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin)))  # current time
        print('f_name:%s\ndb_name:%s ' % (f_name, db_name))
        logging.info("\nDatetime: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin)) + '\t 扫描开始...')
        logging.info('f_name:%s\ndb_name:%s\n' % (f_name, db_name))
        f = open(f_name, 'rb')
        f1 = open(db_name, 'w');
        f1.close()  # 数据库文件
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(
            "create table innodb_page(id integer primary key,offset,ts_no,page_no,page_type,pre_page,next_page,index_level,index_id,rec_sum)")  # 大表，用于小库
        #  cursor.execute("create table link_1(l1_id integer primary key,l2_id,per_off,tail_off,offset_1,offset_2,page_sum,page_no_1,page_no_2,file_no_1)")
        cursor.execute("create index page_idx on innodb_page(ts_no,page_no,index_id)")  # 创建索引
        scan_size = scan_size  # 扫描 的步长 ,精度, 影响I/O速度
        buff_size = 8 * 1024 * 1024  # baffer大小， 8M, 32M
        page_size = page_size  # 页面大小
        start = start_off  # //512*512
        f_size = end_off - start  # 扫描总大小
        loop_1 = f_size // buff_size
        loop_1_1 = f_size % buff_size
        loop_2 = buff_size // scan_size
        loop_2_1 = loop_1_1 // scan_size
        sum = 0
        page_0 = 0;
        page_8 = 0;
        page_17855 = 0

        for i in range(0, loop_1 + 1):  # 处理文件的所有buffer块
            f.seek(i * buff_size + start)
            data = f.read(buff_size + page_size)
            # if i%(loop_1//1000+1) == 0:
            #     progress = (i/(loop_1+1))*100
            #     now = time.time()
            #     print("Buffer:%d/%d; Percent:%5.1f%%; Find:%d,%dM, I/O:%4.1fM/s\r"%(i,loop_1,progress,sum,sum*page_size/1024/1024,i*8/(now-begin+1)),end="")
            if (i < loop_1):  # 处理文件的所有整buffer块
                for ii in range(0, loop_2):
                    pos1 = ii * scan_size  #
                    data1 = data[pos1:pos1 + page_size]
                    fmt = '>4I2HIHQI'
                    data2 = s(fmt, data1[0:38])
                    chk2 = innodb_check.page_check_2(data1)  # 特征值校验
                    if chk2 == 1:
                        chk3 = innodb_check.page_check_3(data1)  # 页尾校验
                        if chk3 == 1:
                            chk1 = 1  # innodb_check.page_check_1(data1) #====页头 CRC 校验,很慢=================
                            if chk1 == 1:
                                rec_sum = 0
                                if data2[7] == 0:  # 0页
                                    page_0 += 1
                                    index_id = 0
                                    index_level = 0
                                elif data2[7] == 8:  # 文件首页
                                    page_8 += 1
                                    index_id = 0
                                    index_level = 0
                                elif data2[7] == 17855:  # 数据页
                                    page_17855 += 1
                                    rec_sum_1 = s('>H', data1[54:56])
                                    index_1 = s('>HII', data1[64:74])
                                    index_level = index_1[0]
                                    index_id = index_1[2]
                                    rec_sum = rec_sum_1[0]  # 记录数据量
                                else:
                                    index_id = 0
                                    index_level = 0
                                sum += 1
                                offset = i * buff_size + ii * scan_size
                                ii += page_size / scan_size
                                cursor.execute("insert into innodb_page(offset,ts_no,page_no,page_type,pre_page,next_page,index_level,index_id,rec_sum) \
                                values(?,?,?,?,?,?,?,?,?)", (
                                offset, data2[9], data2[1], data2[7], data2[2], data2[3], index_level, index_id,
                                rec_sum))
                                if sum % 10000 == 0:
                                    conn.commit()  # 每10000条commit一次, 频繁提交会影响I/O速度

            elif (i == loop_1):  # 处理文件尾部不足buffer的块
                for ii in range(0, loop_2_1):
                    pos1 = ii * scan_size
                    data1 = data[pos1:pos1 + page_size]
                    fmt = '>4I2HIHQI'
                    data2 = s(fmt, data1[0:38])
                    offset = i * buff_size + ii * scan_size  # ========
                    if offset > f_size:
                        break
                    chk2 = innodb_check.page_check_2(data1)
                    if chk2 == 1:
                        chk3 = innodb_check.page_check_3(data1)
                        if chk3 == 1:
                            chk1 = 1  # innodb_check.page_check_1(data1)
                            if chk1 == 1:
                                rec_sum = 0
                                if data2[7] == 0:
                                    page_0 += 1
                                    index_level = 0
                                    index_id = 0
                                elif data2[7] == 8:
                                    page_8 += 1
                                    index_level = 0
                                    index_id = 0
                                elif data2[7] == 17855:
                                    page_17855 += 1
                                    rec_sum_1 = s('>H', data1[54:56])
                                    index_1 = s('>HII', data1[64:74])
                                    index_level = index_1[0]
                                    index_id = index_1[2]
                                    rec_sum = rec_sum_1[0]  # 记录数据量
                                else:
                                    index_level = 0
                                    index_id = 0
                                sum += 1
                                ii += page_size / scan_size
                                cursor.execute("insert into innodb_page(offset,ts_no,page_no,page_type,pre_page,next_page,index_level,index_id,rec_sum) \
                                values(?,?,?,?,?,?,?,?,?)", (
                                offset, data2[9], data2[1], data2[7], data2[2], data2[3], index_level, index_id,
                                rec_sum))

            if i % (loop_1 // 1000 + 1) == 0 or i == loop_1:  # 输出扫描进度
                progress = ((i + 1) / (loop_1 + 1)) * 100
                now = time.time()
                speed = i * 8 / (now - begin + 1)
                print("Buf:%d/%d,Percent:%4.1f%%, Find:%d=%dM, I/O:%4.1fM/s,Time:%dMin\r" % (
                i, loop_1, progress, sum, sum * page_size / 1024 / 1024, speed,
                (loop_1 + 1 - i) * 8 / ((speed + 0.01) * 60)), end="")
                self.PUP.emit(progress)  # 传递参数
                self.LUP.emit(" Buf:%d/%d,Percent:%4.1f%%, Find:%d=%dM, I/O:%4.1fM/s,Time:%dMin" % (
                i, loop_1, progress, sum, sum * page_size / 1024 / 1024, speed,
                ((loop_1 + 1 - i) * 8 / ((speed + 0.01) * 60) + 1)))  # 传递参数

        print("\n总页数: %d, 空页数: %d, 数据页: %d,文件头: %d" % (sum, page_0, page_17855, page_8))  # 总页数,空页数,数据页数
        logging.info("\n总页数: %d, 空页数: %d, 数据页: %d,文件头: %d" % (sum, page_0, page_17855, page_8))
        conn.commit()
        cursor.close();
        conn.close();
        f.close()
        end = time.time()
        print("Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)), end='')  # current time
        print(" ,Used: %d:" % ((end - begin) // 3600) + time.strftime('%M:%S', time.localtime(end - begin)),
              end='')  # 用时
        print(" ,f_size:%5.2fG ,I/O: %4.1fM/s" % (f_size / 1024 / 1024 / 1024, f_size / 1024 / 1024 / (end - begin)))
        logging.info("Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)) + "\t 扫描完成,用时: %d:" % (
                    (end - begin) // 3600) + time.strftime('%M:%S', time.localtime(end - begin)))
        logging.info("File size:%6.2fG, 平均I/O:%4.1fM/s" % (
        f_size / 1024 / 1024 / 1024, f_size / 1024 / 1024 / (end - begin + 1)))
