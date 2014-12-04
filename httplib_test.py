import httplib
import os

def httplib_read(host,url):
    url = "/"
    h = httplib.HTTPConnection(host, timeout=1)
    header = {"host":"www.baidu.com"}
    #h.putrequest(method='POST', url=url)
    #h.putheader("host", "www.baidu.com")
    h.request(method='POST', url=url, headers=header)
    res = h.getresponse()
    print res.read()


if __name__ == "__main__":
    host = "www.baidu.com"
    url = "/"
    httplib_read(host,url)
