# -*- coding: utf-8 -*-
# 解析innodb 记录 (包括compact, redundant记录)
import struct
import table_struct, data_type

s = struct.unpack


# 初始化页面信息
def page_init(in_data):  # 初始化页面信息
    page_size = 16384
    page1 = table_struct.st_page()
    data1 = s(">4IQHQI", in_data[0:38])
    page1.check1 = data1[0]
    page1.page_no = data1[1]
    page1.page_prev = data1[2]
    page1.page_next = data1[3]
    page1.page_type = data1[5]
    page1.tablespace_id = data1[7]

    if page1.page_type == 17855:  # 数据页
        data2 = s(">9HQHQ", in_data[38:74])
        page1.slot_sum = data2[0]
        page1.rec_sum0 = data2[2]
        if page1.rec_sum0 >= 32768:
            page1.rec_sum0 -= 32768  # ？？？ 最高一位是new-style compact page format标记
        page1.rec_sum1 = data2[8]
        page1.page_level = data2[10]
        page1.page_index_id = data2[11]

    slot_len = page1.slot_sum * 2
    for i in range(0, page1.slot_sum):
        slot1 = s(">H", in_data[page_size - i * 2 - 2 - 8:page_size - i * 2 - 8])  # slot_off_list
        page1.page_slot.append(slot1[0])  # 一般每个页面里slot数量在 1-100.
    return page1


