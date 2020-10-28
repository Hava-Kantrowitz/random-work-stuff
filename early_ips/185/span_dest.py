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
	dest_ips = {}
	for row in csv_reader:
		line_count += 1
		dest_ip = row[4]
		dest_ip = dest_ip[:3] 
		if dest_ip in dest_ips:
			orig_d_ip = dest_ips[dest_ip]
			dest_ips[dest_ip] = orig_d_ip + 1
		else:
			dest_ips[dest_ip] = 1
	print "Processed",line_count,"lines" 
	print dest_ips
	print "There are",len(dest_ips),"different ips"
	"""
	numGreater10 = 0
	for key in dest_ips:
		if dest_ips[key] >= 5:
			numGreater10 += 1
			print key
			print dest_ips[key]  
	print "There are",numGreater10,"lines greater than 5" 
	"""		   
