# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debunk2.ui'
#
# Created: Mon Feb  5 01:48:24 2007
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_debunk2(object):
    def setupUi(self, debunk2):
        debunk2.setObjectName("debunk2")
        debunk2.resize(QtCore.QSize(QtCore.QRect(0,0,721,460).size()).expandedTo(debunk2.minimumSizeHint()))
        debunk2.setSizeGripEnabled(False)

        self.layoutWidget = QtGui.QWidget(debunk2)
        self.layoutWidget.setGeometry(QtCore.QRect(3,9,714,439))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridlayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.nk2Locator = QtGui.QPushButton(self.layoutWidget)
        self.nk2Locator.setObjectName("nk2Locator")
        self.gridlayout.addWidget(self.nk2Locator,0,1,1,1)

        self.nk2Location = QtGui.QComboBox(self.layoutWidget)
        self.nk2Location.setMinimumSize(QtCore.QSize(500,0))
        self.nk2Location.setAcceptDrops(True)
        self.nk2Location.setEditable(True)
        self.nk2Location.setAutoCompletion(True)
        self.nk2Location.setDuplicatesEnabled(False)
        self.nk2Location.setObjectName("nk2Location")
        self.gridlayout.addWidget(self.nk2Location,0,0,1,1)

        self.about = QtGui.QToolButton(self.layoutWidget)
        self.about.setIcon(QtGui.QIcon("../../../../usr/share/icons/crystalsvg/16x16/devices/blockdevice.png"))
        self.about.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.about.setAutoRaise(True)
        self.about.setObjectName("about")
        self.gridlayout.addWidget(self.about,0,4,1,1)

        spacerItem = QtGui.QSpacerItem(20,201,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem,2,3,1,2)

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.radioTSV = QtGui.QRadioButton(self.layoutWidget)
        self.radioTSV.setObjectName("radioTSV")
        self.gridlayout1.addWidget(self.radioTSV,2,0,1,1)

        self.radioSSV = QtGui.QRadioButton(self.layoutWidget)
        self.radioSSV.setChecked(True)
        self.radioSSV.setObjectName("radioSSV")
        self.gridlayout1.addWidget(self.radioSSV,3,0,1,1)

        self.radioCSV = QtGui.QRadioButton(self.layoutWidget)
        self.radioCSV.setChecked(False)
        self.radioCSV.setObjectName("radioCSV")
        self.gridlayout1.addWidget(self.radioCSV,1,0,1,1)

        self.export = QtGui.QPushButton(self.layoutWidget)
        self.export.setObjectName("export")
        self.gridlayout1.addWidget(self.export,6,0,1,1)

        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2,0,0,1,1)

        self.radioVCard = QtGui.QRadioButton(self.layoutWidget)
        self.radioVCard.setObjectName("radioVCard")
        self.gridlayout1.addWidget(self.radioVCard,5,0,1,1)

        self.radioSyncML = QtGui.QRadioButton(self.layoutWidget)
        self.radioSyncML.setEnabled(False)
        self.radioSyncML.setObjectName("radioSyncML")
        self.gridlayout1.addWidget(self.radioSyncML,4,0,1,1)
        self.gridlayout.addLayout(self.gridlayout1,1,3,1,2)

        spacerItem1 = QtGui.QSpacerItem(271,27,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1,0,3,1,1)

        self.parsedTable = QtGui.QTableWidget(self.layoutWidget)
        self.parsedTable.setMinimumSize(QtCore.QSize(600,400))
        self.parsedTable.setAcceptDrops(True)
        self.parsedTable.setDragEnabled(True)
        self.parsedTable.setAlternatingRowColors(True)
        self.parsedTable.setObjectName("parsedTable")
        self.gridlayout.addWidget(self.parsedTable,1,0,2,2)

        self.retranslateUi(debunk2)
        QtCore.QMetaObject.connectSlotsByName(debunk2)
        debunk2.setTabOrder(self.nk2Location,self.nk2Locator)
        debunk2.setTabOrder(self.nk2Locator,self.parsedTable)

    def retranslateUi(self, debunk2):
        debunk2.setWindowTitle(QtGui.QApplication.translate("debunk2", "debuNK2", None, QtGui.QApplication.UnicodeUTF8))
        self.nk2Locator.setText(QtGui.QApplication.translate("debunk2", "&Locate NK2...", None, QtGui.QApplication.UnicodeUTF8))
        self.nk2Location.addItem(QtGui.QApplication.translate("debunk2", "Trying to find autocompletion (NK2) files...", None, QtGui.QApplication.UnicodeUTF8))
        self.about.setToolTip(QtGui.QApplication.translate("debunk2", "About this program...", None, QtGui.QApplication.UnicodeUTF8))
        self.about.setText(QtGui.QApplication.translate("debunk2", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTSV.setToolTip(QtGui.QApplication.translate("debunk2", "Tab-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTSV.setText(QtGui.QApplication.translate("debunk2", "TSV", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSSV.setToolTip(QtGui.QApplication.translate("debunk2", "Semicolon-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSSV.setText(QtGui.QApplication.translate("debunk2", "SSV", None, QtGui.QApplication.UnicodeUTF8))
        self.radioCSV.setToolTip(QtGui.QApplication.translate("debunk2", "Comma-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioCSV.setText(QtGui.QApplication.translate("debunk2", "CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.export.setText(QtGui.QApplication.translate("debunk2", "E&xport...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("debunk2", "Export to file:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioVCard.setToolTip(QtGui.QApplication.translate("debunk2", "Electronic business card (.vcf)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioVCard.setText(QtGui.QApplication.translate("debunk2", "vCard", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSyncML.setToolTip(QtGui.QApplication.translate("debunk2", "xml format suited for mobile phones", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSyncML.setText(QtGui.QApplication.translate("debunk2", "SyncML", None, QtGui.QApplication.UnicodeUTF8))
        self.parsedTable.clear()
        self.parsedTable.setColumnCount(3)
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

        headerItem3 = QtGui.QTableWidgetItem()
        headerItem3.setText(QtGui.QApplication.translate("debunk2", "Organization", None, QtGui.QApplication.UnicodeUTF8))
        self.parsedTable.setHorizontalHeaderItem(2,headerItem3)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    debunk2 = QtGui.QDialog()
    ui = Ui_debunk2()
    ui.setupUi(debunk2)
    debunk2.show()
    sys.exit(app.exec_())
