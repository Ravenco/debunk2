# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debunk2.ui'
#
# Created: Sat Dec 30 20:18:18 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_debunk2(object):
    def setupUi(self, debunk2):
        debunk2.setObjectName("debunk2")
        debunk2.resize(QtCore.QSize(QtCore.QRect(0,0,615,479).size()).expandedTo(debunk2.minimumSizeHint()))
        debunk2.setSizeGripEnabled(True)

        self.parsedTable = QtGui.QTableWidget(debunk2)
        self.parsedTable.setGeometry(QtCore.QRect(10,60,481,381))
        self.parsedTable.setDragEnabled(True)
        self.parsedTable.setAlternatingRowColors(True)
        self.parsedTable.setObjectName("parsedTable")

        self.nk2Location = QtGui.QComboBox(debunk2)
        self.nk2Location.setGeometry(QtCore.QRect(10,30,381,22))
        self.nk2Location.setAcceptDrops(True)
        self.nk2Location.setEditable(True)
        self.nk2Location.setAutoCompletion(True)
        self.nk2Location.setDuplicatesEnabled(False)
        self.nk2Location.setObjectName("nk2Location")

        self.nk2Locator = QtGui.QPushButton(debunk2)
        self.nk2Locator.setGeometry(QtCore.QRect(400,25,91,27))
        self.nk2Locator.setObjectName("nk2Locator")

        self.widget = QtGui.QWidget(debunk2)
        self.widget.setGeometry(QtCore.QRect(500,60,83,197))
        self.widget.setObjectName("widget")

        self.vboxlayout = QtGui.QVBoxLayout(self.widget)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.vboxlayout.addWidget(self.label_2)

        self.radioCSV = QtGui.QRadioButton(self.widget)
        self.radioCSV.setChecked(False)
        self.radioCSV.setObjectName("radioCSV")
        self.vboxlayout.addWidget(self.radioCSV)

        self.radioTSV = QtGui.QRadioButton(self.widget)
        self.radioTSV.setObjectName("radioTSV")
        self.vboxlayout.addWidget(self.radioTSV)

        self.radioSSV = QtGui.QRadioButton(self.widget)
        self.radioSSV.setChecked(True)
        self.radioSSV.setObjectName("radioSSV")
        self.vboxlayout.addWidget(self.radioSSV)

        self.radioSyncML = QtGui.QRadioButton(self.widget)
        self.radioSyncML.setEnabled(False)
        self.radioSyncML.setObjectName("radioSyncML")
        self.vboxlayout.addWidget(self.radioSyncML)

        self.radioVCard = QtGui.QRadioButton(self.widget)
        self.radioVCard.setEnabled(False)
        self.radioVCard.setObjectName("radioVCard")
        self.vboxlayout.addWidget(self.radioVCard)

        self.export = QtGui.QPushButton(self.widget)
        self.export.setObjectName("export")
        self.vboxlayout.addWidget(self.export)

        self.progressBar = QtGui.QProgressBar(debunk2)
        self.progressBar.setGeometry(QtCore.QRect(10,450,118,23))
        self.progressBar.setProperty("value",QtCore.QVariant(0))
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")

        self.statusBar = QtGui.QLabel(debunk2)
        self.statusBar.setGeometry(QtCore.QRect(138,450,351,23))
        self.statusBar.setMinimumSize(QtCore.QSize(0,23))
        self.statusBar.setFrameShape(QtGui.QFrame.Box)
        self.statusBar.setObjectName("statusBar")

        self.retranslateUi(debunk2)
        QtCore.QMetaObject.connectSlotsByName(debunk2)
        debunk2.setTabOrder(self.nk2Location,self.nk2Locator)
        debunk2.setTabOrder(self.nk2Locator,self.parsedTable)

    def retranslateUi(self, debunk2):
        debunk2.setWindowTitle(QtGui.QApplication.translate("debunk2", "debuNK2", None, QtGui.QApplication.UnicodeUTF8))
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
        self.nk2Location.addItem(QtGui.QApplication.translate("debunk2", "Trying to find autocompletion (NK2) files...", None, QtGui.QApplication.UnicodeUTF8))
        self.nk2Locator.setText(QtGui.QApplication.translate("debunk2", "&Locate NK2...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("debunk2", "Export to file:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioCSV.setToolTip(QtGui.QApplication.translate("debunk2", "Comma-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioCSV.setText(QtGui.QApplication.translate("debunk2", "CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTSV.setToolTip(QtGui.QApplication.translate("debunk2", "Tab-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTSV.setText(QtGui.QApplication.translate("debunk2", "TSV", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSSV.setToolTip(QtGui.QApplication.translate("debunk2", "Semicolon-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSSV.setText(QtGui.QApplication.translate("debunk2", "SSV", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSyncML.setText(QtGui.QApplication.translate("debunk2", "SyncML", None, QtGui.QApplication.UnicodeUTF8))
        self.radioVCard.setText(QtGui.QApplication.translate("debunk2", "VCard", None, QtGui.QApplication.UnicodeUTF8))
        self.export.setText(QtGui.QApplication.translate("debunk2", "E&xport...", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBar.setText(QtGui.QApplication.translate("debunk2", "debuNK2 (C) 2006 havard@dahle.no", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    debunk2 = QtGui.QDialog()
    ui = Ui_debunk2()
    ui.setupUi(debunk2)
    debunk2.show()
    sys.exit(app.exec_())
