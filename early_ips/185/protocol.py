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
	protocols = {}
	for row in csv_reader:
		line_count += 1
		# 6 for protocols, 7 for service field
		prot = row[7]
		if prot in protocols:
			orig_prot = protocols[prot]
			protocols[prot] = orig_prot + 1
		else:
			protocols[prot] = 1	
	print "Processed",line_count,"lines" 
	print protocols
	print "There are",len(protocols),"different protocols"
	"""
	numGreater10 = 0
	for key in dest_ips:
		if dest_ips[key] >= 5:
			numGreater10 += 1
			print key
			print dest_ips[key]  
	print "There are",numGreater10,"lines greater than 5" 
	"""		   
