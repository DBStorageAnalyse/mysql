# -*- coding: utf-8 -*-
mysql 解析工具
解析 mysql innodb1,*.ibd文件
注意：有些数据类型解析与mysql版本有关。

支持mysql5.5， 5.6， 5.7


cd /d C:\Python34\Scripts
cxfreeze C:\Users\zsz\PycharmProjects\sqlserver\test\ui_unload.py --target-dir=C:\Users\zsz\PycharmProjects\sqlserver\test\tt
pyinstaller -F C:\Users\zsz\PycharmProjects\sqlserver\test\ui_unload.py
History -----------------------------------------------------
mysql v1.0.1  2015-2-13
无GUI界面，开发测试版本
能解析 innodb 的 compact和Redundant 记录
mysql v1.0.2  2015-7-17
mysql v1.0.4  2015-12-5
mysql v1.1.0  2015-12-9
innodb 的正常解析
数据库删除，表删除的解析
mysql v1.2.0  2016-1-2
加入 GUI界面
2016-01-03   V1.3.0
三库 联调 1
2016-03-21   V1.4.0
增强功能，加入行溢出解析
可解析blob等大字段
可导出一个库为dump文件（还需完善）
2016-03-23   V1.5.0
修复严重bug
完善索引解析
2016-03-29   V1.5.2
完善删除恢复部分
完善table_frm,sql转sqlite
2016-04-13   V1.5.4
完善删除恢复部分
放弃table_frm，用官方自带的转换工具。代码在scan_frm项目里。
2016-05-20   V1.5.8
加入注册验证
2016-06-21   V1.6.0
三库 联调 2

2017-04-01   V1.6.0
适应win10 高分屏显示：
加大表格行宽，加大关于标签
修复bugs


数据类型解析 要加入 版本判断和字符编码判断, 版本和编码需要人工指定


下版本处理 版本号，多文件,decimal解析 等问题
----------------------------------------------------------------------------------
#create table db_info(db_id,db_version,os,tab_sum,create)
#create table tab_info(db_id,tab_type,tab_obj_id,tab_name,col_sum)
#create table col_info(tab_obj_id,col_id,col_name,col_type,col_len,prec,scale,notnull_is,pkey_is,var_len_is,def_data)
#insert into tab_info values(1,1,1,1,'SYS_TABLES',7,1)
#insert into col_info values(0,2,'table_id',1,1,8,0,0,null,null,0,0,0,null)
# nullable_is,pkey_is,var_len_is 这些可以按位来存,一起存储在一个字节里
# 初始化表的信息,初始化多个表的,多个列. 双重循环
update tab_info set tab_obj_id=3825,index_id=10871,ts_no=3811 where tab_obj_id=3;
update col_info set tab_obj_id=3825 where tab_obj_id=3;

有 text的 直接行溢出

