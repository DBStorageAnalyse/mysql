# -*- coding: utf-8 -*-
# 数据类型解析
import struct,time
s = struct.unpack   # B H I

encoding = "gbk" # utf-8，gbk

def data_type(data,col_1):
    # int，bigint,smallint,mediumint ...
    if col_1.col_type in ('tinyint','smallint','mediumint','int','bigint'):
        if col_1.col_type == 'tinyint' :
            a = s(">B",data)
            b = 128
        elif col_1.col_type == 'smallint' :
            a = s(">H",data)
            b = 32768
        elif col_1.col_type == 'mediumint' :   # 5.1 的 有符号和无符号， 有待测试
            a0 = s(">HB",data)
            s0 = (a0[0]-32768)*256 + a0[1]
            # a0 = s(">BH", data)
            # s0 = a0[0] + a0[1]*65536
            a = [s0,]
            b = 0  # 8388608
        elif col_1.col_type == 'int' :
            a = s(">I",data)
            b = 2147483648
        elif col_1.col_type == 'bigint' :
            a = s(">Q",data)
            b = 9223372036854775808
        data_out = a[0]-b
        if col_1.col_unsign == 1:
            data_out = a[0]
        return data_out

    # datetime, date, time, year, timestamp
    elif col_1.col_type == 'datetime' and col_1.col_len == 8 :   # datatime, 5.6.4版本以前的
        a = s(">Q",data)
        data = a[0] - 9223372036854775808
        data = str(data)
        data_out = '%s-%s-%s %s:%s:%s'%(data[0:4],data[4:6],data[6:8],data[8:10],data[10:12],data[12:14])
        return data_out
    elif col_1.col_type == 'datetime' and col_1.col_len == 5 :   # 5.6.4 版本及以后的datetime
            a0 = s(">BI",data[0:5])
            ss = a0[1]%64
            mm = (a0[1]>>6)%64
            hh = (a0[1]>>12)%32
            dd = (a0[1]>>17)%32
            s0 = int(a0[1]>>22) + (a0[0]-128)*1024
            yy = s0//13     # 年
            mo = s0%13      # 月
            datetime = '%d-%d-%d %d:%d:%d'%(yy,mo,dd,hh,mm,ss)
            return datetime
    elif col_1.col_type == 'time' :    # time, 5.6.4 以前的存储
        a = [128,0]
        if len(data) == 3 :
            a = s(">BH",data)
        data = str((a[0]-128)*65536 + a[1])
        if len(data) < 6:
            data = '0'*(6-len(data))+data
        data_out = '%s:%s:%s'%(data[0:2],data[2:4],data[4:6])
        return data_out

    elif col_1.col_type == 'date' :    # date,所有版本都是
        try:
            a0 = s(">BH",data[0:3])
        except struct.error:
            yy=0;mo=0;dd=0
        s0 = a0[1] + (a0[0]-128)*65536
        dd = s0%32
        mo = (s0>>5)%16
        yy = int(s0>>9)
        date = '%d-%d-%d'%(yy,mo,dd)
        return date
    elif col_1.col_type == 'timestamp' :    # timestamp,所有版本都是
        a = [0]
        if len(data) == 4 :
            a = s(">I",data)
        if a[0] > 0:   # 时区 46800= 13*3600
            data = a[0]-0
            data_out = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(data))
        else:
            data_out = '0000-00-00 00:00:00'
        return data_out
    elif col_1.col_type == 'year' :    # year,所有版本都是
        a = s("B",data)
        data = a[0] + 1900
        return data

    # 字符 char, varchar, text,  ...
    elif col_1.col_type in('varchar','char','text') :
        try:
            data_out = str(data,encoding=encoding).strip()   # utf-8，gbk
        except UnicodeDecodeError as e:
            data_out = ''
        return data_out
    elif col_1.col_type == 'blob' :    # blob,  此处没处理。
        data_out = 'blob'
        return data_out

    # decimal,
    elif col_1.col_type == 'decimal' :  # decimal(m,n)
        data_out = 0
        if col_1.col_len == 5 :
            a = s(">IB",data)
            b = 2147483648
            if a[0] >= b :
                data_out = a[0]-b
            else:
                data_out = 0-a[0]
            data_out = '%d.%d'%(data_out,a[1])
        elif col_1.col_len == 3 :
            a = s(">HB",data)
            b = 32768
            if a[0] >= b :
                data_out = a[0]-b
            else:
                data_out = 0-a[0]
            data_out = '%d.%d'%(a[1],data_out)
        return data_out
    # double(m,n)
    elif col_1.col_type == 'double' :
        if len(data) == 8 :
            a = s("<d",data)
            data = a[0]
        return data
    # float(m,n)
    elif col_1.col_type == 'float' :
        if col_1.col_len == 4 :
            a = s("<f",data)
            data = a[0]
        return data
    # bit
    elif col_1.col_type == 'bit' :
        if col_1.col_len == 1 :
            a = s("B",data)
            data = a[0]
        return data

    else:
        return data

