
## mysql innodb 文件页面扫描/拼接

innodb_scan.py  # 主文件
innodb_check.py # 校验算法
link_1.py，init.py 是把页面合并为碎片

link_2.py  碎片拼接为块
通过半页，来链接两个碎片。
先查每个片段最后一页的后面是否是一个半页。如果是一个半页（通不过check_log且页号+1），通过半页去匹配: (少量，精准)
找片段起始页为页号+2的片段，如果找到，去读此片段第一页前的一页，去匹配这两个片段，先看check_log是否相同。如果不同，说明不是一个块的。
如果相同，这两个片段就可以连接在一起为一个块，连接位置通过crc32来确定，如果crc32确定不通过，说明这两个不是一个块。 这个片段就到此结束，为一个块的结尾。

页面校验有： 页头特征值，页尾校验，页头checksum校验.记录的都是好的页面(包含首页，0类型页)，没有半页的.
扫描结果存放在数据库里: innodb_page(scan_file,id integer primary key,offset,ts_no,page_no,page_type,pre_page,next_page,chk)
数据页获取不到记录的总列数

# 记录片段信息：片段号，片段中页数，起始页信息(物理偏移，页号，文件号)，结束页信息(物理偏移，页号，文件号)
# 记录块信息：块号，块中片段数，起始片段信息(片段编号,起始页号,文件号)，结束片段信息

C:\Python34\Scripts> cxfreeze C:\Users\zsz\PycharmProjects\sqlserver\test\ui_scan.py --target-dir=C:\Users\zsz\PycharmProjects\sqlserver\test\tt
 --base-name=C:\Python34\Lib\site-packages\cx_Freeze\bases\Win32GUI.exe
cd C:\Users\zsz\PycharmProjects\sqlserver\test
pyinstaller -F C:\Users\zsz\PycharmProjects\sqlserver\test\ui_scan.py
history: ----------------------------------------------------------------
v1.0.0  2015-04-01
无GUI界面,开发测试版本
scan 速度： I/O:   80 M/s
1T的库 --> 55380414 recoders --> 1.75G

v1.1.0  2016-04-10
修复bugs，增强功能
v1.2.0  2016-05-24
加入界面，完善功能
v1.3.0  2016-06-21
3库联调
v1.4.0  2016-07-05
完善导出模块
v1.4.2  2016-07-06
修复link_1中的bug
修复结束偏移的设置
v1.5.0  2016-08-27
加入多线程，界面加入进度显示




