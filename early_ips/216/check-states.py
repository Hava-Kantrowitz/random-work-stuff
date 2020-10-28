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
	qclasses = {}
	qtypes = {}
	rcodes = {}
	aas = {}
	tcs = {}
	rds = {}
	ras = {}
	zs = {}
	rejs = {}
	for row in csv_reader:
		line_count += 1
		qclass = row[10]
		qtype = row[12]
		rcode = row[14]
		aa = row[15]
		tc = row[16]
		rd = row[17]
		ra = row[18]
		z = row[19]
		rej = row[20]
		if rcode in 'TC:false':
			rcode = "DNE"
			aa = row[13]
			tc = row[14]
			rd = row[15]
			ra = row[16]
			z = row[17]
			rej = row[18] 
		if qclass in qclasses:
			orig_qclass = qclasses[qclass]
			qclasses[qclass] = orig_qclass + 1
		else:
			qclasses[qclass] = 1
		if qtype in qtypes:
			orig_qtypes = qtypes[qtype]
			qtypes[qtype] = orig_qtypes + 1
		else:
			qtypes[qtype] = 1
		if rcode in rcodes:
			orig_rcode = rcodes[rcode]
			rcodes[rcode] = orig_rcode + 1
		else:
			rcodes[rcode] = 1
		if aa in aas:
			orig_aa = aas[aa]
			aas[aa] = orig_aa + 1
		else:
			aas[aa] = 1
		if tc in tcs:
			orig_tc = tcs[tc]
			tcs[tc] = orig_tc + 1
		else:
			tcs[tc] = 1
		if rd in rds:
			orig_rd = rds[rd]
			rds[rd] = orig_rd + 1
		else:
			rds[rd] = 1
		if ra in ras:
			orig_ra = ras[ra]
			ras[ra] = orig_ra + 1
		else: 
			ras[ra] = 1
		if z in zs:
			orig_z = zs[z]
			zs[z] = orig_z + 1
		else:
			zs[z] = 1
		if rej in rejs:	
			orig_rej = rejs[rej]
			rejs[rej] = orig_rej + 1
		else:
			rejs[rej] = 1
	print "Processed",line_count,"lines" 
	print "There are",len(qclasses),"different qclasses"
	print qclasses
	print "There are",len(qtypes),"different qtypes"
	print qtypes
	print "There are",len(rcodes),"different rcodes"
	print rcodes
	print "There are",len(aas),"different AAs"
	print aas
	print "There are",len(tcs),"different TCs"
	print tcs
	print "There are",len(rds),"different RDs"
	print rds
	print "There are",len(ras),"different RAs"
	print ras
	print "There are",len(zs),"different Zs"
	print zs
	print "There are",len(rejs),"different rejected states"
	print rejs
