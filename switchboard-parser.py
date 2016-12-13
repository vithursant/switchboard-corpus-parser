#!/usr/bin/env python3

import os

class ParseSB:
	def __init__(self):
		self.transcribed_files = []

	def walk_directory(self):
		all_transcribed_files = []
		for dirpath, dirnames, filenames in os.walk("."):
		    for filename in [f for f in filenames if f.endswith("-trans.text")]:
		    	#os.path.join(dirpath, filename)
		   		transcribed_files.append(os.path.abspath(filename))

		self.all_transcribed_files = transcribed_files


	def main(self):
		self.walk_directory()
		print (self.all_transcribed_files)