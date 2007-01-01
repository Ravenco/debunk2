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

__doc__ = """Parse MS Outlook NK2 files into something readable by humans and machines
"""

import types, sys, os.path

NUL='\x00'

DEBUGLEVEL=0

def isString(s):
    "True if it's a python or Unicode string"
    return type(s) in (types.StringType, types.UnicodeType)

class nk2bib:
    file = None
    filedata = None
    records = []
    
    def __init__(self, file):
        dbg(file)
        assert(isString(file))
        assert(os.path.exists(file))
        self.file = file
        f = open(file, 'rb')
        
        self.filedata = f.read()
        f.close()
        
    def parse(self):
        sep1 = '\x04H\xfe\x13' # record separator
        sep2 = '\x00\xdd\x01\x0fT\x02\x00\x00\x01'  # record separator
        
        continueSep = '\x81+\x1f\xa4\xbe\xa3\x10\x19\x9dn' #record continues
        stopSep = ('\xd2', '\xd3', '\xd4') #record stop words
        
        rec = None
        self.records = [] # reset list
        for z in self.filedata.split(sep1):
            for y in z.split(sep2):
                #dbg(y
        
                split1 = [x.replace(NUL, '') for x in y.split(NUL*3)] # SPLIT1: split record into something useful by separating at triple NULs
                dbg(split1, 2)
                
                rec = nk2addr() 
                if split1[1] != 'SMTP': # SPLIT1 failed
                    split2 = [x.replace(NUL, '') for x in y.split(NUL*1)] # SPLIT2: split again, this time using single NULs as delimiter
                    split1 = split2[1:] # adapt (hack) the list so the SPLIT2 fields have the same order and structure as SPLIT1
                    split1[0] = ' ' + split1[0] # more hacking of SPLIT2
                    dbg(split1, 2)
                
                rec._type = split1[1]
                if rec._type != 'SMTP': 
                    dbg(y, 2)
                    continue # couldn't find any email address in this record
                rec.setAddress(split1[2])
                rec.setName(unicode(split1[0][1:], "latin1"))
                self.addRecord(rec)
                #self.records.append(rec)
    
    def addRecord(self, rec):
        "Add an nk2 record to the internal list of records"
        assert(isinstance(rec, nk2addr))
        #weed out byte by byte duplicates
        if self.findRecord(rec.address): return
        self.records.append(rec)
    
    def prn(self):
        for z in self.records: print z.__str__().encode('utf8')

    def findRecord(self, address):
        for rec in self.records:
            if rec.address == address: return rec
        return False

    def csv(self):
        for z in self.records:
            if z.address:
                print z.fieldSeparatedValues(u";")

class nk2addr:
    
    name = u'' # pretty-printable name
    charset = None # charset of name
    address = u'' # email address
    
    _type = None # SMTP or xxx
    domaincheck = False
    _origlines = []
    _data = []
    
    def __init__(self):
        self.name = u''
        self.address = u''
    
    def parseFirstLine(self, b):
        self._origlines.append(b)
        B = self.strp(b)
        i = B.find('\x03\x15')
        dbg(B, 2)
        assert(i > 0)
        self.setAddress(B[1:i])
        dbg("Record found: %s" % self.address, 1)
    
    def parseLine(self, b):
        "parse a record full of hodge-podge bytes and email data and try to make some sense of it"
        self._origlines.append(b)
        #[f.replace(n, '') for f in c.split(n*3)]
        r = [self.strp(z) for z in b.split(NUL*3)]
        dbg(r, 2)
        self._data.append(r)
        try:
            self.setName(unicode(r[0][1:], 'latin1'))
        except:
            
            print "BONK!",repr(r[0])
            raise
        self._type = r[1]
        
    def setName(self, name):
        assert(isString(name))
        #name = name.strip()
        self.name = self.strpApos(name)
    
    def setAddress(self, address):
        assert(isString(address), "supplied argument is not a valid email address")
        a = u''
        for z in address:
            #dbg(ord(z), 1)
            if ord(z) < 20 or ord(z) > 128:
                break
            a += z
        self.address = self.strpApos(a)
    
    def strp(self, s):
        "Return string stripped of NUL bytes and unprintable characters"
        return s.replace(NUL, '')#.replace('\x00', '')

    def strpApos(self, s):
        if len(s) == 0: 
            return None
        for apo in ('"', "'"):
            if s[0] == apo and s[-1] == apo:
                s = s[1:-1] # remove apostrophes
                dbg("strng is now %s" % s, 1)
        return s
        
    
    def fieldSeparatedValues(self, fieldsep=u';'):
        "Return record fields separated by fieldsep. Ideal for import into some other program"
        self.sep = fieldsep
        try:
            return u'%(address)s%(sep)s%(name)s' % (dict(vars(self))) #vars(self)
        except:
            dbg(vars)
            dbg(self.address)
            raise
    
    def __str__(self):
        if self.address is None: return u''
        #try:
            #return u'"%s" <%s>' % (self.name, self.address) #'"%(name)s" <%(address)s>' % vars(self)
        #except:
            #print "KKA", type(self.address), repr(self.address)
            #raise
        try:
            return u'"%(name)s" <%(address)s>' %  {'name':self.name, 'address':self.address} #vars(self)
        except: 
            print self.name
            print vars(self)
            raise


def dbg(s, level=0):
    if level <= DEBUGLEVEL:
        print "[nk2parser]:",repr(s)


if __name__ == '__main__':
    DEBUGLEVEL = sys.argv.count('-d')
    assert(os.path.exists(sys.argv[1]))
    nk2 = nk2bib(sys.argv[1])
    nk2.parse()
    nk2.prn()
    #for z in nk2.walk():
        #print repr(z)
        ##print z
        #print '++'
        