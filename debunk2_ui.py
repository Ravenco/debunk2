# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debunk2.ui'
#
# Created: Sat Dec 30 15:57:07 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_debunk2(object):
    def setupUi(self, debunk2):
        debunk2.setObjectName("debunk2")
        debunk2.resize(QtCore.QSize(QtCore.QRect(0,0,592,470).size()).expandedTo(debunk2.minimumSizeHint()))
        debunk2.setSizeGripEnabled(True)

        self.Layout5 = QtGui.QWidget(debunk2)
        self.Layout5.setGeometry(QtCore.QRect(500,30,82,410))
        self.Layout5.setObjectName("Layout5")

        self.vboxlayout = QtGui.QVBoxLayout(self.Layout5)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.buttonOk = QtGui.QPushButton(self.Layout5)
        self.buttonOk.setAutoDefault(True)
        self.buttonOk.setDefault(True)
        self.buttonOk.setObjectName("buttonOk")
        self.vboxlayout.addWidget(self.buttonOk)

        self.buttonCancel = QtGui.QPushButton(self.Layout5)
        self.buttonCancel.setAutoDefault(True)
        self.buttonCancel.setObjectName("buttonCancel")
        self.vboxlayout.addWidget(self.buttonCancel)

        spacerItem = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.nk2Location = QtGui.QComboBox(debunk2)
        self.nk2Location.setGeometry(QtCore.QRect(10,30,371,21))
        self.nk2Location.setAcceptDrops(True)
        self.nk2Location.setEditable(True)
        self.nk2Location.setAutoCompletion(True)
        self.nk2Location.setDuplicatesEnabled(False)
        self.nk2Location.setObjectName("nk2Location")

        self.nk2Locator = QtGui.QPushButton(debunk2)
        self.nk2Locator.setGeometry(QtCore.QRect(390,30,94,21))
        self.nk2Locator.setObjectName("nk2Locator")

        self.parsedTable = QtGui.QTableWidget(debunk2)
        self.parsedTable.setGeometry(QtCore.QRect(10,60,481,381))
        self.parsedTable.setDragEnabled(True)
        self.parsedTable.setAlternatingRowColors(True)
        self.parsedTable.setObjectName("parsedTable")

        self.retranslateUi(debunk2)
        QtCore.QObject.connect(self.buttonOk,QtCore.SIGNAL("clicked()"),debunk2.accept)
        QtCore.QObject.connect(self.buttonCancel,QtCore.SIGNAL("clicked()"),debunk2.reject)
        QtCore.QMetaObject.connectSlotsByName(debunk2)
        debunk2.setTabOrder(self.nk2Location,self.nk2Locator)
        debunk2.setTabOrder(self.nk2Locator,self.parsedTable)
        debunk2.setTabOrder(self.parsedTable,self.buttonOk)
        debunk2.setTabOrder(self.buttonOk,self.buttonCancel)

    def retranslateUi(self, debunk2):
        debunk2.setWindowTitle(QtGui.QApplication.translate("debunk2", "debuNK2", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOk.setText(QtGui.QApplication.translate("debunk2", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("debunk2", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.nk2Location.addItem(QtGui.QApplication.translate("debunk2", "Trying to find autocompletion (NK2) files...", None, QtGui.QApplication.UnicodeUTF8))
        self.nk2Locator.setText(QtGui.QApplication.translate("debunk2", "Locate NK2...", None, QtGui.QApplication.UnicodeUTF8))
        self.parsedTable.clear()
        self.parsedTable.setColumnCount(2)
        self.parsedTable.setRowCount(1)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("debunk2", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.parsedTable.setVerticalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("debunk2", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.parsedTable.setHorizontalHeaderItem(0,headerItem1)

        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("debunk2", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.parsedTable.setHorizontalHeaderItem(1,headerItem2)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    debunk2 = QtGui.QDialog()
    ui = Ui_debunk2()
    ui.setupUi(debunk2)
    debunk2.show()
    sys.exit(app.exec_())
