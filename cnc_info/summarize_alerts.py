import os
import json
import operator
import numpy as np

FIREEYE_HTTP_LOG_DIR = '/scratch/to2cu/logs/fireeye_http/'
HTTP_LOG_DIR = "/scratch/hsk4p/dec/uva/all_days"
OUT_DIR = "../../results/fireeye_analysis/"
OUT_NAME = "alert_summary.csv"
os.makedirs(OUT_DIR, exist_ok=True)


def get_file_list(dir):
    fileList = []
    for filename in os.listdir(dir):
        fileList.append(os.path.join(dir, filename))
    return fileList


def analyze_logs(file_list, out_file):
    outFile = open(out_file, "w+", encoding='cp437')
    outFile.write('ip,port,total_count,url_count,internal_ip_count,requested_len_max,requested_len_min,requested_len_mean,'
                  'responded_len_max,responded_len_min,responded_len_mean,url_list,internal_ip_list\n')


    for afile in file_list:
        print ("Working on file {0}".format(afile))
        ip = afile.split('_')[-1]
        print ("Working on IP {0}".format(ip))
        focusFile = open(afile, encoding='cp437')
        line_count = 0
        internal_ips = {}
        urls = {}
        ports = {}
        anon_host_count = 0
        request_lens = []
        response_lens = []

        for line in focusFile:
            if '{' not in line:
                continue
            line_json = json.loads(line)
            internal_ip = line_json['id.orig_h']
            req_len = line_json['request_body_len']
            res_len = line_json['response_body_len']
            if 'host' in line_json:
                host = line_json['host']
            else:
                host = 'empty'
            if 'uri' in line_json:
                uri = line_json['uri']
            else:
                uri = '/empty'
            url = host + uri

            port = line_json['id.resp_p']
            if port not in ports:
                ports[port] = 0
            ports[port] += 1
            # if line_json['anon_host'] == 'none':
            #     anon_host_count += 1
            line_count += 1

            if url not in urls:
                urls[url] = 0
            urls[url] += 1
            if internal_ip not in internal_ips:
                internal_ips[internal_ip] = 0
            internal_ips[internal_ip] += 1
            request_lens.append(req_len)
            response_lens.append(res_len)

        urls_sorted = sorted(urls.items(), key=operator.itemgetter(1), reverse=True)[:100]
        internal_ips_sorted =  sorted(internal_ips.items(), key=operator.itemgetter(1), reverse=True)[:100]
        ports_sorted =  sorted(ports.items(), key=operator.itemgetter(1), reverse=True)

        urls = ""
        for url, count in urls_sorted:
            urls += url + ':' + str(count) + ';'
        int_ips = ""
        for ip, count in internal_ips_sorted:
            int_ips += ip + ':' + str(count) + ';'
        ports_str = ""
        for port, count in ports_sorted:
            ports_str += str(port) + ':' + str(count) + ';'

        line = str(ip)
        for elem in [ports_str, line_count, len(urls_sorted), len(internal_ips_sorted),
                np.max(request_lens), np.min(request_lens), np.mean(request_lens),
                np.max(response_lens), np.min(response_lens), np.mean(response_lens),
                urls, int_ips]:
            line += ',' + str(elem)

        outFile.write(line + '\n')
    outFile.close()
    print('File written:', out_file)



def main():
    file_list = get_file_list(FIREEYE_HTTP_LOG_DIR)
    analyze_logs(file_list, os.path.join(OUT_DIR, OUT_NAME))


main()
