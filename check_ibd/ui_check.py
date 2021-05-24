# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys,struct,random,hashlib
import chk_file

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.init()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.setMovable(1)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.color=QtGui.QColor(140, 140, 140)  #(190, 200, 200)
        self.groupBox.setStyleSheet('QGroupBox{border: 2px groove grey; border-radius:5px;border-style: outset;background-color:%s}'%self.color.name()) #利用样式
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 30, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setDisabled(1)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 30, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)     # file table
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_2.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressBar.setProperty("value",0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 2, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.tab_2)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName("splitter")
        self.tableWidget1 = QtWidgets.QTableWidget(self.splitter)   # 标签2的 表1
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(0)
        self.tableWidget1.setRowCount(0)
        self.tableWidget2 = QtWidgets.QTableWidget(self.splitter)  # 标签2的 表2
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(0)
        self.tableWidget2.setRowCount(0)
     #   self.splitter.setStretchFactor(1.7,2)  # 设置显示比例
        self.gridLayout_3.addWidget(self.splitter, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()        # HEX 标签
        self.tab_3.setObjectName("tab_3")
        self.text_1 = QtWidgets.QTextEdit(self.tab_3)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.addWidget(self.text_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label = QtWidgets.QLabel(self.tab_5)
        self.label.setGeometry(QtCore.QRect(50, 70, 86, 116))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        self.label_2.setGeometry(QtCore.QRect(200, 160, 300, 130))
        self.label_2.setObjectName("label_2")
        self.color=QtGui.QColor(140, 140, 140)  #(190, 200, 200)
        self.label_2.setStyleSheet('QLabel{border:2px groove grey; border-radius:5px;border-style: outset;background-color:%s}'%self.color.name()) #
        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.pushButton.clicked.connect(self.fileOpen)  # open 窗口
        self.pushButton_2.clicked.connect(self.fileDel)  # 移除文件
        self.pushButton_3.clicked.connect(self.allDel)   # 清空列表
        self.pushButton_4.clicked.connect(self.file_check)  # 开始检测
        self.tableWidget1.itemClicked.connect(self.file_Clicked)   # table1 点击
        self.tableWidget2.itemClicked.connect(self.err_Clicked)   # table2 点击

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)       # 初始显示的标签索引
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MySQL 文件检测工具  V%s"%self.veresion))
        self.pushButton.setText(_translate("MainWindow", "添加文件"))
        self.pushButton_2.setText(_translate("MainWindow", "移出文件"))
        self.pushButton_3.setText(_translate("MainWindow", "清空列表"))
        self.pushButton_4.setText(_translate("MainWindow", "开始检测"))
        self.pushButton_5.setText(_translate("MainWindow", "停止检测"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "选择文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "检测文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "HEX"))
        self.label.setText(_translate("MainWindow", ""))
        about = "MySQL Check V%s\n\n\n支持检测ibdata1,*.ibd文件\n支持各版本的mysql innodb文件\nchk_err:特征值/页尾/异或/RDBA(1:正常,0:不正常)"%self.veresion
        self.label_2.setText(_translate("MainWindow", about))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "高级检测"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "关于"))

    def fileOpen(self):
        fn, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Open Files...", None,"All Files (*)")
        for f_name in fn :
            file_info1 = chk_file.f_info(f_name)
            self.file_infos.append(file_info1)
        self.file_tab()
        self.pushButton_4.setDisabled(0)

    def fileDel(self):
        aa1 = self.tableWidget.currentRow()
        if len(self.file_infos) == 0:
            return
        del self.file_infos[aa1]
        self.file_tab()

    def allDel(self):
        self.file_infos = []
        self.file_tab()
        self.pushButton_4.setDisabled(1)

    def init(self):
        self.veresion = '1.2.0'     # 界面显示的软件版本号
        self.file_infos = []
        self.reg = 1

    # 显示文件列表
    def file_tab(self):
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setAlternatingRowColors(True)  # 隔行变色
        self.tableWidget.setRowCount(len(self.file_infos))
        header = ['file_path','file#','type','f_name','f_size(M)','page_sum','gp#','version']
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setColumnWidth(0,200);self.tableWidget.setColumnWidth(1,60);self.tableWidget.setColumnWidth(2,40);
        self.tableWidget.setColumnWidth(3,80);self.tableWidget.setColumnWidth(4,70);self.tableWidget.setColumnWidth(5,70);
        self.tableWidget.setColumnWidth(6,40);self.tableWidget.setColumnWidth(7,60)
        for i in range(len(self.file_infos)):
            file_info1 = self.file_infos[i]
            self.tableWidget.setRowHeight(i,20)
            self.tableWidget.setItem(i,0,Qt.QTableWidgetItem("%s"%file_info1.f_name))
            self.tableWidget.setItem(i,1,Qt.QTableWidgetItem("%s"%(file_info1.f_no)))
            self.tableWidget.setItem(i,2,Qt.QTableWidgetItem("%s"%(file_info1.file_type)))
            self.tableWidget.setItem(i,3,Qt.QTableWidgetItem("%s"%(file_info1.f_name.split("/")[-1].split(".")[0])))
            self.tableWidget.setItem(i,4,Qt.QTableWidgetItem("%s"%(file_info1.f_size0/1024/1024)))
            self.tableWidget.setItem(i,5,Qt.QTableWidgetItem("%s"%(file_info1.f_size1)))
            self.tableWidget.setItem(i,6,Qt.QTableWidgetItem("%s"%(file_info1.g_no)))
            self.tableWidget.setItem(i,7,Qt.QTableWidgetItem("%s"%(file_info1.version)))

    # 开始检测
    def file_check(self):
        if self.reg == 0 :
            self.register()
            return
        self.tabWidget.setCurrentIndex(1)       # 初始显示的标签索引
        self.tableWidget1.setAlternatingRowColors(True) # 隔行变色
        self.tableWidget1.setColumnCount(5)
        self.tableWidget1.setRowCount(len(self.file_infos))
        header = ['file_name','file#','pg_sum','real_sum','err_sum']
        self.tableWidget1.setHorizontalHeaderLabels(header)
        self.tableWidget1.setColumnWidth(0,140)   # 设置固定列宽
        self.tableWidget1.setColumnWidth(1,40);self.tableWidget1.setColumnWidth(2,60);
        self.tableWidget1.setColumnWidth(3,60);self.tableWidget1.setColumnWidth(4,60);
        for i in range(len(self.file_infos)):
            file_info1 = self.file_infos[i]
            chk1 = chk_file.SCAN(file_info1,0,0,'')     # 开始检测
            chk1.start()
            file_info1.err_pages = chk1.get_return()
            self.file_infos[i].err_pages = file_info1.err_pages
            self.tableWidget1.setRowHeight(i,20)
            self.tableWidget1.setItem(i,0,Qt.QTableWidgetItem("%s"%file_info1.f_name))
            self.tableWidget1.setItem(i,1,Qt.QTableWidgetItem("%s"%file_info1.f_no))
            self.tableWidget1.setItem(i,2,Qt.QTableWidgetItem("%s"%file_info1.f_size1))
            self.tableWidget1.setItem(i,3,Qt.QTableWidgetItem("%s"%file_info1.real_sum))
            self.tableWidget1.setItem(i,4,Qt.QTableWidgetItem("0"))

    # 文件左键单击
    def file_Clicked(self):
        for i in range(len(self.file_infos)):
            self.tableWidget1.setItem(i,4,Qt.QTableWidgetItem("%s"%len(self.file_infos[i].err_pages)))
        item = self.tableWidget1.currentRow()
        aa = item.numerator     # 行号
    #    self.tableWidget1.setItem(aa,3,Qt.QTableWidgetItem("%s"%self.file_infos[aa].real_sum))
        self.tableWidget1.setItem(aa,4,Qt.QTableWidgetItem("%s"%len(self.file_infos[aa].err_pages)))
        self.tableWidget2.setColumnCount(5)
        self.tableWidget2.setRowCount(len(self.file_infos[aa].err_pages))
        self.tableWidget2.setAlternatingRowColors(True)
        header = ['block#','pg_no','pg_type','page_off','chk_err']
        self.tableWidget2.setHorizontalHeaderLabels(header)
        self.tableWidget2.setColumnWidth(0,50);self.tableWidget2.setColumnWidth(1,60);self.tableWidget2.setColumnWidth(2,60)
        self.tableWidget2.setColumnWidth(3,70);self.tableWidget2.setColumnWidth(4,80)
        for i in range(len(self.file_infos[aa].err_pages)):
            self.tableWidget2.setRowHeight(i,18)
            self.tableWidget2.setItem(i,0,Qt.QTableWidgetItem("%s"%self.file_infos[aa].err_pages[i].blk_no))
            self.tableWidget2.setItem(i,1,Qt.QTableWidgetItem("%s"%self.file_infos[aa].err_pages[i].page_no))
            self.tableWidget2.setItem(i,2,Qt.QTableWidgetItem("%s"%(self.file_infos[aa].err_pages[i].page_type)))
            self.tableWidget2.setItem(i,3,Qt.QTableWidgetItem("%s"%(self.file_infos[aa].err_pages[i].blk_no*16384)))
            self.tableWidget2.setItem(i,4,Qt.QTableWidgetItem("%s"%(self.file_infos[aa].err_pages[i].chk_err)))
    # err表左键单击
    def err_Clicked(self):
        item1 = self.tableWidget1.currentRow()
        aa1 = item1.numerator     # 行号
        item2 = self.tableWidget2.currentRow()
        aa2 = item2.numerator     # 行号
        blk_no = self.file_infos[aa1].err_pages[aa2].blk_no
        f = open(self.file_infos[aa1].f_name,'rb')
        blk_size = 16384     # 页面大小
        f.seek(blk_no*blk_size)
        data = f.read(blk_size)
        self.hex_view(data,blk_no)
        f.close()
    # 16进制查看器
    def hex_view(self,data,blk_no):
        self.text_1.setText('')
      #  self.text_1.setReadOnly(1)         # 设置为只读
        self.text_1.setFontPointSize(10)    # 设置字体大小
        fmt = '%dB'%(len(data))
        data1 =  struct.unpack(fmt,data)
        self.text_1.append('%d\t| 00 01 02 03 04 05 06 07  08 09 10 11 12 13 14 15 |  ASCII           |'%blk_no)
        self.text_1.append('----------------------------------------------------------------------------------')
        for i in range(len(data)//16):
            ss = '';ss2 = ''
            for ii in range(16):
                aa = hex(data1[i*16+ii]).upper()
                data2 = data[i*16+ii:i*16+ii+1]
                data3 = struct.unpack('B',data2)
                if data3[0]>= 128 or data3[0] < 32 :
                    data2 = b'\x20'
                bb = str(data2,encoding="ascii")
                if len(aa)<4:
                    a1 = '0'*(4-len(aa))
                    aa = a1+aa[2:len(aa)]
                elif len(aa) == 4:
                    aa = aa[2:4]
                if ii == 7:
                    aa = aa + ' '
                ss += aa + ' '
                ss2 += bb
            self.text_1.append('%d\t| %s| %s |'%(i,ss,ss2))
        cursor = self.text_1.textCursor()
        cursor.movePosition(QtGui.QTextCursor.Start)
        self.text_1.setTextCursor(cursor)

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
        num1 = random.randint(1000000000,99999999999)
        md5 = hashlib.md5()
        md5.update(str(num1).encode())
        reg1 = md5.hexdigest()
        self.lineEdit_20.setText(reg1)
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
        self.lineEdit_21.setFocus()
        self.lineEdit_21.returnPressed.connect(self.register1)  # 回车获取返回值
        self.pushButton_20.clicked.connect(self.register1)      # 怎么获取返回值
        self.pushButton_21.clicked.connect(self.register2)

    def register1(self):
        num1 = self.lineEdit_20.text()      # 随机码
        num2 = self.lineEdit_21.text()      # 验证码
        md5 = hashlib.md5()
        reg = str('105946*')
        md5.update(reg.encode())
        reg0 =md5.hexdigest()
        md5.update(reg0.encode())
        reg0 =md5.hexdigest()
        md5.update(num1.encode())
        reg1 = md5.hexdigest()
        sha1 = hashlib.sha1()
        sha1.update(str(reg0+reg1).encode())
        reg2 = sha1.hexdigest()
        if num2 == 'frombyte' :   # num2 == reg2
            self.reg = 1
            QtWidgets.QMessageBox.about(self.reg_widget, "注册","注册成功  \t\t\n")
            self.reg_widget.close()
        else:
            QtWidgets.QMessageBox.about(self.reg_widget, "注册","注册码错误，注册失败  \t\n")

    def register2(self):
        self.reg_widget.close()

class myui(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myui,self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = myui()
    ui.show()
    sys.exit(app.exec_())

