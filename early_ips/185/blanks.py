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
	durations = {}
	bytes_or = {}
	bytes_resp = {}
	for row in csv_reader:
		line_count += 1
		dur = row[8]
		b_or = row[9]
		b_resp = row[10]
		if dur in durations:
			orig_dur = durations[dur]
			durations[dur] = orig_dur + 1
		else:
			durations[dur] = 1
		if b_or in bytes_or:
			orig_or = bytes_or[b_or]
			bytes_or[b_or] = orig_or + 1
		else:
			bytes_or[b_or] = 1
		if b_resp in bytes_resp:
			orig_resp = bytes_resp[b_resp]
			bytes_resp[b_resp] = orig_resp + 1
		else:
			bytes_resp[b_resp] = 1	
	print "Processed",line_count,"lines" 
	# print durations
	print "There are",len(durations),"different durations"
	print bytes_or
	print "There are",len(bytes_or),"different #s of orig bytes"
	print bytes_resp
	print "There are",len(bytes_resp),"different #s of resp bytes" 
	"""
	numGreater10 = 0
	for key in dest_ips:
		if dest_ips[key] >= 5:
			numGreater10 += 1
			print key
			print dest_ips[key]  
	print "There are",numGreater10,"lines greater than 5" 
	"""		   
