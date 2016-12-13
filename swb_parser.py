#!/usr/bin/env python3

import os
from itertools import izip

class ParseSB:

	def __init__(self):
		self.transcribed_files = []
		self.file_pairs = []

	def walk_directory(self):
		all_transcribed_files = []
		for dirpath, dirnames, filenames in os.walk("."):
		    for filename in [f for f in filenames if f.endswith("-trans.text")]:
		    	#os.path.join(dirpath, filename)
		   		all_transcribed_files.append(os.path.abspath(filename))

		self.transcribed_files = all_transcribed_files
		#print (self.transcribed_files)

	def grouper(self, n = 2):
		for i in xrange(0, len(self.transcribed_files), 2):
			yield self.transcribed_files[i:i+n]

	def match_files(self, n = 2):
		pair = []
		print (len(self.transcribed_files))
		for first, second in self.grouper(n):
			pair.append(first)
			pair.append(second)
			self.file_pairs.append(pair)

		print len(self.file_pairs)

	def get_conversations(self):
		for file_pair in self.file_pairs:
			for file in enumerate(file_pair):
				with open("textfile1") as textfile1:
					

	def main(self):
		self.walk_directory()
		self.match_files()

		