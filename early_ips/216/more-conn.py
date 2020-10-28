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
	states_blank = {}
	states_zero = {}
	for row in csv_reader:
		line_count += 1
		resp_bytes = row[10]
		state = row[11]
		if resp_bytes == '-': 
			if state in states_blank:
				orig_state = states_blank[state]
				states_blank[state] = orig_state + 1
			else:
				states_blank[state] = 1
		if resp_bytes == '0':
			if state in states_zero:
				orig_state = states_zero[state]
				states_zero[state] = orig_state + 1
			else:
				states_zero[state] = 1	
	print "Processed",line_count,"lines" 
	print states_blank
	print "There are",len(states_blank),"different conn states with resp bytes -"
	print states_zero
	print "There are",len(states_zero),"different conn states with resp bytes 0" 