# 解析 compact 记录,普通表 记录.  需要加入 索引结点的解析
def rec_compact(f, in_data, table):  # 解析 compact 记录  in_data(输入页面数据),table(表结构)
    page1 = page_init(in_data)
    off_set = page1.page_slot[0]
    if page1.page_level != 0:  # 聚集索引的 索引结点，记录结构不同，是索引记录
        page_1 = page1
        in_data1 = in_data
        print('talbe:%s,level:%s,page_no:%d,rec_sum:%d' % (
            table.tab_name, page_1.page_level, page_1.page_no, page_1.rec_sum1))
        for i in range(0, page_1.rec_sum1 + 2):  # 解记录
            record1 = table_struct.st_rec_compact()
            try:
                header1 = s(">B2h", in_data1[off_set - 5:off_set])  # 记录头
            except struct.error:
                off_set = record1.rec_h2
                continue
            record1.rec_h0 = header1[0]
            record1.rec_h1 = header1[1]
            record1.rec_h2 = header1[2]
            record1.rec_off = off_set
            del_flag = (record1.rec_h0 >> 1) % 2  # 删除标志

            if i == 0:
                off_set = off_set + record1.rec_h2  # 下一条记录的起始偏移
                continue
            if i == page1.rec_sum1 + 1:
                continue

            col_off = 0;
            var_list = 0  # 变长列长度列表的长度
            # 解析 索引记录的 各列数据, 行溢出略,索引记录里没有溢出  ======================================
            for ii3 in range(len(table.index_col)):
                len1 = table.index_col[ii3].col_len
                if table.index_col[ii3].varlen_is == 0:  # 是定长
                    AA = 0
                elif table.index_col[ii3].varlen_is == 1:  # 是可变长
                    var_list = var_list + 1
                    var_len1 = s("B", in_data1[off_set - 5 - var_list:off_set - 5 - var_list + 1])
                    len1 = var_len1[0]
                    if var_len1[0] >= 128:
                        var_list = var_list + 1
                        var_len1 = s("BB", in_data1[off_set - 5 - var_list:off_set - 5 - var_list + 2])
                        len1 = (var_len1[1] - 128) * 256 + var_len1[0]
                col_data1 = in_data1[off_set + col_off:off_set + col_off + len1]
                col_off += len1
                try:
                    col_data2 = data_type.data_type(col_data1, table.index_col[ii3])  # 列数据解析,
                except UnboundLocalError:
                    print('UnboundLocalError:pg_no:%d,crd_no:%d,off:%d,col_no:%d,len:%d ' % (
                        page1.page_no, i, off_set, ii3, len1))
                    col_data2 = ''
                record1.col_data2.append(col_data2)

            off_set = off_set + record1.rec_h2  # 下一条记录的起始偏移
            page_no_1 = record1.col_data2[-1]
            f.seek(page_no_1 * 16384)
            in_data = f.read(16384)
            page2 = rec_compact(f, in_data, table)  # 解析level 0 的页面
            #    print(table.tab_name,record1.col_data2[0],record1.col_data2[1],len(page2.record))
            for record in page2.record:
                page_1.record.append(record)
        return page_1

    elif page1.page_level == 0:  # 叶子节点，数据页
        for i in range(0, page1.rec_sum1 + 2):  # 页中的所有记录
            record1 = table_struct.st_rec_compact()
            var_list = 0  # 变长列长度列表的长度
            try:
                header1 = s(">B2h", in_data[off_set - 5:off_set])  # 记录头
            except struct.error:
                continue
            record1.rec_h0 = header1[0]
            record1.rec_h1 = header1[1]
            record1.rec_h2 = header1[2]
            record1.rec_off = off_set
            if i == 0:
                off_set = off_set + record1.rec_h2  # 下一条记录的起始偏移
                continue
            if i == page1.rec_sum1 + 1:
                continue
            null_map_len = (table.nullable_sum + 7) // 8  # null 位图的长度
            null_map2 = 0
            frm = str(null_map_len) + 'B'
            null_map = s(frm,
                         in_data[off_set - null_map_len - 5:off_set - 5])  # null位图  +++++++++++++++++++++++++++++++++
            for i1 in range(null_map_len):
                null_map2 += null_map[i1] * (2 ** ((null_map_len - i1 - 1) * 8))
            record1.null_map = null_map2  # null位图  ++++++++++++++++++++++++++++++++
            col_off = 0;
            nullable_id = 0
            # 解析记录的各列数据, 行溢出也可解析 ======================================
            for ii3 in range(0, len(table.col_1)):
                yichu_is = 0  # 溢出标志
                if page1.page_no == 0 and i == 1 and ii3 == 10:  # 测试 定位用。 页号，记录号，列号
                    dd = 0
                len1 = table.col_1[ii3].col_len
                col_is_null = 0  # 此列是否为 null
                if table.col_1[ii3].notnull_is == 0:  # 此列可为 null
                    a1 = record1.null_map >> nullable_id
                    col_is_null = a1 % 2
                    nullable_id = nullable_id + 1
                    if col_is_null == 0:  # 列不为空
                        if table.col_1[ii3].varlen_is == 0:  # 是定长
                            AA = 0
                        elif table.col_1[ii3].varlen_is == 1:  # 是可变长
                            var_list = var_list + 1
                            var_len1 = s("B", in_data[
                                              off_set - null_map_len - 5 - var_list:off_set - null_map_len - 5 - var_list + 1])
                            len1 = var_len1[0]
                            if var_len1[0] >= 128:
                                var_list = var_list + 1
                                var_len1 = s("BB", in_data[
                                                   off_set - null_map_len - 5 - var_list:off_set - null_map_len - 5 - var_list + 2])
                                len1 = (var_len1[1] - 128) * 256 + var_len1[0]
                                if len1 >= 16384:  # 行溢出
                                    yichu_is = 1
                                    len1 = len1 - 16384
                                    col_data_1 = in_data[off_set + col_off:off_set + col_off + len1 - 20]
                                    try:
                                        yichu_1 = s(">40I",
                                                    in_data[off_set + col_off + len1 - 16:off_set + col_off + len1])
                                    except struct.error:
                                        yichu_is = 0
                                        len1 = len1 - 16384
                                        col_off += len1
                                        col_data2 = ''
                                        record1.col_data2.append(col_data2)
                                        continue
                                    next_page = yichu_1[0]
                                    off_1 = yichu_1[1]
                                    next_len = yichu_1[3]
                                    for i in range(10):
                                        f.seek(next_page * 16384)
                                        in_data1 = f.read(16384)
                                        next_1 = s('>2I', in_data1[38:38 + 8])
                                        next_len1 = next_1[0];
                                        next_page = next_1[1]
                                        col_data_1 += in_data1[38 + 8:38 + 8 + next_len1]
                                        if next_page == 4294967295:
                                            break
                        if yichu_is == 1:
                            col_data1 = col_data_1
                        else:
                            col_data1 = in_data[off_set + col_off:off_set + col_off + len1]
                        col_off += len1
                        try:
                            col_data2 = data_type.data_type(col_data1, table.col_1[ii3])  # 列数据解析,
                        except struct.error:
                            print('struct.error:pg_no:%d,crd_no:%d,off:%d,col_no:%d,len:%d ' % (
                                page1.page_no, i, off_set, ii3, len1))
                            col_data2 = ''

                        # if table.col_1[ii3].col_name == 'picture':          # 取照片
                        #     f_1 = open(r'.\picture\%s.jpg'%(record1.col_data2[3]),'wb')
                        #     f_1.write(col_data1)
                        #     f_1.close()

                    elif col_is_null == 1:  # 列为空
                        if table.col_1[ii3].varlen_is == 0:  # 是定长
                            len1 = 0  # 为空的定长列，不占位，长度为0
                        elif table.col_1[ii3].varlen_is == 1:  # 是可变长
                            var_list = var_list + 0
                            len1 = 0
                        col_data1 = 'NULL'
                        col_data2 = 'NULL'  # 列数据解析
                elif table.col_1[ii3].notnull_is == 1:  # 此列不可为 null
                    if table.col_1[ii3].varlen_is == 0:  # 是定长
                        AA = 0
                    elif table.col_1[ii3].varlen_is == 1:  # 是可变长
                        var_list = var_list + 1
                        var_len1 = s("B", in_data[
                                          off_set - null_map_len - 5 - var_list:off_set - null_map_len - 5 - var_list + 1])
                        len1 = var_len1[0]
                        if var_len1[0] >= 128:
                            var_list = var_list + 1
                            var_len1 = s("BB", in_data[
                                               off_set - null_map_len - 5 - var_list:off_set - null_map_len - 5 - var_list + 2])
                            len1 = (var_len1[1] - 128) * 256 + var_len1[0]
                            if len1 >= 16384:  # 行溢出
                                yichu_is = 1
                                len1 = len1 - 16384
                                col_data_1 = in_data[off_set + col_off:off_set + col_off + len1 - 20]
                                try:
                                    yichu_1 = s(">40I", in_data[off_set + col_off + len1 - 16:off_set + col_off + len1])
                                except struct.error:
                                    yichu_is = 0
                                    len1 = len1 - 16384
                                    col_off += len1
                                    col_data2 = ''
                                    record1.col_data2.append(col_data2)
                                    continue
                                next_page = yichu_1[0]
                                off_1 = yichu_1[1]
                                next_len = yichu_1[3]
                                for i in range(10):  # 多个溢出页
                                    f.seek(next_page * 16384)
                                    in_data1 = f.read(16384)
                                    next_1 = s('>2I', in_data1[38:38 + 8])
                                    next_len1 = next_1[0];
                                    next_page = next_1[1]
                                    col_data_1 += in_data1[38 + 8:38 + 8 + next_len1]
                                    if next_page == 4294967295:
                                        break
                    if yichu_is == 1:
                        col_data1 = col_data_1
                    else:
                        col_data1 = in_data[off_set + col_off:off_set + col_off + len1]
                    col_off += len1
                    try:
                        col_data2 = data_type.data_type(col_data1, table.col_1[ii3])  # 列数据解析,
                    except (UnboundLocalError, struct.error) as e:
                        print('UnboundLocalError:pg_no:%d,crd_no:%d,off:%d,col_no:%d,len:%d ' % (
                            page1.page_no, i, off_set, ii3, len1))
                        col_data2 = ''

                record1.col_data2.append(col_data2)
            for i1 in range(table.col_sum):  # 调整列顺序
                for i2 in range(len(table.col_1)):
                    if table.col[i1].col_id == table.col_1[i2].col_id:
                        try:
                            record1.col_data1.append(
                                record1.col_data2[i2])  # col_data1 是最终解析好的，可直接输出的，跟表结构相同。col_data2是记录存储中的列顺序。
                        except IndexError:
                            #     print('溢出，page_no:%s,off_set:%s'%(page1.page_no,off_set))
                            continue
                        break
            page1.record.append(record1)  # 把记录放到 页面的记录容器里,会很多
            off_set = off_set + record1.rec_h2  # 下一条记录的起始偏移
        return page1


