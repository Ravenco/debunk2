#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2007 - Håvard Dahle 
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################


from distutils.core import setup
#from setuptools import setup

import sys, os.path


setup(name="debunk2",
      version=0.1,
      description="Read MS Outlook autocomplete (NK2) files and extract email addresses",
      author='Håvard Dahle',
      author_email="havard@dahle.no",
      url="http://code.google.com/p/debunk2/",
      #packages=['finfaktura',],
      data_files=[#('share/finfaktura/pixmaps', ['pixmaps/error.png', 'pixmaps/warning.png']),
            ('share/debunk2/data', ['debunk2.ui', ]),
           ],
      scripts=["debunk2.py"],
      license="GPL2",
      long_description="""Microsoft Outlook stores its autocomplete email info in an undocumented file format. This project tries to unlock the information therein.""",
      #install_requires = ['docutils>=0.3', 'reportlab'],
      #zip_safe=True,
     )
