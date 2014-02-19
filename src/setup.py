# -*- coding: utf-8 -*- 

from distutils.core import setup
import py2exe

setup(console=['fam3read.py', 'fam3write.py', 'fam3add.py'])
'''
option = {
  "compressed"    :1,
  "optimize"      :2,
  "bundle_files"  :1
}

setup(
  options = {
    "py2exe": option
  },

  console = ['fam3read.py', 'fam3write.py', 'fam3add.py'],

  zipfile = None
)
'''
