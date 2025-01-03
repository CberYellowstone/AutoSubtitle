# Form implementation generated from reading ui file 'd:\Code\AutoSubtitle\GUI_style.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AutoSubtitle(object):
    def setupUi(self, AutoSubtitle):
        AutoSubtitle.setObjectName("AutoSubtitle")
        AutoSubtitle.resize(635, 205)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AutoSubtitle.sizePolicy().hasHeightForWidth())
        AutoSubtitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        AutoSubtitle.setFont(font)
        AutoSubtitle.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        AutoSubtitle.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=AutoSubtitle)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(120, 150, 331, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.Title = QtWidgets.QLabel(parent=self.centralwidget)
        self.Title.setEnabled(True)
        self.Title.setGeometry(QtCore.QRect(20, 10, 341, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.chooseButtom = QtWidgets.QToolButton(parent=self.centralwidget)
        self.chooseButtom.setGeometry(QtCore.QRect(520, 70, 81, 31))
        self.chooseButtom.setObjectName("chooseButtom")
        self.saveButtom = QtWidgets.QToolButton(parent=self.centralwidget)
        self.saveButtom.setGeometry(QtCore.QRect(520, 110, 81, 31))
        self.saveButtom.setObjectName("saveButtom")
        self.OpenFilePathEdit = DragAcceptableQLine(parent=self.centralwidget)
        self.OpenFilePathEdit.setGeometry(QtCore.QRect(20, 70, 481, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.OpenFilePathEdit.setFont(font)
        self.OpenFilePathEdit.setStatusTip("")
        self.OpenFilePathEdit.setObjectName("OpenFilePathEdit")
        self.SaveFilePathEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SaveFilePathEdit.setGeometry(QtCore.QRect(20, 110, 481, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.SaveFilePathEdit.setFont(font)
        self.SaveFilePathEdit.setObjectName("SaveFilePathEdit")
        self.videoTypeList = QtWidgets.QComboBox(parent=self.centralwidget)
        self.videoTypeList.setGeometry(QtCore.QRect(370, 40, 231, 21))
        self.videoTypeList.setObjectName("videoTypeList")
        self.Title_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Title_2.setEnabled(True)
        self.Title_2.setGeometry(QtCore.QRect(230, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Title_2.setFont(font)
        self.Title_2.setObjectName("Title_2")
        self.setSavePathToDefaultButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.setSavePathToDefaultButton.setGeometry(QtCore.QRect(460, 140, 41, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.setSavePathToDefaultButton.setFont(font)
        self.setSavePathToDefaultButton.setObjectName("setSavePathToDefaultButton")
        self.FlagOPcomboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.FlagOPcomboBox.setGeometry(QtCore.QRect(510, 10, 91, 22))
        self.FlagOPcomboBox.setObjectName("FlagOPcomboBox")
        self.Title_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Title_3.setEnabled(True)
        self.Title_3.setGeometry(QtCore.QRect(370, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Title_3.setFont(font)
        self.Title_3.setObjectName("Title_3")
        AutoSubtitle.setCentralWidget(self.centralwidget)

        self.retranslateUi(AutoSubtitle)
        self.chooseButtom.clicked.connect(AutoSubtitle.raiseOpenFile) # type: ignore
        self.saveButtom.clicked.connect(AutoSubtitle.raiseSaveFile) # type: ignore
        self.startButton.clicked.connect(AutoSubtitle.tryToStart) # type: ignore
        self.OpenFilePathEdit.editingFinished.connect(AutoSubtitle.updateOpenPath) # type: ignore
        self.SaveFilePathEdit.editingFinished.connect(AutoSubtitle.updateSavePath) # type: ignore
        self.videoTypeList.currentIndexChanged['int'].connect(AutoSubtitle.updateVideoType) # type: ignore
        self.setSavePathToDefaultButton.clicked.connect(AutoSubtitle.setSavePathToDefault) # type: ignore
        self.OpenFilePathEdit.dropAccepted.connect(AutoSubtitle.updateOpenPath) # type: ignore
        self.FlagOPcomboBox.currentIndexChanged['int'].connect(AutoSubtitle.updateOPstyle) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AutoSubtitle)

    def retranslateUi(self, AutoSubtitle):
        _translate = QtCore.QCoreApplication.translate
        AutoSubtitle.setWindowTitle(_translate("AutoSubtitle", "AutoSubtitle"))
        self.startButton.setText(_translate("AutoSubtitle", "开始打轴"))
        self.Title.setText(_translate("AutoSubtitle", "<html><head/><body><p>自动打轴机<span style=\" color:#353535;\"> - By Yellowstone</span></p></body></html>"))
        self.chooseButtom.setText(_translate("AutoSubtitle", "选择打开视频"))
        self.saveButtom.setText(_translate("AutoSubtitle", "选择保存位置"))
        self.OpenFilePathEdit.setPlaceholderText(_translate("AutoSubtitle", "请选择输入视频文件路径"))
        self.SaveFilePathEdit.setPlaceholderText(_translate("AutoSubtitle", "请选择轴保存路径"))
        self.Title_2.setText(_translate("AutoSubtitle", "  请选择视频类型"))
        self.setSavePathToDefaultButton.setText(_translate("AutoSubtitle", "默认"))
        self.Title_3.setText(_translate("AutoSubtitle", "请选择Flag系列OP类型"))
from DragAcceptableQLine import DragAcceptableQLine
