#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2006-2007 - Håvard Dahle
#    <havard@dahle.no>
#
#    Lisence: GPL2
#
# $Id: faktura.py 105 2006-12-24 01:00:17Z havard.dahle $
###########################################################################

__doc__ = """Export MS Outlook NK2 files into something readable by humans and machines (qt gui)
"""
import sys, types, os.path, os, glob
import qt, debunk2_ui, nk2parser

# constants
CSV=1  # comma-separated
TSV=2  # tab-separated
SSV=3  # semicolon-separated
XML=4  # 
VCARD=5  # vcard spec
SYNCML=6  # syncml
ODT=7  # OpenSpreadsheet 

class debunker(debunk2_ui.debunk2):
    
    nk2 = None
    pathlist = []
    
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        debunk2_ui.debunk2.__init__(self, parent, name, fl)
        self.connect(self.nk2Location, qt.SIGNAL('highlighted(int)'), self.loadNK2)

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
        self.nk2Location.clear()
        for z in pathlist: 
            self.nk2Location.insertItem(z)
    
    def loadNK2(self, item=0):
        "Load an NK2 and display it"
        path = unicode(self.nk2Location.currentText())
        print "path", path
        assert(os.path.exists(path))
        #del(self.nk2)
        self.nk2 = nk2parser.nk2bib(path)  # init the parser
        self.nk2.parse()                   # slurp the file
        self.parsedTable.setNumRows(len(self.nk2.records) + 1) # expand table to keep all records
        i  = 0
        for rec in self.nk2.records:
            self.parsedTable.setText(i, 0, rec.name)
            self.parsedTable.setText(i, 1, rec.address)
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
    else:
        a = qt.QApplication(sys.argv)
        qt.QObject.connect(a,qt.SIGNAL('lastWindowClosed()'),a,qt.SLOT('quit()'))
        d = debunker()
        a.setMainWidget(d)
        d.show()
        a.exec_loop()
