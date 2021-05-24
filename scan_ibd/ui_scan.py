# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys, sqlite3, random, hashlib, os.path, logging, time
import os_win, innodb_scan, link_1, data_out


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.init()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)  # 设置边缘宽度
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")  # 数据源
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_2.setContentsMargins(0, 8, 0, 0)  # 设置边缘宽度
        self.groupBox = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)  # 磁盘选择框
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)  # open
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)  # 信息
        self.gridLayout_4.addWidget(self.textEdit, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_1)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 372, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)  # 起始偏移　lineEdit
        self.lineEdit.setText('0')  # 设置默认值  setPlaceholderText
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)  # 扫描步长下拉框
        self.comboBox_2.addItem("512")
        self.comboBox_2.addItem("1024")
        self.comboBox_2.addItem("4096")
        self.comboBox_2.addItem("8192")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_2)  # 页面大小
        self.comboBox_5.addItem("16384")
        self.comboBox_5.addItem("8192")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout_3.addWidget(self.comboBox_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName("结束偏移")
        self.lineEdit_2.setText('0')  # 设置默认值
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.addItem("全部空间")
        self.comboBox_3.addItem("自由空间")
        self.verticalLayout_5.addWidget(self.comboBox_3)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_2)  # 大小端选择框
        self.comboBox_6.addItem("小端")
        self.comboBox_6.addItem("大端")
        self.verticalLayout_5.addWidget(self.comboBox_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()  # 物理拼接
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setContentsMargins(2, 2, 2, 0)  # 设置边缘宽度
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)  # 物理碎片表
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_7.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)  # 进度条
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.progressBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.lable_1 = QtWidgets.QLabel(self.progressBar)
        self.lable_1.setFixedSize(QtCore.QSize(900, 20))
        self.gridLayout_7.addWidget(self.progressBar, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()  # 逻辑拼接
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)  # 设置边缘宽度
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_5.setTitle("")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_5)  # 开始拼接按钮
        self.pushButton_4.setGeometry(QtCore.QRect(245, 20, 75, 23))
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_5)  # 开始导出按钮
        self.pushButton_5.setGeometry(QtCore.QRect(445, 20, 75, 23))
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_4.setGeometry(QtCore.QRect(45, 20, 156, 22))
        self.comboBox_4.addItem("算法1")
        self.comboBox_4.addItem("算法2")
        self.comboBox_4.addItem("算法3")
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.tab_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.headerItem().setText(0, "1")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.splitter.setStretchFactor(1, 2)  # 设置显示比例
        self.gridLayout_5.addWidget(self.splitter, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.tab_4)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_5)
        self.splitter_2 = QtWidgets.QSplitter(self.tab_5)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(3)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.splitter_2)
        self.treeWidget_2.headerItem().setText(0, "1")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.splitter_2)
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.splitter_2.setStretchFactor(1, 2)  # 设置显示比例
        self.gridLayout_9.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(140, 125, 400, 180))
        self.color = QtGui.QColor(180, 180, 180)
        self.label_9.setStyleSheet(
            'QLabel{border:3px groove grey; border-radius:3px;border-style: outset;background-color:%s}' % self.color.name())  #
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.disk_open()  # 初始化磁盘选择框
        self.pushButton.clicked.connect(self.fileOpen)
        self.pushButton_2.clicked.connect(self.scan_start)  # 开始扫描
        self.pushButton_4.clicked.connect(self.logic_link)
        self.pushButton_5.clicked.connect(self.data_out)  # 导出数据

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MySQL 数据库碎片工具  V%s" % self.version))
        self.groupBox.setTitle(_translate("MainWindow", "数据源"))
        self.pushButton.setText(_translate("MainWindow", "open"))
        self.groupBox_2.setTitle(_translate("MainWindow", "扫描设置"))
        self.pushButton_2.setText(_translate("MainWindow", "开始扫描"))
        self.pushButton_3.setText(_translate("MainWindow", "停止扫描"))
        self.label.setText(_translate("MainWindow", "起始偏移"))
        self.label_3.setText(_translate("MainWindow", "扫描步长"))
        self.label_5.setText(_translate("MainWindow", "页面大小"))
        self.label_2.setText(_translate("MainWindow", "结束偏移"))
        self.label_4.setText(_translate("MainWindow", "扫描空间"))
        self.label_6.setText(_translate("MainWindow", "大小端"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "数据源"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "物理拼接"))
        self.pushButton_4.setText(_translate("MainWindow", "开始拼接"))
        self.pushButton_5.setText(_translate("MainWindow", "开始导出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "逻辑拼接"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "检测/解析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "数据展示"))
        abort = 'mysql innodb数据库碎片工具  V%s\n\n支持mysql 5.x，MariaDB的innodb\n此版本只能运行在64位Windows系统中\n' \
                '可扫描镜像文件和磁盘,扫描磁盘需以管理员运行.\n此程序注册单次有效,程序重启需重新获取注册码注册.\nI/O速度参考:50m/s=3G/min=180G/h=1T/5.7h' % self.version
        self.label_9.setText(_translate("MainWindow", "%s" % abort))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "关于"))

    def init(self):
        self.version = '1.5.0'
        self.f_name = ''
        self.reg = 1

    def fileOpen(self):
        fn, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open img...", None, "Img-Files (*.*);;All Files (*)")
        self.f_name = fn
        self.comboBox.setItemText(0, self.f_name)

    def disk_open(self):
        os_info = os_win.os_info()
        os_1 = os_info.sys_version()
        cpu_1, mem_1 = os_info.cpu_mem()
        self.textEdit.append('%s' % os_1 + cpu_1 + mem_1)
        self.disk_info = os_info.disk()
        self.disk_sum = len(self.disk_info)
        self.comboBox.addItem('')
        self.comboBox.addItem('------------------磁盘-------------------')
        for i in range(len(self.disk_info)):
            self.comboBox.addItem(
                self.disk_info[i].device_id + '[%5.1fG]' % (self.disk_info[i].disk_size / 1024.0 / 1024 / 1024))
        self.comboBox.addItem('------------------分区-------------------')
        for i in range(len(self.disk_info)):
            for ii in range(len(self.disk_info[i].partitions)):
                self.comboBox.addItem(self.disk_info[i].partitions[ii].partition_name)

    # 开始扫描和物理拼接
    def scan_start(self):
        if self.reg == 0:
            self.register()
            return
        self.f_name = self.comboBox.currentText()  # 改成 事件 触发
        if self.f_name[0:4] == '\\\\.\\':
            self.f_name = "\\\\.\\" + self.f_name[4:-8]
            for i in range(len(self.disk_info)):
                if self.f_name == self.disk_info[i].device_id:
                    size = self.disk_info[i].disk_size
        elif self.f_name == '':
            QtWidgets.QMessageBox.about(self, "error", "没有数据源，请先选择一个数据源...\t\t\n")
            return 0
        try:
            f = open(self.f_name, 'rb')
        except PermissionError as e:
            self.textEdit.append('%s,请以管理员权限重启此程序.' % e)
            return 0
        except FileNotFoundError as e:
            self.textEdit.append('%s' % e)
            return 0
        if self.f_name[0:4] == '\\\\.\\':
            f_size = size
        else:
            f_size = os.path.getsize(f.name)
        end_off = int(self.lineEdit_2.text())
        if end_off == 0:
            self.lineEdit_2.setText(str(f_size))
        endian_0 = {'大端': 1, '小端': 0}
        start_off = int(self.lineEdit.text())  # 起始偏移
        end_off = int(self.lineEdit_2.text())  # 结束偏移
        scan_size = int(self.comboBox_2.currentText())  # 扫描步长
        self.page_size = int(self.comboBox_5.currentText())  # 页面大小
        self.endian = endian_0[self.comboBox_6.currentText()]  # 大小端,其实没用

        self.textEdit.append('file: %s' % self.f_name)
        out_path = QtWidgets.QFileDialog.getExistingDirectory(self, "选择一个存放中间数据库的目录...", None)  # 选择文件夹对话框
        if out_path == '':
            return
        self.db_name = out_path + '/ibd_scan.db'
        self.textEdit.append('scan db: %s' % self.db_name)
        ret = QtWidgets.QMessageBox.question(self, "请确认", self.tr(" 是否开始扫描 ?\t\t\n"),
                                             QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel,
                                             QtWidgets.QMessageBox.Ok)
        if ret == QtWidgets.QMessageBox.Ok:
            self.textEdit.append('\n正在扫描，可能需要一段时间，请耐心等待...\n')
        elif ret == QtWidgets.QMessageBox.Cancel:
            self.textEdit.append('\n扫描取消 ...\n')
            return

        logging.basicConfig(level=logging.DEBUG, format='%(message)s', filename='%s_%s.log' % (
            self.db_name[:-3], time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))), filemode='w')
        logging.info('file: %s' % self.f_name)
        logging.info('scan_db: %s' % self.db_name)
        self.tabWidget.setCurrentIndex(1)  # 切换到下一个标签页

        ora_scan_1 = innodb_scan.Scan_1(self)  # 页面扫描 *****
        ora_scan_1.f_name, ora_scan_1.db_name, ora_scan_1.logging, ora_scan_1.start_off, ora_scan_1.end_off, ora_scan_1.endian, \
        ora_scan_1.page_size, ora_scan_1.scan_size = self.f_name, self.db_name, logging, start_off, end_off, self.endian, self.page_size, scan_size
        ora_scan_1.start()
        ora_scan_1.PUP.connect(self.progressBar.setValue)  # 传递参数
        ora_scan_1.LUP.connect(self.lable_1.setText)
        ora_scan_1.PUP.connect(self.aa_1)  # 判断scan 进程完成，进行下边的操作

        # self.textEdit.append('db name: %s'%file_infos[0].SID)
        # self.textEdit.append('db version: %s'%file_infos[0].version)
        # # self.textEdit.append('scan page sum:%d'%info.page_sum)
        # # self.textEdit.append('link1 sum:%d'%info.link1_sum)
        # self.textEdit.append('\n扫描完成...\n')
        # self.tabWidget.setCurrentIndex(1)           # 切换到下一个标签页
        # self.show_tab1(db_name)

    def aa_1(self, press):
        if press == 100:
            time.sleep(2)
            link_1.link_1(self.db_name)  # 物理拼接
            self.textEdit.append('\n扫描完成...\n')
        #   self.show_tab1(self.db_name)                            # 显示碎片列表
        #         link_wl = ora_link1.Link_wl(self)     # 页面扫描 *****
        #         link_wl.f_name,link_wl.db_name,link_wl.endian,link_wl.page_size,link_wl.logging = self.f_name,self.db_name,self.endian,self.page_size,logging
        #         link_wl.start()
        #         link_wl.PUP.connect(self.progressBar.setValue)   # 传递参数
        #         link_wl.LUP.connect(self.lable_1.setText)
        #         link_wl.PUP.connect(self.aa_2)
        # def aa_2(self,press):
        #     if press == -2:
        #         self.textEdit.append('\n扫描完成...\n')
        #         self.show_tab1(self.db_name)                            # 显示碎片列表

    # 物理碎片列表
    def show_tab1(self, db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("select * from link_2 ;")
        values = cursor.fetchall()  # 取出数据
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(values))
        header1 = ['g1_id', 'page_sum', 'offset_1', 'offset_2', 'page_no_1', 'page_no_2', 'file_no_1']
        self.tableWidget.setHorizontalHeaderLabels(header1)
        self.tableWidget.setColumnWidth(0, 50)  # 设置固定列宽
        self.tableWidget.setSortingEnabled(1)  # 点击表头 可以排序
        for i in range(len(values)):
            self.tableWidget.setRowHeight(i, 22)
            self.tableWidget.setItem(i, 0, Qt.QTableWidgetItem("%s" % values[i][0]))
            self.tableWidget.setItem(i, 1, Qt.QTableWidgetItem("%s" % values[i][1]))
            self.tableWidget.setItem(i, 2, Qt.QTableWidgetItem("%s" % values[i][2]))
            self.tableWidget.setItem(i, 3, Qt.QTableWidgetItem("%s" % values[i][3]))
            self.tableWidget.setItem(i, 4, Qt.QTableWidgetItem("%s" % values[i][4]))
            self.tableWidget.setItem(i, 5, Qt.QTableWidgetItem("%s" % values[i][5]))
            self.tableWidget.setItem(i, 6, Qt.QTableWidgetItem("%s" % values[i][6]))

        self.textEdit.append('link_wl sum:%d' % len(values))
        self.textEdit.append('物理拼接完成...\n')

    def logic_link(self):  # 逻辑拼接
        self.textEdit.append('逻辑拼接开始')

    def data_out(self):
        # 弹出导出配置界面
        self.out_widget = QtWidgets.QWidget()
        self.out_widget.setGeometry(QtCore.QRect(385, 100, 550, 340))
        self.out_widget.setWindowTitle('导出数据')
        self.label_10 = QtWidgets.QLabel(self.out_widget)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 70, 23))
        self.label_10.setText('file_in')
        self.label_11 = QtWidgets.QLabel(self.out_widget)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 70, 23))
        self.label_11.setText('file_out')
        self.label_12 = QtWidgets.QLabel(self.out_widget)
        self.label_12.setGeometry(QtCore.QRect(10, 100, 70, 23))
        self.label_12.setText('db_name')
        self.label_13 = QtWidgets.QLabel(self.out_widget)
        self.label_13.setGeometry(QtCore.QRect(10, 140, 520, 23))
        self.label_13.setText('out_sql：select offset_1,offset_2,page_no_1 from link_1 where ')
        self.label_14 = QtWidgets.QLabel(self.out_widget)
        self.label_14.setGeometry(QtCore.QRect(10, 220, 400, 23))

        self.comboBox_8 = QtWidgets.QComboBox(self.out_widget)  # 页面大小
        self.comboBox_8.setGeometry(QtCore.QRect(440, 170, 100, 23))
        self.comboBox_8.addItem("按查询位置")
        self.comboBox_8.addItem("按页号位置")

        self.lineEdit_10 = QtWidgets.QLineEdit(self.out_widget)
        self.lineEdit_10.setGeometry(QtCore.QRect(80, 20, 400, 23))
        self.lineEdit_11 = QtWidgets.QLineEdit(self.out_widget)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 60, 400, 23))
        self.lineEdit_12 = QtWidgets.QLineEdit(self.out_widget)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 100, 400, 23))
        self.lineEdit_13 = QtWidgets.QLineEdit(self.out_widget)  # 导出sql
        self.lineEdit_13.setGeometry(QtCore.QRect(80, 170, 360, 23))

        self.pushButton_10 = QtWidgets.QPushButton(self.out_widget)  #
        self.pushButton_10.setGeometry(QtCore.QRect(500, 20, 40, 23))
        self.pushButton_10.setText('...')
        self.pushButton_11 = QtWidgets.QPushButton(self.out_widget)  #
        self.pushButton_11.setGeometry(QtCore.QRect(500, 60, 40, 23))
        self.pushButton_11.setText('...')
        self.pushButton_12 = QtWidgets.QPushButton(self.out_widget)  #
        self.pushButton_12.setGeometry(QtCore.QRect(500, 100, 40, 23))
        self.pushButton_12.setText('...')

        self.pushButton_14 = QtWidgets.QPushButton(self.out_widget)  # 设置完成，开始导出
        self.pushButton_14.setGeometry(QtCore.QRect(80, 260, 150, 23))
        self.pushButton_14.setText('设置完成，开始导出')
        self.pushButton_15 = QtWidgets.QPushButton(self.out_widget)  # 取消导出
        self.pushButton_15.setGeometry(QtCore.QRect(350, 260, 100, 23))
        self.pushButton_15.setText('关闭')
        self.pushButton_10.clicked.connect(self.fileOpen1)
        self.pushButton_11.clicked.connect(self.fileOpen2)
        self.pushButton_12.clicked.connect(self.fileOpen3)
        self.pushButton_14.clicked.connect(self.data_out1)
        self.pushButton_15.clicked.connect(self.data_out2)

        self.out_widget.show()

    def fileOpen1(self, ):
        fn, _ = QtWidgets.QFileDialog.getOpenFileName(self.out_widget, "Open ", None, "All Files (*)")
        self.lineEdit_10.setText(fn)

    def fileOpen2(self, ):
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(self.out_widget, "Save File ... ", None, "All Files (*)")
        self.lineEdit_11.setText(fn)

    def fileOpen3(self, ):
        fn, _ = QtWidgets.QFileDialog.getOpenFileName(self.out_widget, "Open ", None, "All Files (*)")
        self.lineEdit_12.setText(fn)

    def data_out1(self):
        file_in = self.lineEdit_10.text()
        file_out = self.lineEdit_11.text()
        db_name = self.lineEdit_12.text()
        out_sql = 'select offset_1,offset_2,page_no_1 from link_1 where ' + self.lineEdit_13.text()
        out_type = self.comboBox_8.currentText()
        print('file_in:%s' % file_in)
        print('out_sql:%s' % out_sql)
        if file_in != '' and file_out != '' and db_name != '' and out_sql != '':
            self.label_14.setText('正在导出...')
            if out_type == '按查询位置':  # 导出为单个文件
                out = data_out.data_out1(file_in, file_out, db_name, out_sql)  # 开始导出
            elif out_type == '按页号位置':  # 按文件号页号位置导出为多个文件
                out = data_out.data_out2(file_in, file_out, db_name, out_sql)  # 开始导出
            if out == 0:
                self.label_14.setText('导出完成...')
                # self.out_widget.close()
        else:
            QtWidgets.QMessageBox.about(self.out_widget, "提示", "参数不全,请输入完整参数 ...  \t\n")

    def data_out2(self):
        self.out_widget.close()

    def register(self):
        # 弹出导出配置界面
        self.reg_widget = QtWidgets.QWidget()
        self.reg_widget.setGeometry(QtCore.QRect(385, 100, 500, 180))
        self.reg_widget.setWindowTitle('注册')

        self.label_20 = QtWidgets.QLabel(self.reg_widget)
        self.label_20.setGeometry(QtCore.QRect(10, 20, 50, 23))
        self.label_20.setText('原始码')
        self.label_21 = QtWidgets.QLabel(self.reg_widget)
        self.label_21.setGeometry(QtCore.QRect(10, 60, 50, 23))
        self.label_21.setText('注册码')
        self.lineEdit_20 = QtWidgets.QLineEdit(self.reg_widget)
        self.lineEdit_20.setGeometry(QtCore.QRect(80, 20, 400, 23))
        num1 = random.randint(1000000000, 9999999999)
        self.lineEdit_20.setText(str(num1))
        self.lineEdit_20.setReadOnly(1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.reg_widget)
        self.lineEdit_21.setGeometry(QtCore.QRect(80, 60, 400, 23))
        self.label_22 = QtWidgets.QLabel(self.reg_widget)
        self.label_22.setGeometry(QtCore.QRect(10, 90, 500, 23))
        self.label_22.setText('* 发送原始码,获取注册码进行注册. 注册单次有效,程序重启需重新获取注册码注册！')
        self.pushButton_20 = QtWidgets.QPushButton(self.reg_widget)
        self.pushButton_20.setGeometry(QtCore.QRect(80, 120, 160, 23))
        self.pushButton_20.setText('注册')
        self.pushButton_21 = QtWidgets.QPushButton(self.reg_widget)
        self.pushButton_21.setGeometry(QtCore.QRect(300, 120, 100, 23))
        self.pushButton_21.setText('取消')
        self.reg_widget.show()
        self.pushButton_20.clicked.connect(self.register1)  # 怎么获取返回值
        self.pushButton_21.clicked.connect(self.register2)

    def register1(self):
        num1 = self.lineEdit_20.text()  # 随机码
        num2 = self.lineEdit_21.text()  # 验证码
        md5 = hashlib.md5()
        reg = str(105946)
        md5.update(reg.encode())
        reg0 = md5.hexdigest()
        md5.update(num1.encode())
        reg1 = md5.hexdigest()
        sha1 = hashlib.sha1()
        sha1.update(str(reg0 + reg1).encode())
        reg2 = sha1.hexdigest()
        if num2 == reg2:
            self.reg = 1
            QtWidgets.QMessageBox.about(self.reg_widget, "注册", "注册成功  \t\t\n")
            self.reg_widget.close()
        else:
            QtWidgets.QMessageBox.about(self.reg_widget, "注册", "注册码错误，注册失败  \t\n")

    def register2(self):
        self.reg_widget.close()


class myui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myui, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = myui()
    ui.show()
    sys.exit(app.exec_())
