# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainUI/MainUI.ui'
#
# Created: Sat Jun 18 07:55:04 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BCARM(object):
    def setupUi(self, BCARM):
        BCARM.setObjectName(_fromUtf8("BCARM"))
        BCARM.resize(1366, 768)
        BCARM.setStyleSheet(_fromUtf8("background: rgb(0, 0, 0)"))
        self.centralWidget = QtGui.QWidget(BCARM)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lbl_rgb = QtGui.QLabel(self.centralWidget)
        self.lbl_rgb.setGeometry(QtCore.QRect(0, 144, 640, 480))
        self.lbl_rgb.setText(_fromUtf8(""))
        self.lbl_rgb.setObjectName(_fromUtf8("lbl_rgb"))
        self.lbl_segmented = QtGui.QLabel(self.centralWidget)
        self.lbl_segmented.setGeometry(QtCore.QRect(726, 144, 640, 480))
        self.lbl_segmented.setText(_fromUtf8(""))
        self.lbl_segmented.setObjectName(_fromUtf8("lbl_segmented"))
        BCARM.setCentralWidget(self.centralWidget)

        self.retranslateUi(BCARM)
        QtCore.QMetaObject.connectSlotsByName(BCARM)

    def retranslateUi(self, BCARM):
        BCARM.setWindowTitle(_translate("BCARM", "MainWindow", None))

