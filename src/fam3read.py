#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from ftplib import FTP

def fam3read(fam3, dev, num):

	user = os.environ.get('FAM3USER', 'anonymous')
	pwd =  os.environ.get('FAM3PASS', 'fam3@')

	ftp = FTP(fam3, user, pwd)

	url = '''RETR \VIRTUAL\CMD\D2FCSV_{0}_2_{1}_0_0_0_1_1_{1}'''.format(dev,num)
	ftp.retrbinary(url, sys.stdout.write)

	ftp.quit()

if __name__ == '__main__':
	argv = sys.argv
	argc = len(argv)

	if argc < 3:
		print '[usage] %s  fam3  device  [num=1]' % argv[0]
		quit()

	fam3 = argv[1]
	dev = argv[2]
	num = argv[3] if 3 < argc else 1

	fam3read(fam3, dev, num)
