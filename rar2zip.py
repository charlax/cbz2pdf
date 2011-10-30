#!/usr/bin/python
# encoding: utf-8
"""
rar2zip.py

Created by Charles-Axel Dein on 2011-10-29.
Copyright (c) 2011 Charles-Axel Dein. All rights reserved.
"""

import sys
import os
import argparse
import zipfile
import tempfile
import logging

logging.basicConfig(level=logging.DEBUG)

def run_command(cmd):
	logging.info("running %s" % cmd)
	os.system(cmd)

# From Fabric http://docs.fabfile.org/
def confirm(question, default=True):
	"""Ask user a yes/no question and return their response as True or False.
	"""
	# Set up suffix
	if default:
		suffix = "Y/n"
	else:
		suffix = "y/N"
		
	# Loop till we get something we like
	while True:
		response = raw_input("%s [%s] " % (question, suffix)).lower()
		# Default
		if not response:
			return default
		if response in ['y', 'yes']:
			return True
		if response in ['n', 'no']:
			return False
		# Didn't get empty, yes or no, so complain and loop
		print("Please specify '(y)es' or '(n)o'.")

def main(args=None):
	for source_file in args.source_files:
		extract_folder = tempfile.mkdtemp(prefix='rar2zip')
		output_filename = os.path.splitext(source_file)[0] + "." + \
			args.extension
		
		if os.path.exists(output_filename):
			if confirm('Output file "%s" already exists. Do you want to overwrite it?' % output_filename, default=False):
				os.remove(output_filename)
			else:
				continue

		run_command('unrar -inul e "%s" %s' % (source_file,
			extract_folder))
		run_command('zip -jq -x Thumbs.db -r "%s" %s/*' %
			(output_filename, extract_folder))
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Convert rar files to \
		zip files')
	parser.add_argument('source_files', nargs="*", help='some rar files')
	parser.add_argument('-e', '--extension', default='zip', 
		help='file extension of the output')
	
	args = parser.parse_args()
	
	sys.exit(main(args))