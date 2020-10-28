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
	uids = []
	for row in csv_reader:
		line_count += 1
		uid = row[1]
		uids.append(uid)
	print "Processed",line_count,"lines" 
	print uids
	print "There are",len(uids),"different ips"
			   
