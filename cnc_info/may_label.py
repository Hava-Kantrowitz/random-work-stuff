import os
import json

CNC_LIST = "/scratch/hsk4p/fireye-months/may/uva/mayCncList.txt"
HTTP_LOG_DIR = "/scratch/hsk4p/fireye-months/may/uva"
OUT_DIR = "/scratch/hsk4p/fireye-months/may/labels"
os.makedirs(OUT_DIR, exist_ok=True)


def build_cnc_dict(file_name=CNC_LIST):
	myList = set()
	listFile = open(file_name)
	for line in listFile:
		a = line.split("'")
		if len(a) > 1:
			myList.add(a[1])
	return myList


def get_file_list(dir=HTTP_LOG_DIR):
	fileList = []
	for filename in os.listdir(dir):
		if filename.startswith("anon"):
			fileList.append(os.path.join(dir, filename))
	return fileList


def find_relevant_logs(file_list, cnc_dict):

	for afile in file_list:
		print ("Working on file {0}".format(afile))
		focusFile =  open(afile)
		for line in focusFile:
			line_json = json.loads(line)
			ip_dst = line_json["id.resp_h"]
			if ip_dst in cnc_dict:
				# print ("IP {0} found!".format(ip_dst))
				fileName = os.path.join(OUT_DIR, "mal_" + ip_dst)
				outFile = open(fileName, "a+")
				outFile.write(line + '\n')
				outFile.close()


def main():
	cnc_dict = build_cnc_dict()
	http_files = get_file_list()
	find_relevant_logs(http_files, cnc_dict)


main()
