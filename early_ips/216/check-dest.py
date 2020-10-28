#!/usr/bin/env python 

import csv 
import argparse 

print "Program running!"

parser = argparse.ArgumentParser(description='test')
parser.add_argument('file_name', help='Required file name')
args = parser.parse_args()

file_name = args.file_name
print "The file name is",file_name

with open(file_name) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	locs = {}
	for row in csv_reader:
		line_count += 1
		# Use 15 for location, 14 for loc source 
		loc = row[14]
		if loc in locs:
			orig_loc = locs[loc]
			locs[loc] = orig_loc + 1
		else:
			locs[loc] = 1	
	print "Processed",line_count,"lines" 
	print locs
	print "There are",len(locs),"different destination locations"