# 解析 redundant 记录, 系统表 记录，   需要调整下，参考 rec_compact
def rec_redundant(f, in_data, table):  # 解析 redundant 记录,解析系统表,插入sqlite
    page1 = page_init(in_data)
    if len(page1.page_slot) == 0:
        return page1
    off_set = page1.page_slot[0]
    if page1.page_level != 0:  # 聚集索引的 索引结点，记录结构不同
        page_1 = page1
        in_data1 = in_data
        for i in range(0, page_1.rec_sum1 + 2):  # 解记录
            record1 = table_struct.st_rec_compact()
            try:
                header1 = s(">4Bh", in_data1[off_set - 6:off_set])  # 记录头
            except struct.error:
                off_set = record1.rec_h2
                continue
            record1.rec_h0 = header1[0]
            record1.rec_h1 = header1[1]
            record1.rec_h3 = header1[2]
            record1.rec_h4 = header1[3]
            record1.rec_h2 = header1[4]
            col_sum_1 = record1.rec_h4 >> 1
            del_flag = (record1.rec_h0 >> 1) % 2  # 删除标志
            record1.rec_off = off_set
            if i == 0:
                off_set = record1.rec_h2  # 下一条记录的起始偏移
                continue
            if i == page_1.rec_sum1 + 1:
                continue
            var_list = 0  # 列长度列表的长度
            col_off = 0
            off_set_now = off_set
            # 解析 索引记录的 各列数据, 行溢出略,（此种记录含义出极少）  ======================================
            for ii3 in range(col_sum_1):
                var_list = var_list + 1
                var_len1 = s("B", in_data1[off_set - 6 - var_list:off_set - 6 - var_list + 1])
                if var_len1[0] >= 128:
                    var_list = var_list + 2
                    var_len1 = s("B",
                                 in_data1[off_set - 6 - var_list + 1:off_set - 6 - var_list + 2])  # ================
                len1 = var_len1[0] - col_off
                col_off = var_len1[0]
                col_data1 = in_data1[off_set + var_len1[0] - len1:off_set + var_len1[0]]  # 二进制列数据
                col_data2 = 0

                if ii3 == col_sum_1 - 1:  # 解析索引最后一列，页面指针
                    col_data3 = s('>I', col_data1)  # 列数据解析,
                    col_data2 = col_data3[0]
                record1.col_data2.append(col_data2)
            off_set = record1.rec_h2  # 下一条记录的起始偏移
            page_no_1 = record1.col_data2[col_sum_1 - 1]
            table_name = record1.col_data2[0]
            if table.tab_obj_id == 1:
                print('i:%d,off_set_now:%d,off_set_next:%d,table_name:%s,page_no:%d' % (
                    i, off_set_now, off_set, table_name, page_no_1))
            f.seek(page_no_1 * 16384)
            in_data = f.read(16384)
            page2 = rec_redundant(f, in_data, table)  # 解析level 0 的页面
            for record in page2.record:
                page_1.record.append(record)
        return page_1
    elif page1.page_level == 0:  # 叶子节点，数据页
        for i in range(0, page1.rec_sum1 + 2):  # 解记录
            record1 = table_struct.st_rec_compact()
            header1 = s(">4Bh", in_data[off_set - 6:off_set])  # 记录头
            record1.rec_h0 = header1[0]
            record1.rec_h1 = header1[1]
            record1.rec_h3 = header1[2]
            record1.rec_h4 = header1[3]
            record1.rec_h2 = header1[4]
            col_sum_1 = record1.rec_h4 >> 1 - 1
            record1.rec_off = off_set
            if i == 0:
                off_set = record1.rec_h2  # 下一条记录的起始偏移
                continue
            if i == page1.rec_sum1 - 1:
                continue
            var_list = 0  # 列长度列表的长度
            col_off = 0
            off_set_now = off_set
            # 解析记录的各列数据, 行溢出略,（此种记录含义出极少）  ======================================
            for ii3 in range(0, len(table.col_1)):
                #    len1 = table.col_1[ii3].col_len
                var_list = var_list + 1
                var_len1 = s("B", in_data[off_set - 6 - var_list:off_set - 6 - var_list + 1])
                if var_len1[0] >= 128:
                    var_list = var_list + 2
                    var_len1 = s("B",
                                 in_data[off_set - 6 - var_list + 1:off_set - 6 - var_list + 2])  # ================
                len1 = var_len1[0] - col_off
                col_off = var_len1[0]
                col_data1 = in_data[off_set + var_len1[0] - len1:off_set + var_len1[0]]  # 二进制列数据
                col_data2 = data_type.data_type(col_data1, table.col_1[ii3])  # 列数据解析,
                record1.col_data2.append(col_data2)
            for i1 in range(table.col_sum):  # 调整列顺序
                for i2 in range(len(table.col_1)):
                    if table.col[i1].col_id == table.col_1[i2].col_id:
                        try:
                            record1.col_data1.append(
                                record1.col_data2[i2])  # col_data1 是最终解析好的，可直接输出的，跟表结构相同。col_data2是记录存储中的列顺序。
                        except IndexError:
                            print('溢出，page_no:%s,off_set:%s' % (page1.page_no, off_set))
                            continue
                        break
            page1.record.append(record1)  # 把记录放到 页面的记录容器里,会很多. 可以插入到tab_info,col_info表中
            off_set = record1.rec_h2  # 下一条记录的起始偏移
            if page1.page_no == 868382:
                print('i:%d,off_set_now:%d,off_set_next:%d,table_name:%s,page_no:%d' % (
                    i, off_set_now, off_set, '', page1.page_no))
        return page1
