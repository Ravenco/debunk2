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

INFO=1
WARNING=2
ERROR=3
QUESTION=4

class debunker(QtGui.QDialog):
    
    nk2 = None
    startuppath = None
    pathlist = []
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = debunk2_ui.Ui_debunk2()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.nk2Location, QtCore.SIGNAL('editTextChanged(QString)'), self.loadNK2)
        QtCore.QObject.connect(self, QtCore.SIGNAL('pathlistChanged'), self.loadNK2)
        
        QtCore.QObject.connect(self.ui.nk2Locator, QtCore.SIGNAL('clicked()'), self.addNK2)
        QtCore.QObject.connect(self.ui.export, QtCore.SIGNAL('clicked()'), self.exportNK2)

        here = os.getenv('PWD')
        if here is not None:
            self.startuppath = here
            self.pathlist.append(here)
        
        self.displayPaths(self.findNK2())
        
    def findNK2(self):
        "Look in the default places for an NK2 file. Returns list of found files"
        #return "test.NK2"
        locations = []
        for p in self.pathlist:
            locations += glob.glob(p+"/*.NK2")
            locations += glob.glob(p+"/*.nk2")
        return locations
    
    def displayPaths(self, pathlist):
        "Displays different paths in the combobox so the user can choose"
        assert(type(pathlist) == types.ListType)
        self.ui.nk2Location.clear()
        self.ui.nk2Location.insertItems(0, pathlist)
        self.emit(QtCore.SIGNAL('pathlistChanged'))
    
    def loadNK2(self, item=0):
        "Load an NK2 and display it"
        path = unicode(self.ui.nk2Location.currentText())
        print "path", path
        assert(os.path.exists(path))
        assert(os.path.isfile(path))
        #del(self.nk2)
        self.nk2 = nk2parser.nk2bib(path)  # init the parser
        self.nk2.parse()                   # slurp the file
        #self.nk2.check()
        self.ui.parsedTable.clear() # zap the existing contents 
        self.ui.parsedTable.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem('Name'))
        self.ui.parsedTable.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem('Address'))
        self.ui.parsedTable.setRowCount(len(self.nk2.records)) # expand table to keep all records
        i  = 0
        for rec in self.nk2.records:
            self.ui.parsedTable.setItem(i, 0, QtGui.QTableWidgetItem(rec.name))
            self.ui.parsedTable.setItem(i, 1, QtGui.QTableWidgetItem(rec.address))
            i += 1
        self.ui.parsedTable.resizeColumnsToContents()
        
    def exportNK2(self):
        format = None
        controls = { CSV: self.ui.radioCSV,
                     TSV: self.ui.radioTSV,
                     SSV: self.ui.radioSSV,
                     SYNCML : self.ui.radioSyncML,
                     VCARD : self.ui.radioVCard }
        for c in controls.keys():
            if controls[c].isChecked(): 
                format = c
                break
        print "format: ", format
        defaultpath = os.path.join(self.startuppath, 'outlook-export.csv')
        exportfile = QtGui.QFileDialog.getSaveFileName(self, 
                                           "Select file name for export",
                                           defaultpath)
                                           
        ret = self.saveTable(exportfile, format)
        self.info('Names and email addresses were written successfully to %s' % exportfile)
    
    def addNK2(self):
        nk2file = QtGui.QFileDialog.getOpenFileName(self,
                                              'Select your autocomplete file',
                                              self.startuppath,
                                              'Autocomplete files (*.NK2)')
        print "adding nk2:", nk2file
        pathlist = [nk2file,] + self.findNK2()
        self.displayPaths(pathlist)
        
    def saveTable(self, fileobject, format=SSV):
        if format in (CSV, TSV, SSV):
            return self.saveTableCharacterSeparated(fileobject, format)
        elif format in (SYNCML, XML):
            return self.saveTableXml(fileobject, format)
        elif format == VCARD:
            return self.saveTableVCard(fileobject)
        
    def saveTableCharacterSeparated(self, file, format):
        seps = { CSV:',',
                 TSV:'\t',
                 SSV:';' }
        separator = seps[format]
        print "charsep: --%s-- " % separator
        #make sure the file is something we can write to
        if type(file) != types.FileType:
            #assert
            file = open(file, 'wb')
        assert(hasattr(file, 'write'))
        
        #loop thru the table
        #we're using the table (and not self.nk2) since the user 
        #may have made changes to the table data
        i = 0
        total = self.ui.parsedTable.rowCount()
        while i < total:
            name = unicode(self.ui.parsedTable.item(i, 0).text()).encode('utf8')
            address = unicode(self.ui.parsedTable.item(i, 1).text()).encode('utf8')
            file.write("'%s'%s%s\r\n" % (name, separator, address))
            print "wrote '%s'%s%s" % (name, separator, address)
            i += 1
        file.close()
        
    def saveTableXml(self, file, format=SYNCML):
        print "saveTableXml"
    
    def saveTableVCard(self, file):
        print "saveTableVCard"

    def info(self, text):
        ret = QtGui.QMessageBox.information(self, 'debuNK2 information', text)
        return ret

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
