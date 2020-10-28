#!/usr/bin/env python3

import os
import json
import re

def build_cnc_dict(month, bigCount):
	file_name = "/scratch/to2cu/http_logs/benign_domains_" + month + ".tsv"
	myList = set()
	listFile = open(file_name)
	inCount = 0
	for line in listFile:
		if "domain" not in line and "empty" not in line:
			ip = line.split("\t")[0]
			count = line.split("\t")[1].split("\n")[0]
			# print(ip)
			# print(count)
			if inCount <= bigCount:
				myList.add(ip)
				inCount = inCount + 1  
	return myList


def get_file(month):
	dir = "/scratch/hsk4p/http_labels/" + month
	for filename in os.listdir(dir):
		if filename.startswith("benign"):
			fileName = os.path.join(dir, filename)
			return fileName

def find_relevant_logs(month, afile, cnc_dict):
	print(cnc_dict)
	focusFile = open(afile)
	out_dir = "/scratch/hsk4p/http_labels/" + month
	print(out_dir)
	for line in focusFile:
		ip_dst = 0
		test = re.split(r'\s',line)
		test1 = test[0]
		test2 = test1.split("{")
		if len(test2) < 2:
			dummyVal = 1
		else:
			test3 = test2[1]
			test4 = test3.split('"')
			ip_dst = test4[15]
			ip = test4[17]
			# print(ip_dst + ": " + ip)
			if ip in cnc_dict:
				print ("IP {0} found!".format(ip))
				fileName = os.path.join(out_dir, "top_benign")
				outFile = open(fileName, "a+")
				outFile.write(line + '\n')
				outFile.close()

def main():
	months = ["dec"]
	for month in months:
		cnc_dict = build_cnc_dict(month, 100)
		http_file = get_file(month)
		find_relevant_logs(month, http_file, cnc_dict)


main()
