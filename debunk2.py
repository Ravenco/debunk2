#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2006-2007 - Håvard Dahle
#    <havard@dahle.no>
#
#    Lisence: GPL2
#
# $Id$
###########################################################################

__doc__ = """Export MS Outlook NK2 files into something readable by humans and machines (qt4 gui)
"""
import sys, types, os.path, os, glob
from PyQt4 import QtCore, QtGui, uic
import debunk2_ui, nk2parser

# constants
CSV=1  # comma-separated
TSV=2  # tab-separated
SSV=3  # semicolon-separated
XML=4  # 
VCARD=5  # vcard spec
SYNCML=6  # syncml
ODT=7  # OpenSpreadsheet 

#gui = uic.loadUi('debunk2.ui')

class debunker(QtGui.QDialog):#, debunk2_ui.Ui_debunk2):
    
    nk2 = None
    pathlist = []
    
    def __init__(self):#,parent = None,name = None,modal = 0,fl = 0):
        QtGui.QDialog.__init__(self)
        #debunk2_ui.Ui_debunk2.__init__(self)#, parent, name, fl)
        self.ui = debunk2_ui.Ui_debunk2()
        self.ui.setupUi(self)
        
        #self.setupUi(debunk2_ui.Ui_debunk2)
        QtCore.QObject.connect(self.ui.nk2Location, QtCore.SIGNAL('highlighted(int)'), self.loadNK2)

        here = os.getenv('PWD')
        if here is not None:
            self.pathlist.append(here)
        
        self.displayPaths(self.findNK2())
        
        self.loadNK2()
        
    def findNK2(self):
        "Look in the default places for an NK2 file. Returns list of found files"
        #return "test.NK2"
        locations = []
        for p in self.pathlist:
            locations += glob.glob(p+"/*.NK2")
            locations += glob.glob(p+"/*.nk2")
        return locations
    
    def displayPaths(self, pathlist):
        "Displays different paths so the user can choose"
        self.ui.nk2Location.clear()
        #for z in pathlist: 
            #self.ui.nk2Location.insertItem(z)
        self.ui.nk2Location.insertItems(0, pathlist)
    
    def loadNK2(self, item=0):
        "Load an NK2 and display it"
        path = unicode(self.ui.nk2Location.currentText())
        print "path", path
        assert(os.path.exists(path))
        #del(self.nk2)
        self.nk2 = nk2parser.nk2bib(path)  # init the parser
        self.nk2.parse()                   # slurp the file
        self.ui.parsedTable.setRowCount(len(self.nk2.records) + 1) # expand table to keep all records
        i  = 0
        for rec in self.nk2.records:
            self.ui.parsedTable.setItem(i, 0, QtGui.QTableWidgetItem(rec.name))
            self.ui.parsedTable.setItem(i, 1, QtGui.QTableWidgetItem(rec.address))
            #self.ui.parsedTable.setText(i, 0, rec.name)
            #self.ui.parsedTable.setText(i, 1, rec.address)
            i += 1
        #self.nk2.check()
    
    def saveTable(self, format=SSV):
        if format in (CSV, TSV, SSV):
            return self.saveTableCharacterSeparated(format)
        elif format == XML:
            return self.saveTableXml()
        
    def saveTableCharacterSeparated(self, format):
        pass
    
    def saveTableXml(self):
        pass

if __name__ == "__main__":

    DEBUGLEVEL = sys.argv.count('-d')
    nk2parser.DEBUGLEVEL = DEBUGLEVEL

    if "-h" in sys.argv[1:]:
        print __doc__
        print "Bruk %s -i for å lage kommandolinjefaktura" % sys.argv[0]
        sys.exit()
    elif False:
        a = QtGui.QApplication(sys.argv)
        #QtCore.QObject.connect(a,QtCore.SIGNAL('lastWindowClosed()'),a,QtCore.SLOT('quit()'))
        ui = debunker()
        d.show()
        #a.exec_loop()
        sys.exit(app.exec_())
    else:
        app = QtGui.QApplication(sys.argv)
        debunk2 = QtGui.QDialog()
        ui = debunker()
        #ui.setupUi(debunk2)
        ui.show()
        sys.exit(app.exec_())
