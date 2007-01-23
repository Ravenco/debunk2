#!/usr/bin/python
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

import sys, types, os.path, os, re, glob, quopri

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
    from Tkinter import *
    import tkMessageBox
except ImportError:
    #grr. pyqt4 is not (properly) installed
    printerror("""You need Tkinyrt to run this program
Try to run nk2parser.py directly for a non-gui version""")
    sys.exit(1)

try:
    import nk2parser
except ImportError:
    #grr. Something is severly wrong
    printerror("""Something is severely wrong. 
    
Couldn't load the rest of the program. Seek help.""")
    raise #show the real error

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

class debunker:

    pathlist = []
    startuppath = ''
    exportcharset = 'iso-8859-1' # hold outlook in the hand. no utf8

    def __init__(self, tkroot):
        self.root = tkroot
        self.pathlist = []
        self.startuppath = os.getcwd()

        #locatebutton
        self.locateButton = Button(self.root, command=self.locate, text='Locate NK2')
        self.locateButton.pack(anchor='ne')#, side='right')
        
        #pathbox
        self.path = StringVar()
        self.pathWidget = Entry(self.root, textvariable=self.path, width=60)
        self.pathWidget.pack(anchor='nw')#side='left')

        #displaybox
        self.list = Listbox(self.root, selectmode=EXTENDED, width=80)
        self.list.pack(expand=True, fill='y')

        #createbutton
        self.saveButton = Button(self.root, command=self.save, text='Export')
        self.saveButton.pack(side='right')
        
        #exportfile
        self.exportPath = StringVar()
        self.exportPathWidget = Entry(self.root, textvariable=self.exportPath, width=60)
        self.exportPath.set(os.path.join(self.startuppath, 'outlook-export.%s' % fileExt(VCARD)))
        self.exportPathWidget.pack()#side='left')
        
        #make
        self.start()

    def start(self):
        locs = ['USERPROFILE', 'SYSTEMDRIVE']
        for v in []: #locs:
            here = os.getenv(v)
            if here is not None:
                self.startuppath = here
                self.pathlist.append(here)
                break
        #print self.startuppath
        self.pathlist.append(self.startuppath)
        self.displayPaths(self.findNK2())
        self.loadNK2()
        
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
        self.path.set(str(pathlist[0]))
    
    def loadNK2(self, item=0):
        "Load an NK2 and display it"
        #path = unicode(self.ui.nk2Location.currentText())
        path = unicode(self.path.get())
        print "path", path
        assert(os.path.exists(path))
        assert(os.path.isfile(path))
        #del(self.nk2)
        self.nk2 = nk2parser.nk2bib(path)  # init the parser
        self.nk2.parse()                   # slurp the file
        #self.nk2.check()
        self.list.delete(0) # zap the existing table 
        i  = 0
        for rec in self.nk2.records:
            self.list.insert(END,
                             '%i %s' % (i, unicode(rec))
                             )
            i += 1
        #self.ui.parsedTable.resizeColumnsToContents() # resize so it looks nice

    def locate(self):
        print "locate"
        

    def save(self):
        f = open(self.exportPath.get(), 'wb')
        return self.saveTable(f, VCARD)

    def saveTable(self, fileobject, format=SSV):
        if format in (CSV, TSV, SSV):
            r = self.saveTableCharacterSeparated(fileobject, format)
        elif format in (SYNCML, XML):
            r = self.saveTableXml(fileobject, format)
        elif format == VCARD:
            r = self.saveTableVCard(fileobject)
        if r:
            tkMessageBox.showinfo(
                "debunk2",
                "Names and addresses have been written to %s" % self.exportPath.get()
            )
        else:
            tkMessageBox.showerror(
                "debunk2",
                "Something went wrong. "
            )
        
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
        return True
        
    def saveTableXml(self, file, format=SYNCML):
        print "saveTableXml"
        return False
    
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
        #total = self.ui.parsedTable.rowCount()
        for rec in self.list.get(0, END):
            file.write("BEGIN:VCARD\r\n") #Begin vcard
            file.write("VERSION:2.1\r\n")
            #a = rec.split()
            a = self.splitRow(rec)
            print a
            name = a[1]
            address = a[2]
            file.write("FN;ENCODING=QUOTED-PRINTABLE;CHARSET=%s:%s\r\n" % \
                (self.exportcharset, quopri.encodestring(name.encode(self.exportcharset))))
            file.write("EMAIL;INTERNET;ENCODING=QUOTED-PRINTABLE;CHARSET=%s:%s\r\n" %\
                (self.exportcharset, quopri.encodestring(address.encode(self.exportcharset)))) 
            
            #file.write("KEY;TYPE=X509:%s\r\n" x509) #not supported yet
            file.write("END:VCARD\r\n\r\n") #end vcard
            i += 1
        file.close()
        return True
        
    def splitRow(self, s):
        """Get a row: '1 "Contact Name" <contact@server.com>' and split the fields. Returns a tuple of three elements"""
        assert(type(s) in (types.StringType, types.UnicodeType))
        pat = re.compile('^(\d+)\s"([^"]+)"\s<([^>]+)>$')
        try:
            return pat.match(s.strip()).groups()
        except AttributeError:
            return None, None, None

class debunkerQT:#QtGui.QDialog):
    
    nk2 = None
    startuppath = ''
    pathlist = []
    
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
            name = unicode(self.ui.parsedTable.item(i, 0).text()).encode('utf8')
            address = unicode(self.ui.parsedTable.item(i, 1).text()).encode('utf8')
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
            name = unicode(self.ui.parsedTable.item(i, 0).text()).encode('utf8')
            file.write("FN;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:%s\r\n" % quopri.encodestring(name))
            address = unicode(self.ui.parsedTable.item(i, 1).text()).encode('utf8')
            file.write("EMAIL;INTERNET;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:%s\r\n" % quopri.encodestring(address))
            
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
    elif False:
        app = QtGui.QApplication(sys.argv)
        debunk2 = QtGui.QDialog()
        ui = debunker()
        ui.show()
        sys.exit(app.exec_())
    else:
        r = Tk()
        app = debunker(r)
        r.mainloop()
        
