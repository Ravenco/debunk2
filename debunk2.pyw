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

import sys

import debunk2_gui, nk2parser

if __name__ == "__main__":

    DEBUGLEVEL = sys.argv.count('-d')
    nk2parser.DEBUGLEVEL = DEBUGLEVEL

    if "-h" in sys.argv[1:]:
        print __doc__
        print 'Usage: %s [NK2 file] '% sys.argv[0]
        sys.exit()
    else:
        debunk2_gui.main(sys.argv)