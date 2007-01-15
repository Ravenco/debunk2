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

import sys, types, os.path, os, glob, quopri

def printerror(errormsg):
    "Display an error message on the console and, if possible, on the gui"
    print errormsg
    guis = [ ['zenity', '--error', '--text', errormsg],
             ['kdialog', '--error', errormsg],
             #'gdialog': '--error "%s"', ### how does gdialog work?
             ['xmessage', '-center', errormsg],
             #'win32', '--er'  # how to do this on win32?
             #'macosx', '--er'  # how to do this on macosx?
           ]
    for g in guis:
        print g
        try:
            s = os.spawnvp(os.P_WAIT, g[0], g)
        except:
            #grr
            pass
        else:
            if s == 0: # dialog was shown, stop now
                break
try:
    from PyQt4 import QtCore, QtGui, uic
except ImportError:
    #grr. pyqt4 is not (properly) installed
    printerror("""You need pyqt4 to run this program
Try to run nk2parser.py directly for a non-gui version""")
    sys.exit(1)

try:
    import debunk2_ui, nk2parser
except ImportError:
    #grr. Something is severly wrong
    printerror("""Something is severely wrong. 
    
Couldn't load the rest of the program. Seek help.""")
    raise #show the real error

try:
    from xml.etree import ElementTree # py2exe needs this import statement
except ImportError:
    #oh oh. we're fucked
    print "You may have problems creating exe files. If you don't intend to do that, have a nice day"

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

#def dragEnterEvent(self, e):
    #print "enterevent"
    #e.acceptProposedAction()
    
#def dropEvent(self, e):
    #print "dropevent"
    #e.accept()
  
#def dragMoveEvent(self, event):
    #print "moveevent"
    #raise 'hei'
    #event.acceptProposedAction()

def fileExt(format):
    "Return file extension of supplied format"
    if format in (CSV, TSV, SSV):
        return "csv"
    elif format in (SYNCML, ):
        return "syncml"
    elif format in (XML,):
        return "xml"
    elif format == VCARD:
        return "vcf"


class debunker(QtGui.QDialog):
    
    nk2 = None
    startuppath = ''
    pathlist = []
    exportcharset = 'iso-8859-1' # we need to hold outlook in the hand. no utf8
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = debunk2_ui.Ui_debunk2()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.nk2Location, QtCore.SIGNAL('editTextChanged(QString)'), self.loadNK2)
        QtCore.QObject.connect(self, QtCore.SIGNAL('pathlistChanged'), self.loadNK2)
        
        QtCore.QObject.connect(self.ui.nk2Locator, QtCore.SIGNAL('clicked()'), self.addNK2)
        QtCore.QObject.connect(self.ui.export, QtCore.SIGNAL('clicked()'), self.exportNK2)
        QtCore.QObject.connect(self.ui.about, QtCore.SIGNAL('clicked()'), self.about)

        ##self.ui.setAcceptDrops(True) # we want to be able to accept drag and drops
        #self.ui.parsedTable.dragEnterEvent = dragEnterEvent
        #self.ui.parsedTable.dropEvent = dropEvent
        #self.ui.parsedTable.dragMoveEvent = dragMoveEvent
        
        #self.ui.nk2Location.dragEnterEvent = dragEnterEvent
        #self.ui.nk2Location.dropEvent = dropEvent
        #self.ui.nk2Location.dragMoveEvent = dragMoveEvent
        
        locs = ['USERPROFILE', 'PWD', 'SYSTEMDRIVE']
        for v in locs:
            here = os.getenv(v)
            if here is not None:
                self.startuppath = here
                self.pathlist.append(here)
                break
        #print self.startuppath
        self.displayPaths(self.findNK2())
        
    def findNK2(self):
        "Look in the default places for an NK2 file. Returns list of found files"
        locations = [] #XXX: TODO: Find default locations on win32
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
        self.ui.parsedTable.clear() # zap the existing table 
        self.ui.parsedTable.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem('Name'))
        self.ui.parsedTable.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem('Address'))
        self.ui.parsedTable.setRowCount(len(self.nk2.records)) # expand table to keep all records
        i  = 0
        for rec in self.nk2.records:
            self.ui.parsedTable.setItem(i, 0, QtGui.QTableWidgetItem(rec.name))
            self.ui.parsedTable.setItem(i, 1, QtGui.QTableWidgetItem(rec.address))
            i += 1
        self.ui.parsedTable.resizeColumnsToContents() # resize so it looks nice
        
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
        defaultpath = os.path.join(self.startuppath, 'outlook-export.%s' % fileExt(format))
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
            name = unicode(self.ui.parsedTable.item(i, 0).text()).encode(self.exportcharset)
            address = unicode(self.ui.parsedTable.item(i, 1).text()).encode(self.exportcharset)
            file.write("'%s'%s%s\r\n" % (name, separator, address))
            #print "wrote '%s'%s%s" % (name, separator, address)
            i += 1
        file.close()
        
    def saveTableXml(self, file, format=SYNCML):
        print "saveTableXml"
    
    def saveTableVCard(self, file):
        #http://www.imc.org/pdi/vcard-21.rtf
        print "saveTableVCard"
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
            file.write("BEGIN:VCARD\r\n") #Begin vcard
            file.write("VERSION:2.1\r\n") 
            name = unicode(self.ui.parsedTable.item(i, 0).text()).encode(self.exportcharset)
            file.write("FN;ENCODING=QUOTED-PRINTABLE;CHARSET=%s:%s\r\n" % (self.exportcharset, quopri.encodestring(name)))
            address = unicode(self.ui.parsedTable.item(i, 1).text()).encode(self.exportcharset)
            file.write("EMAIL;INTERNET;ENCODING=QUOTED-PRINTABLE;CHARSET=%s:%s\r\n" % (self.exportcharset,  quopri.encodestring(address)))
            
            #file.write("KEY;TYPE=X509:%s\r\n" x509) #not supported yet
            file.write("END:VCARD\r\n\r\n") #end vcard
            i += 1
        file.close()
        

    def info(self, text):
        ret = QtGui.QMessageBox.information(self, 'debuNK2 information', text)
        return ret

    def about(self):
        "Display about this program message"
        ret = QtGui.QMessageBox.information(self, 'About debuNK2 %s' % nk2parser.__version__,
u"""DebuNK2 version %s

DebuNK2 is a program to extract useful information from the autocomplete files of MS Outlook.

Copyright (C) 2007 Håvard Dahle <havard@dahle.no>
http://code.google.com/p/debunk2/

The autocomplete (NK2) files store the name and email address (and more) of every outgoing e-mail sent in MS Outlook. This list of contacts is valuable data, but putting it to use is difficult since the file format is undocumented. By some tweaking, this program is able to read the name and addresses of ordinary email (SMTP) addressees.

As far as the author is aware, it does not loose data, but in certain cases (especially where non-English characters are involved) records may be skipped. Sorry. Sacrifice a chicken, then send me the file and I will fix it.

The program and source code are fully available to anyone at any time, under the terms of the GPLv2 license.
http://www.gnu.org/copyleft/gpl.html
""" % (nk2parser.__version__) )
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
