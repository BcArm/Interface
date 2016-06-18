# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/GridUI/GridUI.ui'
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
        self.B = QtGui.QLabel(self.centralWidget)
        self.B.setGeometry(QtCore.QRect(595, 30, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.B.setFont(font)
        self.B.setStyleSheet(_fromUtf8("color: rgb(61, 61, 61)"))
        self.B.setAlignment(QtCore.Qt.AlignCenter)
        self.B.setObjectName(_fromUtf8("B"))
        self.A = QtGui.QLabel(self.centralWidget)
        self.A.setGeometry(QtCore.QRect(140, 30, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.A.setFont(font)
        self.A.setStyleSheet(_fromUtf8("color: rgb(61, 61, 61)"))
        self.A.setAlignment(QtCore.Qt.AlignCenter)
        self.A.setObjectName(_fromUtf8("A"))
        self.C = QtGui.QLabel(self.centralWidget)
        self.C.setGeometry(QtCore.QRect(1050, 30, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.C.setFont(font)
        self.C.setStyleSheet(_fromUtf8("color: rgb(61, 61, 61)"))
        self.C.setAlignment(QtCore.Qt.AlignCenter)
        self.C.setObjectName(_fromUtf8("C"))
        self.E = QtGui.QLabel(self.centralWidget)
        self.E.setGeometry(QtCore.QRect(595, 290, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.E.setFont(font)
        self.E.setStyleSheet(_fromUtf8("color: rgb(61, 61, 61)"))
        self.E.setAlignment(QtCore.Qt.AlignCenter)
        self.E.setObjectName(_fromUtf8("E"))
        self.D = QtGui.QLabel(self.centralWidget)
        self.D.setGeometry(QtCore.QRect(140, 290, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.D.setFont(font)
        self.D.setStyleSheet(_fromUtf8("color: rgb(61, 61, 61)"))
        self.D.setAlignment(QtCore.Qt.AlignCenter)
        self.D.setObjectName(_fromUtf8("D"))
        self.F = QtGui.QLabel(self.centralWidget)
        self.F.setGeometry(QtCore.QRect(1050, 290, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.F.setFont(font)
        self.F.setStyleSheet(_fromUtf8("color: rgb(61, 61, 61)"))
        self.F.setAlignment(QtCore.Qt.AlignCenter)
        self.F.setObjectName(_fromUtf8("F"))
        self.H = QtGui.QLabel(self.centralWidget)
        self.H.setGeometry(QtCore.QRect(595, 540, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.H.setFont(font)
        self.H.setStyleSheet(_fromUtf8("color: rgb(61, 61, 61)"))
        self.H.setAlignment(QtCore.Qt.AlignCenter)
        self.H.setObjectName(_fromUtf8("H"))
        self.G = QtGui.QLabel(self.centralWidget)
        self.G.setGeometry(QtCore.QRect(140, 540, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.G.setFont(font)
        self.G.setStyleSheet(_fromUtf8("color: rgb(61, 61, 61)"))
        self.G.setAlignment(QtCore.Qt.AlignCenter)
        self.G.setObjectName(_fromUtf8("G"))
        self.I = QtGui.QLabel(self.centralWidget)
        self.I.setGeometry(QtCore.QRect(1050, 540, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.I.setFont(font)
        self.I.setStyleSheet(_fromUtf8("color: rgb(61, 61, 61)"))
        self.I.setAlignment(QtCore.Qt.AlignCenter)
        self.I.setObjectName(_fromUtf8("I"))
        BCARM.setCentralWidget(self.centralWidget)

        self.retranslateUi(BCARM)
        QtCore.QMetaObject.connectSlotsByName(BCARM)

    def retranslateUi(self, BCARM):
        BCARM.setWindowTitle(_translate("BCARM", "MainWindow", None))
        self.B.setText(_translate("BCARM", "B", None))
        self.A.setText(_translate("BCARM", "A", None))
        self.C.setText(_translate("BCARM", "C", None))
        self.E.setText(_translate("BCARM", "E", None))
        self.D.setText(_translate("BCARM", "D", None))
        self.F.setText(_translate("BCARM", "F", None))
        self.H.setText(_translate("BCARM", "H", None))
        self.G.setText(_translate("BCARM", "G", None))
        self.I.setText(_translate("BCARM", "I", None))

