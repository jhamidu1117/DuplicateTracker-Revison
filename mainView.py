# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jhamidullah\PycharmProjects\DuplicateTracker-Revison\UI\MainView.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 488)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("background: transparent")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setLineWidth(0)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setForegroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.LocationLabel = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LocationLabel.sizePolicy().hasHeightForWidth())
        self.LocationLabel.setSizePolicy(sizePolicy)
        self.LocationLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.LocationLabel.setObjectName("LocationLabel")
        self.verticalLayout.addWidget(self.LocationLabel)
        self.TrgLineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TrgLineEdit.sizePolicy().hasHeightForWidth())
        self.TrgLineEdit.setSizePolicy(sizePolicy)
        self.TrgLineEdit.setText("")
        self.TrgLineEdit.setObjectName("TrgLineEdit")
        self.verticalLayout.addWidget(self.TrgLineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Enter = QtWidgets.QPushButton(self.tab)
        self.Enter.setObjectName("Enter")
        self.horizontalLayout_2.addWidget(self.Enter)
        self.Redo = QtWidgets.QPushButton(self.tab)
        self.Redo.setObjectName("Redo")
        self.horizontalLayout_2.addWidget(self.Redo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(12, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OutputTable = QtWidgets.QTableWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OutputTable.sizePolicy().hasHeightForWidth())
        self.OutputTable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.OutputTable.setFont(font)
        self.OutputTable.setObjectName("OutputTable")
        self.OutputTable.setColumnCount(3)
        self.OutputTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.OutputTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OutputTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OutputTable.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.OutputTable)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setStyleSheet("background: transparent")
        self.graphicsView_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_2.setLineWidth(0)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setForegroundBrush(brush)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_2.addWidget(self.graphicsView_2)
        self.LocationLabel_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LocationLabel_2.sizePolicy().hasHeightForWidth())
        self.LocationLabel_2.setSizePolicy(sizePolicy)
        self.LocationLabel_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.LocationLabel_2.setObjectName("LocationLabel_2")
        self.verticalLayout_2.addWidget(self.LocationLabel_2)
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Enter_2 = QtWidgets.QPushButton(self.tab_2)
        self.Enter_2.setObjectName("Enter_2")
        self.horizontalLayout_6.addWidget(self.Enter_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(12, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.OutputTable_2 = QtWidgets.QTableWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OutputTable_2.sizePolicy().hasHeightForWidth())
        self.OutputTable_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.OutputTable_2.setFont(font)
        self.OutputTable_2.setObjectName("OutputTable_2")
        self.OutputTable_2.setColumnCount(3)
        self.OutputTable_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.OutputTable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OutputTable_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OutputTable_2.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_5.addWidget(self.OutputTable_2)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setStyleSheet("background: transparent")
        self.graphicsView_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_3.setLineWidth(0)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_3.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_3.setForegroundBrush(brush)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_3.addWidget(self.graphicsView_3)
        self.LocationLabel_3 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LocationLabel_3.sizePolicy().hasHeightForWidth())
        self.LocationLabel_3.setSizePolicy(sizePolicy)
        self.LocationLabel_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.LocationLabel_3.setObjectName("LocationLabel_3")
        self.verticalLayout_3.addWidget(self.LocationLabel_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Enter_3 = QtWidgets.QPushButton(self.tab_3)
        self.Enter_3.setObjectName("Enter_3")
        self.horizontalLayout_9.addWidget(self.Enter_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(12, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.OutputTable_3 = QtWidgets.QTableWidget(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OutputTable_3.sizePolicy().hasHeightForWidth())
        self.OutputTable_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.OutputTable_3.setFont(font)
        self.OutputTable_3.setObjectName("OutputTable_3")
        self.OutputTable_3.setColumnCount(3)
        self.OutputTable_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.OutputTable_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OutputTable_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OutputTable_3.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_8.addWidget(self.OutputTable_3)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(2, 1)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView_4.sizePolicy().hasHeightForWidth())
        self.graphicsView_4.setSizePolicy(sizePolicy)
        self.graphicsView_4.setStyleSheet("background: transparent")
        self.graphicsView_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_4.setLineWidth(0)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_4.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_4.setForegroundBrush(brush)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalLayout_4.addWidget(self.graphicsView_4)
        self.LocationLabel_4 = QtWidgets.QLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LocationLabel_4.sizePolicy().hasHeightForWidth())
        self.LocationLabel_4.setSizePolicy(sizePolicy)
        self.LocationLabel_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.LocationLabel_4.setObjectName("LocationLabel_4")
        self.verticalLayout_4.addWidget(self.LocationLabel_4)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.Enter_4 = QtWidgets.QPushButton(self.tab_4)
        self.Enter_4.setObjectName("Enter_4")
        self.horizontalLayout_12.addWidget(self.Enter_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_4.addWidget(self.progressBar_2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(12, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.OutputTable_4 = QtWidgets.QTableWidget(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.OutputTable_4.sizePolicy().hasHeightForWidth())
        self.OutputTable_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.OutputTable_4.setFont(font)
        self.OutputTable_4.setObjectName("OutputTable_4")
        self.OutputTable_4.setColumnCount(4)
        self.OutputTable_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.OutputTable_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OutputTable_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OutputTable_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OutputTable_4.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_11.addWidget(self.OutputTable_4)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(2, 1)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 21))
        self.menubar.setObjectName("menubar")
        self.menuFunctions = QtWidgets.QMenu(self.menubar)
        self.menuFunctions.setObjectName("menuFunctions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOffline_Mode = QtWidgets.QAction(MainWindow)
        self.actionOffline_Mode.setObjectName("actionOffline_Mode")
        self.actionOnline_Mode = QtWidgets.QAction(MainWindow)
        self.actionOnline_Mode.setObjectName("actionOnline_Mode")
        self.actionConfig = QtWidgets.QAction(MainWindow)
        self.actionConfig.setObjectName("actionConfig")
        self.menuFunctions.addAction(self.actionOnline_Mode)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionConfig)
        self.menubar.addAction(self.menuFunctions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LocationLabel.setText(_translate("MainWindow", "Location"))
        self.TrgLineEdit.setPlaceholderText(_translate("MainWindow", "TRG-xxxxxxxx"))
        self.Enter.setText(_translate("MainWindow", "Enter"))
        self.Redo.setText(_translate("MainWindow", "Redo"))
        item = self.OutputTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TRGID"))
        item = self.OutputTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "timeStamp"))
        item = self.OutputTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Scan TRG"))
        self.LocationLabel_2.setText(_translate("MainWindow", "Enter TRGs"))
        self.Enter_2.setText(_translate("MainWindow", "Enter"))
        item = self.OutputTable_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TRGID"))
        item = self.OutputTable_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "timeStamp"))
        item = self.OutputTable_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Search TRGs"))
        self.LocationLabel_3.setText(_translate("MainWindow", "Enter Location IDs"))
        self.Enter_3.setText(_translate("MainWindow", "Enter"))
        item = self.OutputTable_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TRGID"))
        item = self.OutputTable_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "timeStamp"))
        item = self.OutputTable_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Search Locations"))
        self.LocationLabel_4.setText(_translate("MainWindow", "Export"))
        self.Enter_4.setText(_translate("MainWindow", "Select FMSI Export "))
        item = self.OutputTable_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TRGID"))
        item = self.OutputTable_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "timeStamp"))
        item = self.OutputTable_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Location"))
        item = self.OutputTable_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Error"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "FMSI QC"))
        self.menuFunctions.setTitle(_translate("MainWindow", "Functions"))
        self.actionOffline_Mode.setText(_translate("MainWindow", "Search"))
        self.actionOnline_Mode.setText(_translate("MainWindow", "Online Mode"))
        self.actionConfig.setText(_translate("MainWindow", "Config."))
