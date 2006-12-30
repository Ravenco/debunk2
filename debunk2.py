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

class debunker(QtGui.QDialog):#, debunk2_ui.Ui_debunk2):
    
    nk2 = None
    pathlist = []
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = debunk2_ui.Ui_debunk2()
        self.ui.setupUi(self)
        
        #QtCore.QObject.connect(self.ui.nk2Location, QtCore.SIGNAL('highlighted(int)'), self.loadNK2)
        QtCore.QObject.connect(self.ui.nk2Location, QtCore.SIGNAL('currentIndexChanged(int)'), self.loadNK2)

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
        self.ui.nk2Location.insertItems(0, pathlist)
    
    
    def loadNK2(self, item=0):
        "Load an NK2 and display it"
        path = unicode(self.ui.nk2Location.currentText())
        print "path", path
        assert(os.path.exists(path))
        #del(self.nk2)
        self.nk2 = nk2parser.nk2bib(path)  # init the parser
        self.nk2.parse()                   # slurp the file
        #self.nk2.check()
        self.ui.parsedTable.clear() # zap the existing contents 
        self.ui.parsedTable.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem('Name'))
        self.ui.parsedTable.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem('Address'))
        self.ui.parsedTable.setRowCount(len(self.nk2.records) + 1) # expand table to keep all records
        i  = 0
        for rec in self.nk2.records:
            self.ui.parsedTable.setItem(i, 0, QtGui.QTableWidgetItem(rec.name))
            self.ui.parsedTable.setItem(i, 1, QtGui.QTableWidgetItem(rec.address))
            i += 1
        self.ui.parsedTable.resizeColumnsToContents()
    
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
        print 'Usage: %s [NK2 file] '% sys.argv[0]
        sys.exit()
    else:
        app = QtGui.QApplication(sys.argv)
        debunk2 = QtGui.QDialog()
        ui = debunker()
        ui.show()
        sys.exit(app.exec_())
