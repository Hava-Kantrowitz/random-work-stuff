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
	sources = {}
	ports = {}
	for row in csv_reader:
		line_count += 1
		source = row[2]
		port = row[3]
		if source in sources:
			orig_source = sources[source]
			sources[source] = orig_source + 1
		else:
			sources[source] = 1
		if port in ports:
			orig_port = ports[port]
			ports[port] = orig_port + 1
		else:
			ports[port] = 1	
	print "Processed",line_count,"lines" 
	print sources
	print "There are",len(sources),"different source ips"
	print ports
	print "There are",len(ports),"different source ports"
	"""	
	num0to10 = 0
	num11to20 = 0
	num21to30 = 0
	hasGreater = 0
	for key in sources:
		if sources[key] <= 10:
			num0to10 += 1
		if sources[key] > 10 and sources[key] <= 20:
			num11to20 += 1
		if sources[key] > 20:
			num21to30 += 1
		if sources[key] > 30:
			hasGreater = 1	
	print "There are",num0to10,"sources with 1-10 originators"
	print "There are",num11to20,"sources with 11-20 originators"
	print "There are",num21to30,"sources with 21-30 originators"
	if hasGreater == 1:
		print "There are sources greater than 30 in here"  
	"""		   
