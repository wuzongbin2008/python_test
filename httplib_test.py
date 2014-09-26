import httplib
import os

def httplib_read(host,url):
    h = httplib.HTTPConnection(host, timeout=1)
    h.request(method='GET', url=url)
    res = h.getresponse()
    print res.read()


if __name__ == "__main__":
    host = "www.baidu.com"
    url = "/"
    httplib_read(host,url)
