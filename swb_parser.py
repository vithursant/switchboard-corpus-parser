#!/usr/bin/env python3

import os
import tqdm
from operator import itemgetter
import sys

class ParseSB:

	def __init__(self):
		self.transcribed_files = []
		self.file_pairs = []
		self.conversations = []

		self.SWB_LINES_FIELDS = ["speaker","start","end","dialogue"]

	def walk_directory(self):
		"""Traverses the current directory for transcribed switchboard files

	    Args:
	        None
	    Returns:
	        a list of transcribed switchboard data files
	    Raises:
	        None

	    """
		all_transcribed_files = []
		for dirpath, dirnames, filenames in os.walk("."):
		    for filename in [f for f in filenames if f.endswith("-trans.text")]:
		    	#os.path.join(dirpath, filename)
		    	#print (os.path.abspath(os.path.join(dirpath, filename)))
		    	all_transcribed_files.append((os.path.abspath(os.path.join(dirpath, filename))))

		self.transcribed_files = all_transcribed_files
		#print (self.transcribed_files)

	def grouper(self, n = 2):
		"""Pairs matching switchboard data files (i.e. Speaker A and Speaker B)

	    Args:
	        Number of files to group
	    Returns:
	        a generator object of paired Switchboard data files
	    Raises:
	        None

	    """
		for i in range(0, len(self.transcribed_files), 2):
			yield self.transcribed_files[i:i+n]

	def extract_fields(self, line):
		"""Creates a dictionary for each line of conversation

	    Args:
	        Line read from the Switchboard transcribed data file
	    Returns:
	        a list of dictionaries for each line
	    Raises:
	        None

	    """
		line = line.split(" ")
		line[3:len(line)] = [' '.join(line[3:len(line)])]

		#sys.exit()

		# Extract fields
		convObj = {}

		for i, field in enumerate(self.SWB_LINES_FIELDS):
			convObj[field] = line[i]
            #print (convObj_f1[field])
      	#print (convObj)
		self.conversations.append(convObj)

	def parse_swb_data(self):
		"""Parses the Switchboard data in A, B, A, B format

	    Args:
	        None
	    Returns:
	        None
	    Raises:
	        None

	    """
		pair = []
		#print (len(self.transcribed_files))
		for first, second in tqdm.tqdm(self.grouper(2)):
			pair.append(first)
			pair.append(second)
			self.file_pairs.append(pair)
			self.get_conversations(first, second)
			self.merge_conversations()
			self.conversations = []
			#sys.exit()
		#print len(self.file_pairs)

	def get_conversations(self, file1, file2):
		"""Get the conversations from the matching pairs of 
			Switchboard transcribed data

	    Args:
	        files 1 and file 2
	    Returns:
	        None
	    Raises:
	        None

	    """
		with open(file1) as f1, open(file2) as f2:
			for f1_line, f2_line in zip(f1, f2):
				self.extract_fields(f1_line)
				self.extract_fields(f2_line)

	def merge_conversations(self):
		"""Sort and merges the Speaker A and Speaker B transcribed data
			together.

	    Args:
	        None
	    Returns:
	        None
	    Raises:
	        None

	    """
		#self.conversations = sorted(self.conversations, key=itemgetter('end'))
		self.conversations = sorted(self.conversations, key=lambda k: float(k['end']))
		with open('merged_conversations.txt', 'a') as merge_file:
			merge_file.write('Start of Convo\n')

			for line in self.conversations:
				if 'A' in line.get('speaker'):
					speaker = 'A: '
				elif 'B' in line.get('speaker'):
					speaker = 'B: '

				merge_file.write(speaker + ' ' + line.get('end') + ' ' + line.get('dialogue'))
			merge_file.write('End of Convo\n')

	def main(self):
		self.walk_directory()
		self.parse_swb_data()

		