import pycurl
import time
import hmac
import hashlib
import urllib
import datetime

DIP_SECRET_KEY = '961f134968494a8d90b2e5e46926bfc172bSDmLE'
DIP_ACCESS_KEY = 'hNnFsLXCF28292DFB490'
DIP_DOWN_URI = '/rest/v2/file/download_by_aliasname_new'
SECONDS_PER_DAY = 24*3600
RESULTS_PATH = './data/'

#for downloading result file
JOB_INFO = {
   ## job ID        :   job NAME
   '139711564584564' : 'distinct_uid_cnt',
   '139643157223635' : 'storage_size_wap',
   '139643162382860' : 'storage_size_web',
   '139643818224898' : 'top_uid_100',
   '139650412836387' : 'top_appid_100',
   '139650424950555' : 'top_client_ip_100',
   '139650653390898' : 'top_fid_100',
   #'139651467535728' : 'wap_amount_size_statistic',
   #'139651480239786' : 'web_amount_size_statistic',
   '142051668713799' : 'imgbed_weibo_upload_storage_size_count',
   '139651800502452' : 'size_distribution_statistic',
   '139652133868066' : 'upload_detail_wap',
   '139652150663511' : 'upload_detail_web',
   '139711813019434' : 'upload_detail_total'
}

JOB_NAME_LIST = JOB_INFO.values()
AMBITS = (20, 50, 100, 200, 500, 1024, 3072, 5120)

def get_yesterday() :
    time_str = time.localtime(time.time() - SECONDS_PER_DAY)
    yesterday = time.strftime('%Y-%m-%d', time_str)
    return yesterday

def dip_ssig(skey, sstr) :
    ''' sign alg of dip api '''
    hmc = hmac.new(skey, sstr, hashlib.sha1)
    ssig = hmc.digest().encode('base64')[5:15]
    return urllib.quote(ssig)

def dip_download(jobid, name, dfile) :
    ''' download file from dip '''
    timestamp = int(time.time())
    query = '%s/%s/%s?accesskey=%s&timestamp=%d' % (DIP_DOWN_URI, jobid, name,
            DIP_ACCESS_KEY, timestamp)
    sstr = "GET\n\n\n\n%s" % (query)
    ssig = dip_ssig(DIP_SECRET_KEY, sstr)
    url = 'http://api.dip.sina.com.cn%s&ssig=%s' % (query, ssig)

    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    curl.setopt(pycurl.WRITEFUNCTION , dfile.write)
    curl.perform()
    if int(curl.getinfo(pycurl.RESPONSE_CODE)) != 200 :
        raise Exception("download %s FAILED, return code: %s" % \
                (query, curl.getinfo(pycurl.RESPONSE_CODE)))

def download() :
    flag = True
    info = {}
    for key in JOB_INFO :
        job_id = key
        job_pre = JOB_INFO[key]
        result_file = RESULTS_PATH + job_pre + get_yesterday()
        job_name = datetime.date.today().strftime(job_pre+"_%Y%m%d")

        with open(result_file, 'w') as dfile :
            try :
                dip_download(job_id, job_name, dfile)
            except Exception, e :
                flag = False
                info[job_pre] = str(e)

    if flag is not True :
        raise Exception('download failed' + str(info))

def throw_ex():
    try:
        n = 10/0
    except Exception,e:
        raise "test"

if __name__ == "__main__" :
    try :
        download()
        throw_ex()
    except Exception, e :
        print str(e)