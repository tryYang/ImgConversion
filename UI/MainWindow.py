# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1369, 1068)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(710, 20, 471, 281))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.Tb_Tip = QtWidgets.QTextEdit(self.widget_2)
        self.Tb_Tip.setObjectName("Tb_Tip")
        self.verticalLayout.addWidget(self.Tb_Tip)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 290, 1151, 564))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Gv_inputimg = QtWidgets.QGraphicsView(self.tab)
        self.Gv_inputimg.setMinimumSize(QtCore.QSize(520, 520))
        self.Gv_inputimg.setMaximumSize(QtCore.QSize(520, 520))
        self.Gv_inputimg.setObjectName("Gv_inputimg")
        self.horizontalLayout_11.addWidget(self.Gv_inputimg)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_11.addWidget(self.pushButton_11)
        self.Gv_outputimg = QtWidgets.QGraphicsView(self.tab)
        self.Gv_outputimg.setMinimumSize(QtCore.QSize(520, 520))
        self.Gv_outputimg.setMaximumSize(QtCore.QSize(520, 520))
        self.Gv_outputimg.setObjectName("Gv_outputimg")
        self.horizontalLayout_11.addWidget(self.Gv_outputimg)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LineChartLayout = QtWidgets.QGridLayout()
        self.LineChartLayout.setObjectName("LineChartLayout")
        self.gridLayout_2.addLayout(self.LineChartLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 10, 561, 181))
        self.widget_3.setStyleSheet("background-color: white;")
        self.widget_3.setObjectName("widget_3")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setGeometry(QtCore.QRect(20, 30, 541, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Tb_Model = QtWidgets.QTextEdit(self.widget)
        self.Tb_Model.setObjectName("Tb_Model")
        self.horizontalLayout.addWidget(self.Tb_Model)
        self.btn_importmodel = QtWidgets.QPushButton(self.widget)
        self.btn_importmodel.setObjectName("btn_importmodel")
        self.horizontalLayout.addWidget(self.btn_importmodel)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Tb_cbdir = QtWidgets.QTextEdit(self.widget)
        self.Tb_cbdir.setObjectName("Tb_cbdir")
        self.horizontalLayout_5.addWidget(self.Tb_cbdir)
        self.btn_importcbdir = QtWidgets.QPushButton(self.widget)
        self.btn_importcbdir.setObjectName("btn_importcbdir")
        self.horizontalLayout_5.addWidget(self.btn_importcbdir)
        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Tb_ctdir = QtWidgets.QTextEdit(self.widget)
        self.Tb_ctdir.setObjectName("Tb_ctdir")
        self.horizontalLayout_10.addWidget(self.Tb_ctdir)
        self.btn_importctdir = QtWidgets.QPushButton(self.widget)
        self.btn_importctdir.setObjectName("btn_importctdir")
        self.horizontalLayout_10.addWidget(self.btn_importctdir)
        self.horizontalLayout_10.setStretch(0, 4)
        self.horizontalLayout_10.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(40, 220, 531, 41))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.isShow_ssim = QtWidgets.QCheckBox(self.widget_4)
        self.isShow_ssim.setChecked(True)
        self.isShow_ssim.setObjectName("isShow_ssim")
        self.horizontalLayout_2.addWidget(self.isShow_ssim)
        self.isShow_psnr = QtWidgets.QCheckBox(self.widget_4)
        self.isShow_psnr.setChecked(True)
        self.isShow_psnr.setObjectName("isShow_psnr")
        self.horizontalLayout_2.addWidget(self.isShow_psnr)
        self.isShow_mse = QtWidgets.QCheckBox(self.widget_4)
        self.isShow_mse.setChecked(True)
        self.isShow_mse.setObjectName("isShow_mse")
        self.horizontalLayout_2.addWidget(self.isShow_mse)
        self.btn_showlinechart = QtWidgets.QPushButton(self.widget_4)
        self.btn_showlinechart.setObjectName("btn_showlinechart")
        self.horizontalLayout_2.addWidget(self.btn_showlinechart)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1369, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "提示"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "图片转换"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "趋势图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "页"))
        self.btn_importmodel.setText(_translate("MainWindow", "导入模型"))
        self.btn_importcbdir.setText(_translate("MainWindow", "导入cbct文件夹"))
        self.btn_importctdir.setText(_translate("MainWindow", "导入ct文件夹"))
        self.isShow_ssim.setText(_translate("MainWindow", "SSIM"))
        self.isShow_psnr.setText(_translate("MainWindow", "PSNR"))
        self.isShow_mse.setText(_translate("MainWindow", "MSE"))
        self.btn_showlinechart.setText(_translate("MainWindow", "生成趋势图"))
