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
	outliers = 0
	dummy = 0
	dummy1 = 0
	dummy2 = 0
	for row in csv_reader:
		line_count += 1
		b_or = row[9]
		b_resp = row[10]
		if b_or == '0':
			dummy1 += 1
		elif b_or == '-':
			dummy2 += 1
		else:
			outliers += 1
			print "Original bytes is",b_or
			print "Conn state is",row[11]
			print "Source port is",row[3]
			print "Destination IP is",row[4]
			print "Destination port is",row[5]
		if b_resp == '0':
			dummy += 1
		elif b_resp == '-':
			dummy += 1
		else:
			outliers += 1
			print "Responder bytes is",b_resp
			print "Conn state is",row[11]
			print "Source port is",row[3]
			print "Destination IP is",row[4]
			print "Destination port is",row[5]
	print "Processed",line_count,"lines"
	if outliers == 0:
		print "No outliers in dataset"
