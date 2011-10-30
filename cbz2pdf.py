#!/usr/bin/python
# encoding: utf-8
"""
cbz2pdf.py

Created by Charles-Axel Dein on 2011-10-29.
Copyright (c) 2011 Charles-Axel Dein. All rights reserved.
"""

import sys
import os
import argparse
import zipfile
import tempfile
import logging

logging.basicConfig(level=logging.ERROR)

def run_command(cmd):
	logging.info("running %s" % cmd)
	os.system(cmd)

def main(args=None):
	for source_file in args.source_files:
		extract_folder = tempfile.mkdtemp(prefix='cbz2pdf')
		output_filename = os.path.splitext(source_file)[0] + ".pdf"
	
		logging.info('extracting "%s"' % source_file)
		with zipfile.ZipFile(source_file, 'r') as z:
			z.extractall(extract_folder)
			z.close()
		
		print 'Creating "%s"...' % output_filename
		run_command('convert %s/*.jpg "%s"' % (extract_folder, output_filename))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Convert a cbz file to a pdf')
	parser.add_argument('source_files', help='cbz files', nargs="*")

	args = parser.parse_args()
	
	sys.exit(main(args))