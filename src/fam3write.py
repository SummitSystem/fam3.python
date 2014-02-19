#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from ftplib import FTP
import tempfile

def fam3write(fam3, dev, val):

    f = tempfile.NamedTemporaryFile()
    f.write('{0}\n'.format(val))
    f.seek(0)

    user = os.environ.get('FAM3USER', 'anonymous')
    pwd =  os.environ.get('FAM3PASS', 'fam3@')

    ftp = FTP(fam3, user, pwd)

    url = '''STOR \VIRTUAL\CMD\F2DCSV_{0}_-1_0_2_1_0_1_1'''.format(dev)
    #print url
    ftp.storbinary(url, f)

    ftp.quit()
    f.close()

if __name__ == '__main__':
	argv = sys.argv
	argc = len(argv)

	if argc < 4:
		print '[usage] %s  fam3  device  value' % argv[0]
		quit()

	fam3write(argv[1], argv[2], argv[3])
