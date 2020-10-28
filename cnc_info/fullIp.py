#!/usr/bin/env python3

import pandas as pd 
import csv
import os
import argparse

parser = argparse.ArgumentParser(description='args')
parser.add_argument('file_name', help="Required file name")
args = parser.parse_args()

file_name = args.file_name

myList = []
listFile = open(file_name)
listData = listFile.readlines()
listFile.close()
fileList = []

# print(listData[0]) 
aList = listData[0].split(",")
# print (aList) 
# if december, use "'" as split
# Code for december: 
for val in aList:
	a = val.split("'")
	if len(a) > 1:
	 	myList.append(a[1])

# print(myList) 

ipList = []
fullIpList = []

numbers = '0123456789'
for val in myList: 
	if any(val.startswith(x) for x in numbers):
		fullIpList.append(val)
	else:
		ipList.append(val)

# print(ipList) 
requestList = []
for val in ipList:
	query = "nslookup " + val
	request = os.popen(query).read()  
	requestList.append(request)

# print(requestList) 
goodRequestList = []
notFound = 0
for val in requestList:
	if "NXDOMAIN" in val:
		notFound = notFound + 1
	elif "SERVFAIL" in val: 
		notFound = notFound + 1
	elif "connection timed out" in val:
		notFound = notFound + 1
	elif "No answer" in val:
		notFound = notFound + 1
	else:
		val = val.split("\n")
		likelyAdr = 5
		address = val[likelyAdr]
		while "Address" not in address:
			likelyAdr = likelyAdr + 1
			address = val[likelyAdr]
		address = address.split(":") 
		address = address[1]
		address = address.split(" ")
		address = address[1]
		fullIpList.append(address)

print (fullIpList)

