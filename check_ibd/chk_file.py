# -*- coding: utf-8 -*-
# 统计，检测 数据文件, 给出报告
import time, struct, sqlite3, os.path, threading
import innodb_check

s = struct.unpack  # B H I


# 库文件信息
def f_info(f_name):
    f = open(f_name, 'rb')
    file_info1 = innodb_check.file_info_all(f)  # 汇总库文件信息
    return file_info1


# 主函数，界面加入多线程
class SCAN(threading.Thread):  # 类check继承自 QThread
    def __init__(self, file_info, start_pg_no, level, db):  # 解析函数
        super(SCAN, self).__init__()
        self.file_info = file_info
        self.start_pg_no = start_pg_no
        self.level = level
        self.db = db
        self.err_pages = []

    # 检测系统页,高级检测（暂时不支持）
    def chk_sys_page(self, f_name, db):
        self.mssql_scan(f_name, 0, db)
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

    # cursor.execute("create index index_1 on mssql_page(id,page_no)")  # 创建索引
    # cursor.execute("select page_no,page_type from mssql_page where page_type=15")  #

    # 检测mdf文件所有页, 单独开的线程
    def run(self):  #
        f_name = self.file_info.f_name;
        db = self.db
        begin = time.time()
        print('开始检测:%s, db:%s ' % (f_name, db))
        f = open(f_name, 'rb')
        conn = sqlite3.connect(db);
        cursor = conn.cursor()
        #   cursor.execute(" create table mssql_page(id integer primary key,offset,page_type,page_no,file_no,chk1,chk2,chk3,chk4,zero)")
        buff_size = 8 * 1024 * 1024  # buffer大小, 8M
        page_size = 16384  # 页面大小
        f_size = os.path.getsize(f.name)  # 只能处理文件,不能磁盘
        start1 = self.start_pg_no * page_size  # 扫描起始偏移
        f_size -= start1
        loop_1 = f_size // buff_size
        loop_1_1 = f_size % buff_size
        loop_2 = buff_size // page_size
        loop_2_1 = loop_1_1 // page_size
        self.file_info.real_sum = f_size // page_size

        for i in range(0, loop_1 + 1):  # 扫描文件的所有buffer块
            f.seek(i * buff_size + start1)
            data = f.read(buff_size)
            print("Buffer:%d/%d; Percent:%5.1f%% \r" % (i, loop_1, ((i + 1) / (loop_1 + 1)) * 100), end="")
            if (i < loop_1):  # 处理文件的所有buffer块
                for ii in range(0, loop_2):
                    pos1 = ii * page_size
                    data1 = data[pos1:pos1 + page_size]
                    data2 = s('>H', data1[24:26])
                    file = s('>I', data1[34:38])[0]
                    page = s('>I', data1[4:8])[0]

                    if self.level == 0:  # level 是检测的严格程度
                        chk1 = 1
                    elif self.level == 1:
                        chk1 = innodb_check.page_check_1(data1)  # 异或校验，慢
                    chk2 = innodb_check.page_check_2(data1)  # 特征值校验
                    chk3 = innodb_check.page_check_3(data1)  # 页尾校验

                    if page == i * loop_2 + ii:  # and file == self.file_info.f_no  # 没检验文件号
                        chk4 = 1  # 页号正确
                    else:
                        chk4 = 0
                    if page == 0 and data2[0] == 0:
                        chk2 = 1;
                        chk3 = 1;
                        chk1 = 1;
                        chk4 = 1
                    if chk2 != 1 or chk3 != 1 or chk1 != 1 or chk4 != 1:  # 损坏页
                        chk = str(chk2) + str(chk3) + str(chk1) + str(chk4)  # 校验结果: 特征值 + 页尾校验 + 异或 + 页号 (1:正常,0:不正常)
                        err_page = innodb_check.err_page()
                        err_page.blk_no = i * loop_2 + ii
                        err_page.page_no = page
                        err_page.chk_err = chk
                        err_page.page_type = data2[0]
                        self.err_pages.append(err_page)
            elif (i == loop_1):  # 处理文件尾部不足buffer的块
                for ii in range(0, loop_2_1):
                    off_set = i * buff_size + ii * page_size
                    if off_set > f_size - page_size:
                        break
                    pos1 = ii * page_size
                    data1 = data[pos1:pos1 + page_size]
                    data2 = s('>H', data1[24:26])
                    file = s('>I', data1[34:38])[0]
                    page = s('>I', data1[4:8])[0]
                    if self.level == 0:  # level 是检测的严格程度
                        chk1 = 1
                    elif self.level == 1:
                        chk1 = innodb_check.page_check_1(data1)  # 异或校验
                    chk2 = innodb_check.page_check_2(data1)  # 特征值
                    chk3 = innodb_check.page_check_3(data1)  # 页尾校验

                    if page == i * loop_2 + ii:  # and file == self.file_info.f_no
                        chk4 = 1  # RDBA
                    else:
                        chk4 = 0
                    if page == 0 and data2[0] == 0:
                        chk2 = 1;
                        chk3 = 1;
                        chk1 = 1;
                        chk4 = 1
                    if chk2 != 1 or chk3 != 1 or chk1 != 1 or chk4 != 1:  # 损坏页
                        chk = str(chk2) + str(chk3) + str(chk1) + str(chk4)  # 校验结果: 特征值 + 页尾校验 + 异或 + RDBA (1:正常,0:不正常)
                        err_page = innodb_check.err_page()
                        err_page.blk_no = i * loop_2 + ii
                        err_page.page_no = page
                        err_page.chk_err = chk
                        err_page.page_type = data2[0]
                        self.err_pages.append(err_page)
        f.close()
        print("\nFile size:%6.2f G, I/O:%4.1f M/s\n" % (
        f_size / 1024 / 1024 / 1024, f_size / 1024 / 1024 / (time.time() - begin)))  # I/O

    def get_return(self):
        return self.err_pages
