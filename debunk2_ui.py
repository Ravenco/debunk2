# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debunk2.ui'
#
# Created: Thu Sep 27 13:10:51 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_debunk2(object):
    def setupUi(self, debunk2):
        debunk2.setObjectName("debunk2")
        debunk2.resize(QtCore.QSize(QtCore.QRect(0,0,936,543).size()).expandedTo(debunk2.minimumSizeHint()))
        debunk2.setSizeGripEnabled(False)

        self.gridlayout = QtGui.QGridLayout(debunk2)
        self.gridlayout.setObjectName("gridlayout")

        self.nk2Location = QtGui.QComboBox(debunk2)
        self.nk2Location.setMinimumSize(QtCore.QSize(500,0))
        self.nk2Location.setAcceptDrops(True)
        self.nk2Location.setEditable(True)
        self.nk2Location.setAutoCompletion(True)
        self.nk2Location.setDuplicatesEnabled(False)
        self.nk2Location.setObjectName("nk2Location")
        self.gridlayout.addWidget(self.nk2Location,0,0,1,1)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.nk2Locator = QtGui.QPushButton(debunk2)
        self.nk2Locator.setObjectName("nk2Locator")
        self.hboxlayout.addWidget(self.nk2Locator)
        self.gridlayout.addLayout(self.hboxlayout,0,1,1,1)

        self.parsedTable = QtGui.QTableWidget(debunk2)
        self.parsedTable.setAcceptDrops(True)
        self.parsedTable.setDragEnabled(True)
        self.parsedTable.setAlternatingRowColors(True)
        self.parsedTable.setObjectName("parsedTable")
        self.gridlayout.addWidget(self.parsedTable,1,0,4,1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.label_2 = QtGui.QLabel(debunk2)
        self.label_2.setObjectName("label_2")
        self.hboxlayout1.addWidget(self.label_2)

        self.exporthelp = QtGui.QPushButton(debunk2)
        self.exporthelp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.exporthelp.setIcon(QtGui.QIcon("../../../../usr/share/icons/crystalsvg/16x16/actions/info.png"))
        self.exporthelp.setAutoDefault(False)
        self.exporthelp.setFlat(True)
        self.exporthelp.setObjectName("exporthelp")
        self.hboxlayout1.addWidget(self.exporthelp)
        self.gridlayout.addLayout(self.hboxlayout1,1,1,1,1)

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")

        self.radioTSV = QtGui.QRadioButton(debunk2)
        self.radioTSV.setObjectName("radioTSV")
        self.vboxlayout.addWidget(self.radioTSV)

        self.radioSSV = QtGui.QRadioButton(debunk2)
        self.radioSSV.setChecked(True)
        self.radioSSV.setObjectName("radioSSV")
        self.vboxlayout.addWidget(self.radioSSV)

        self.radioVCard = QtGui.QRadioButton(debunk2)
        self.radioVCard.setObjectName("radioVCard")
        self.vboxlayout.addWidget(self.radioVCard)

        self.radioXCard = QtGui.QRadioButton(debunk2)
        self.radioXCard.setObjectName("radioXCard")
        self.vboxlayout.addWidget(self.radioXCard)

        self.export = QtGui.QPushButton(debunk2)
        self.export.setObjectName("export")
        self.vboxlayout.addWidget(self.export)
        self.gridlayout.addLayout(self.vboxlayout,2,1,1,1)

        spacerItem = QtGui.QSpacerItem(109,201,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem,3,1,1,1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem1 = QtGui.QSpacerItem(81,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)

        self.about = QtGui.QToolButton(debunk2)
        self.about.setIcon(QtGui.QIcon("../../../../usr/share/icons/crystalsvg/16x16/devices/blockdevice.png"))
        self.about.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.about.setAutoRaise(True)
        self.about.setObjectName("about")
        self.hboxlayout2.addWidget(self.about)
        self.gridlayout.addLayout(self.hboxlayout2,4,1,1,1)

        self.retranslateUi(debunk2)
        QtCore.QMetaObject.connectSlotsByName(debunk2)
        debunk2.setTabOrder(self.nk2Location,self.nk2Locator)
        debunk2.setTabOrder(self.nk2Locator,self.parsedTable)
        debunk2.setTabOrder(self.parsedTable,self.about)
        debunk2.setTabOrder(self.about,self.radioTSV)
        debunk2.setTabOrder(self.radioTSV,self.radioSSV)
        debunk2.setTabOrder(self.radioSSV,self.radioVCard)
        debunk2.setTabOrder(self.radioVCard,self.export)

    def retranslateUi(self, debunk2):
        debunk2.setWindowTitle(QtGui.QApplication.translate("debunk2", "debuNK2", None, QtGui.QApplication.UnicodeUTF8))
        self.nk2Location.addItem(QtGui.QApplication.translate("debunk2", "Trying to find autocompletion (NK2) files...", None, QtGui.QApplication.UnicodeUTF8))
        self.nk2Locator.setText(QtGui.QApplication.translate("debunk2", "&Locate NK2...", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_2.setText(QtGui.QApplication.translate("debunk2", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Export:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exporthelp.setToolTip(QtGui.QApplication.translate("debunk2", "Soothing help text for confused users", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTSV.setToolTip(QtGui.QApplication.translate("debunk2", "Tab-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTSV.setText(QtGui.QApplication.translate("debunk2", "TSV", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSSV.setToolTip(QtGui.QApplication.translate("debunk2", "Semicolon-separated values", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSSV.setText(QtGui.QApplication.translate("debunk2", "SSV", None, QtGui.QApplication.UnicodeUTF8))
        self.radioVCard.setToolTip(QtGui.QApplication.translate("debunk2", "Electronic business card (.vcf)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioVCard.setText(QtGui.QApplication.translate("debunk2", "vCard", None, QtGui.QApplication.UnicodeUTF8))
        self.radioXCard.setToolTip(QtGui.QApplication.translate("debunk2", "Electronic business card, formatted with xml ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioXCard.setText(QtGui.QApplication.translate("debunk2", "xCard", None, QtGui.QApplication.UnicodeUTF8))
        self.export.setText(QtGui.QApplication.translate("debunk2", "E&xport...", None, QtGui.QApplication.UnicodeUTF8))
        self.about.setToolTip(QtGui.QApplication.translate("debunk2", "About this program...", None, QtGui.QApplication.UnicodeUTF8))



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    debunk2 = QtGui.QDialog()
    ui = Ui_debunk2()
    ui.setupUi(debunk2)
    debunk2.show()
    sys.exit(app.exec_())
