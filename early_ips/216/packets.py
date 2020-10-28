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
	packets = {}
	responses = {}
	for row in csv_reader:
		line_count += 1
		pack = row[12]
		resp = row[13]
		if pack in packets:
			orig_pack = packets[pack]
			packets[pack] = orig_pack + 1
		else:
			packets[pack] = 1
		if resp in responses:
			orig_resp = responses[resp]
			responses[resp] = orig_resp + 1
		else:
			responses[resp] = 1
	print "Processed",line_count,"lines" 
	print packets
	print "There are",len(packets),"different packet values sent by originator"
	print "LINE BREAK"
	print responses
	print "There are",len(responses),"different packet values sent by responder" 
