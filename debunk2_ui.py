# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debunk2.ui'
#
# Created: Sun Apr 22 14:13:43 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_debunk2(object):
    def setupUi(self, debunk2):
        debunk2.setObjectName("debunk2")
        debunk2.resize(QtCore.QSize(QtCore.QRect(0,0,817,473).size()).expandedTo(debunk2.minimumSizeHint()))
        debunk2.setSizeGripEnabled(False)

        self.gridlayout = QtGui.QGridLayout(debunk2)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.exporthelp = QtGui.QPushButton(debunk2)
        self.exporthelp.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape(13)))
        self.exporthelp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.exporthelp.setIcon(QtGui.QIcon("../../../../usr/share/icons/crystalsvg/16x16/actions/info.png"))
        self.exporthelp.setAutoDefault(False)
        self.exporthelp.setFlat(True)
        self.exporthelp.setObjectName("exporthelp")
        self.gridlayout.addWidget(self.exporthelp,1,4,1,1)

        self.radioTSV = QtGui.QRadioButton(debunk2)
        self.radioTSV.setObjectName("radioTSV")
        self.gridlayout.addWidget(self.radioTSV,2,3,1,2)

        self.radioSSV = QtGui.QRadioButton(debunk2)
        self.radioSSV.setChecked(True)
        self.radioSSV.setObjectName("radioSSV")
        self.gridlayout.addWidget(self.radioSSV,3,3,1,2)

        self.radioSyncML = QtGui.QRadioButton(debunk2)
        self.radioSyncML.setEnabled(False)
        self.radioSyncML.setObjectName("radioSyncML")
        self.gridlayout.addWidget(self.radioSyncML,4,3,1,2)

        self.radioVCard = QtGui.QRadioButton(debunk2)
        self.radioVCard.setObjectName("radioVCard")
        self.gridlayout.addWidget(self.radioVCard,5,3,1,2)

        self.export = QtGui.QPushButton(debunk2)
        self.export.setObjectName("export")
        self.gridlayout.addWidget(self.export,6,3,1,2)

        spacerItem = QtGui.QSpacerItem(201,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem,0,2,1,1)

        spacerItem1 = QtGui.QSpacerItem(105,161,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1,7,3,1,2)

        self.nk2Locator = QtGui.QPushButton(debunk2)
        self.nk2Locator.setObjectName("nk2Locator")
        self.gridlayout.addWidget(self.nk2Locator,0,1,1,1)

        self.nk2Location = QtGui.QComboBox(debunk2)
        self.nk2Location.setMinimumSize(QtCore.QSize(500,0))
        self.nk2Location.setAcceptDrops(True)
        self.nk2Location.setEditable(True)
        self.nk2Location.setAutoCompletion(True)
        self.nk2Location.setDuplicatesEnabled(False)
        self.nk2Location.setObjectName("nk2Location")
        self.gridlayout.addWidget(self.nk2Location,0,0,1,1)

        self.parsedTable = QtGui.QTableWidget(debunk2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parsedTable.sizePolicy().hasHeightForWidth())
        self.parsedTable.setSizePolicy(sizePolicy)
        self.parsedTable.setAcceptDrops(True)
        self.parsedTable.setDragEnabled(True)
        self.parsedTable.setAlternatingRowColors(True)
        self.parsedTable.setObjectName("parsedTable")
        self.gridlayout.addWidget(self.parsedTable,1,0,8,3)

        spacerItem2 = QtGui.QSpacerItem(81,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2,8,3,1,1)

        self.about = QtGui.QToolButton(debunk2)
        self.about.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape(13)))
        self.about.setIcon(QtGui.QIcon("../../../../usr/share/icons/crystalsvg/16x16/devices/blockdevice.png"))
        self.about.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.about.setAutoRaise(True)
        self.about.setObjectName("about")
        self.gridlayout.addWidget(self.about,8,4,1,1)

        self.label_2 = QtGui.QLabel(debunk2)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,3,1,1)

        self.retranslateUi(debunk2)
        QtCore.QMetaObject.connectSlotsByName(debunk2)
        debunk2.setTabOrder(self.nk2Location,self.nk2Locator)
        debunk2.setTabOrder(self.nk2Locator,self.parsedTable)
        debunk2.setTabOrder(self.parsedTable,self.about)
        debunk2.setTabOrder(self.about,self.radioTSV)
        debunk2.setTabOrder(self.radioTSV,self.radioSSV)
        debunk2.setTabOrder(self.radioSSV,self.radioSyncML)
        debunk2.setTabOrder(self.radioSyncML,self.radioVCard)
        debunk2.setTabOrder(self.radioVCard,self.export)

    def retranslateUi(self, debunk2):
        debunk2.setWindowTitle(QtGui.QApplication.translate("debunk2", "debuNK2", None, QtGui.QApplication.UnicodeUTF8))
        self.exporthelp.setToolTip(QtGui.QApplication.translate("debunk2", "Soothing help text for confused users", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTSV.setToolTip(QtGui.QApplication.translate("debunk2", "Tab-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTSV.setText(QtGui.QApplication.translate("debunk2", "TSV", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSSV.setToolTip(QtGui.QApplication.translate("debunk2", "Semicolon-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSSV.setText(QtGui.QApplication.translate("debunk2", "SSV", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSyncML.setToolTip(QtGui.QApplication.translate("debunk2", "xml format suited for mobile phones", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSyncML.setText(QtGui.QApplication.translate("debunk2", "SyncML", None, QtGui.QApplication.UnicodeUTF8))
        self.radioVCard.setToolTip(QtGui.QApplication.translate("debunk2", "Electronic business card (.vcf)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioVCard.setText(QtGui.QApplication.translate("debunk2", "vCard", None, QtGui.QApplication.UnicodeUTF8))
        self.export.setText(QtGui.QApplication.translate("debunk2", "E&xport...", None, QtGui.QApplication.UnicodeUTF8))
        self.nk2Locator.setText(QtGui.QApplication.translate("debunk2", "&Locate NK2...", None, QtGui.QApplication.UnicodeUTF8))
        self.nk2Location.addItem(QtGui.QApplication.translate("debunk2", "Trying to find autocompletion (NK2) files...", None, QtGui.QApplication.UnicodeUTF8))
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
        self.about.setToolTip(QtGui.QApplication.translate("debunk2", "About this program...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("debunk2", "Export:", None, QtGui.QApplication.UnicodeUTF8))



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    debunk2 = QtGui.QDialog()
    ui = Ui_debunk2()
    ui.setupUi(debunk2)
    debunk2.show()
    sys.exit(app.exec_())
