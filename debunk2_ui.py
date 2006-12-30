# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debunk2.ui'
#
# Created: Fri Dec 29 17:58:32 2006
#      by: The PyQt User Interface Compiler (pyuic) 3.16
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *
from qttable import QTable


class debunk2(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("debunk2")

        self.setSizeGripEnabled(1)


        LayoutWidget = QWidget(self,"Layout5")
        LayoutWidget.setGeometry(QRect(500,30,82,410))
        Layout5 = QVBoxLayout(LayoutWidget,0,6,"Layout5")

        self.buttonOk = QPushButton(LayoutWidget,"buttonOk")
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)
        Layout5.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(LayoutWidget,"buttonCancel")
        self.buttonCancel.setAutoDefault(1)
        Layout5.addWidget(self.buttonCancel)
        Spacer1 = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        Layout5.addItem(Spacer1)

        self.nk2Locator = QPushButton(self,"nk2Locator")
        self.nk2Locator.setGeometry(QRect(390,30,94,21))

        self.nk2Location = QComboBox(0,self,"nk2Location")
        self.nk2Location.setGeometry(QRect(10,30,371,21))
        self.nk2Location.setAcceptDrops(1)
        self.nk2Location.setEditable(1)
        self.nk2Location.setAutoCompletion(1)
        self.nk2Location.setDuplicatesEnabled(0)

        self.parsedTable = QTable(self,"parsedTable")
        self.parsedTable.setNumCols(self.parsedTable.numCols() + 1)
        self.parsedTable.horizontalHeader().setLabel(self.parsedTable.numCols() - 1,self.__tr("Name"))
        self.parsedTable.setNumCols(self.parsedTable.numCols() + 1)
        self.parsedTable.horizontalHeader().setLabel(self.parsedTable.numCols() - 1,self.__tr("Address"))
        self.parsedTable.setNumRows(self.parsedTable.numRows() + 1)
        self.parsedTable.verticalHeader().setLabel(self.parsedTable.numRows() - 1,self.__tr("1"))
        self.parsedTable.setGeometry(QRect(10,70,480,370))
        self.parsedTable.setResizePolicy(QTable.Default)
        self.parsedTable.setVScrollBarMode(QTable.AlwaysOn)
        self.parsedTable.setDragAutoScroll(1)
        self.parsedTable.setNumRows(1)
        self.parsedTable.setNumCols(2)
        self.parsedTable.setReadOnly(0)

        self.languageChange()

        self.resize(QSize(592,470).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.buttonOk,SIGNAL("clicked()"),self.accept)
        self.connect(self.buttonCancel,SIGNAL("clicked()"),self.reject)


    def languageChange(self):
        self.setCaption(self.__tr("debuNK2"))
        self.buttonOk.setText(self.__tr("&OK"))
        self.buttonOk.setAccel(QKeySequence(QString.null))
        self.buttonCancel.setText(self.__tr("&Cancel"))
        self.buttonCancel.setAccel(QKeySequence(QString.null))
        self.nk2Locator.setText(self.__tr("Locate NK2..."))
        self.nk2Location.clear()
        self.nk2Location.insertItem(self.__tr("Trying to find autocompletion (NK2) files..."))
        self.parsedTable.horizontalHeader().setLabel(0,self.__tr("Name"))
        self.parsedTable.horizontalHeader().setLabel(1,self.__tr("Address"))
        self.parsedTable.verticalHeader().setLabel(0,self.__tr("1"))


    def __tr(self,s,c = None):
        return qApp.translate("debunk2",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = debunk2()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
