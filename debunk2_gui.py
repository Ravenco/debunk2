#!/usr/bin/python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2006-2007 - Håvard Dahle
#    <havard@dahle.no>
#
#    License: GPL2
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
    from PyQt4 import QtGui, QtCore
except ImportError:
    #grr. pyqt4 is not (properly) installed
    printerror("""You need PyQt4 to run this program
Try to run nk2parser.py directly for a non-gui version""")
    sys.exit(1)

try:
    import nk2parser, debunk2_ui, debunk2_ui_resources
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
XCARD=6  # XCARD, jabber variant http://www.xmpp.org/extensions/xep-0054.html
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
    elif format in (XCARD, ):
        return "xcard"
    elif format in (XML,):
        return "xml"
    elif format == VCARD:
        return "vcf"

class debunkerQT(QtGui.QDialog):
    
    nk2 = None
    startuppath = ''
    pathlist = []
    charset = 'iso-8859-1' # hold outlook in the hand. no utf8
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = debunk2_ui.Ui_debunk2()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.nk2Location, QtCore.SIGNAL('editTextChanged(QString)'), self.loadNK2)
        QtCore.QObject.connect(self, QtCore.SIGNAL('pathlistChanged'), self.loadNK2)
        
        QtCore.QObject.connect(self.ui.nk2Locator, QtCore.SIGNAL('clicked()'), self.addNK2)
        QtCore.QObject.connect(self.ui.export, QtCore.SIGNAL('clicked()'), self.exportNK2)
        QtCore.QObject.connect(self.ui.about, QtCore.SIGNAL('clicked()'), self.about)
        QtCore.QObject.connect(self.ui.exporthelp, QtCore.SIGNAL('clicked()'), self.exportFormatHelp)
        
        #icons
        self.ui.exporthelp.setIcon(QtGui.QIcon(":/info"))
        self.ui.about.setIcon(QtGui.QIcon(":/blocks"))

        ##self.ui.setAcceptDrops(True) # we want to be able to accept drag and drops
        #self.ui.parsedTable.dragEnterEvent = dragEnterEvent
        #self.ui.parsedTable.dropEvent = dropEvent
        #self.ui.parsedTable.dragMoveEvent = dragMoveEvent
        
        #self.ui.nk2Location.dragEnterEvent = dragEnterEvent
        #self.ui.nk2Location.dropEvent = dropEvent
        #self.ui.nk2Location.dragMoveEvent = dragMoveEvent
        
        # find startuppath (or something like it)
        locs = ['PWD', 'USERPROFILE', 'SYSTEMDRIVE']
        for v in locs:
            here = os.getenv(v)
            if here is not None:
                self.startuppath = here
                self.pathlist.append(here)
                break
        #print self.startuppath
        try:
            self.displayPaths(self.findNK2())
        except AssertionError:
            self.alert("The path list is nothing I can make sense of. What did you do?")
        
    def findNK2(self):
        "Look in the default places for an NK2 file. Returns list of found files"
        locations = []
        # find default locations of nk2 file
        appdata = os.getenv('APPDATA')
        if appdata is not None:
            self.pathlist += [os.path.join(appdata, 'Roaming', 'Microsoft', 'Outlook'), # vista file location 1
                              os.path.join(appdata, 'Local', 'Microsoft', 'Outlook'), # vista file location 2
                              os.path.join(appdata, 'Microsoft', 'Outlook')] # winxp, win2003 file location
        for p in self.pathlist: # look for .NK2 files in all paths, adding as we find
            locations += glob.glob(os.path.join(p, "*.[nN][kK]2")) # case INsensitive globbing for files
        return locations # return a list of nk2 files
    
    def displayPaths(self, pathlist):
        "Displays different paths in the combobox so the user can choose"
        assert(type(pathlist) == types.ListType)
        self.ui.nk2Location.clear()
        self.ui.nk2Location.insertItems(0, pathlist)
        self.emit(QtCore.SIGNAL('pathlistChanged'))
    
    def loadNK2(self, item=0):
        "Load an NK2 and display it"
        path = unicode(self.ui.nk2Location.currentText())
        #print "path", path
        assert(os.path.exists(path))
        assert(os.path.isfile(path))
        #del(self.nk2)
        self.nk2 = nk2parser.nk2bib(path)  # init the parser
        self.nk2.parse()                   # slurp the file
        #self.nk2.check()
        self.ui.parsedTable.clear() # zap the existing table 
        self.ui.parsedTable.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem('Name'))
        self.ui.parsedTable.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem('Address'))
        self.ui.parsedTable.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem('Organization'))
        self.ui.parsedTable.setRowCount(len(self.nk2.records)) # expand table to keep all records
        i  = 0
        for rec in self.nk2.records:
            self.ui.parsedTable.setItem(i, 0, QtGui.QTableWidgetItem(rec.name))
            self.ui.parsedTable.setItem(i, 1, QtGui.QTableWidgetItem(rec.address))
            org = rec.org[0].upper() + rec.org[1:]
            self.ui.parsedTable.setItem(i, 2, QtGui.QTableWidgetItem(org))
            i += 1
        self.ui.parsedTable.resizeColumnsToContents() # resize so it looks nice
        
    def exportNK2(self):
        format = None
        controls = { #CSV: self.ui.radioCSV,  ## comma is not suited as a separator
                     TSV: self.ui.radioTSV,
                     SSV: self.ui.radioSSV,
                     XCARD : self.ui.radioXCard,
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
        # make sure we got a valid file
        if not unicode(exportfile): return # cancelled
        ret = self.saveTable(unicode(exportfile), format)
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
        elif format in (XCARD, XML):
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
            name = unicode(self.ui.parsedTable.item(i, 0).text()).encode(self.charset)
            address = unicode(self.ui.parsedTable.item(i, 1).text()).encode(self.charset)
            file.write("'%s'%s%s\r\n" % (name, separator, address))
            #print "wrote '%s'%s%s" % (name, separator, address)
            i += 1
        file.close()
        
    def saveTableXml(self, file, format=XCARD):
        print "saveTableXml"
        #make sure the file is something we can write to
        if type(file) != types.FileType:
            #assert
            file = open(file, 'wb')
        assert(hasattr(file, 'write'))
        file.write('<?xml encoding="%s"?>\r\n' % self.charset)
        file.write('<!-- vCard in XML: http://www.xmpp.org/extensions/xep-0054.html -->\r\n')
        file.write('<xCard>\r\n')
        #loop thru the table
        #we're using the table (and not self.nk2) since the user 
        #may have made changes to the table data
        i = 0
        total = self.ui.parsedTable.rowCount()
        while i < total:
            file.write('  <vCard><VERSION>2.0</VERSION>\r\n')
            name = unicode(self.ui.parsedTable.item(i, 0).text()).encode(self.charset)
            file.write('    <FN>%s</FN>\r\n' % name)
            address = unicode(self.ui.parsedTable.item(i, 1).text()).encode(self.charset)
            file.write('    <EMAIL><INTERNET/><USERID>%s</USERID></EMAIL>\r\n' % address)
            org = unicode(self.ui.parsedTable.item(i, 2).text()).encode(self.charset)
            file.write('    <ORG><ORGNAME>%s</ORGNAME><ORGUNIT/></ORG>\r\n' % org)
            #file.write("<KEY><TYPE>x509</TYPE><CRED>%s</CRED></KEY>\r\n" % x509) #not supported yet
            
            file.write('  </vCard>\r\n')
            i += 1
        file.write('</xCard>\r\n')
        file.close()
        
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
            name = unicode(self.ui.parsedTable.item(i, 0).text()).encode(self.charset)
            file.write("FN;ENCODING=QUOTED-PRINTABLE;CHARSET=%s:%s\r\n" % (self.charset, quopri.encodestring(name)))
            address = unicode(self.ui.parsedTable.item(i, 1).text()).encode(self.charset)
            file.write("EMAIL;INTERNET;ENCODING=QUOTED-PRINTABLE;CHARSET=%s:%s\r\n" % (self.charset, quopri.encodestring(address)))
            org = unicode(self.ui.parsedTable.item(i, 2).text()).encode(self.charset)
            file.write("ORGANIZATION;ENCODING=QUOTED-PRINTABLE;CHARSET=%s:%s\r\n" % (self.charset, quopri.encodestring(org)))
            
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

Copyright (C) 2007 Håvard Gulldahl <havard@gulldahl.no>
http://code.google.com/p/debunk2/

The autocomplete (NK2) files store the name and email address (and more) of every outgoing e-mail sent in MS Outlook. This list of contacts is valuable data, but putting it to use is difficult since the file format is undocumented. By some tweaking, this program is able to read the name and addresses of ordinary email (SMTP) addressees.

As far as the author is aware, it does not loose data, but in certain cases (especially where non-English characters are involved) records may be skipped. Sorry. Sacrifice a chicken, then send me the file and I will fix it.

The program and source code of all elements in this program are fully available to anyone at any time, under the terms of the GPLv2 license.
http://www.gnu.org/copyleft/gpl.html

This program distributes binary versions of Python2.5, Qt 4.1 Open Source Edition and PyQt, all governed by the same license as debuNK2. Links to source code for all projects are available at http://code.google.com/p/debunk2/
""" % (nk2parser.__version__) )
        return ret

    def exportFormatHelp(self):
        "Display export format help"
        ret = QtGui.QMessageBox.information(self, 'debuNK2 export help',
u"""Choosing the right export format

All depending on what program you intend to peruse the contact info extracted from the NK2 file, different export formats are best suited.

OUTLOOK
If you intend to re-import the records to MS Outlook, your best shot is to 
1) Export as comma-separated values, import into MS Excel, and then import to MS Outlook
2) Export as vCard, import into Windows Address book, and then import to MS Outlook

# If you know of a better method, I'd love to hear from you! #

OTHER CLIENTS
Most other email clients should be able to import vCard files, which is less error-prone than the tab/semicolon-separated exports. In case they do not, experience suggests that semicolon is the best separator -- unless your records contain semicolons, of course.
""")
        return ret


def main(args):
    app = QtGui.QApplication(args)
    debunk2 = QtGui.QDialog()
    ui = debunkerQT()
    ui.show()
    sys.exit(app.exec_())

