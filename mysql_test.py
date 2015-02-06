import os
import logging
import threading
import MySQLdb
import MySQLdb.cursors

STORE_RESULT_MODE = 0
USE_RESULT_MODE = 1

FETCH_ONE = 0
FETCH_MANY = 1
FETCH_ALL = 2

host = "127.0.0.1"
port = "3307"
user = "root"
passwd = "sina@release&1"
db_name = "test"
table = "t"

total = 0
lock = threading.Lock()

class mysql_t(object) :
    def __init__(self):
        self.conn = MySQLdb.connect(host = host, user = user,\
                     passwd = passwd, db = db_name, \
                     port = int(port), cursorclass = MySQLdb.cursors.DictCursor,connect_timeout=30)

    def select(self):
        global lock,total

        k = "aa"
        v = "1211"
        #print "\nthread_name: %s" % threading.currentThread().getName()
        cur     = self.conn.cursor()
        sqlCmd  = "select * from %s WHERE k='%s'" %(table,k)
        #print "\nsqlCmd: %s" % sqlCmd
        #exit(0)
        ret = cur.execute(sqlCmd)
        row = cur.fetchone()
        print row

    def query(self,sqltext, mode=STORE_RESULT_MODE):
        if self.conn==None or self.conn.open==False :
            return -1
        self.conn.query(sqltext)
        if mode == 0 :
            result = self.conn.store_result()
        elif mode == 1 :
            result = self.conn.use_result()
        else :
            raise Exception("mode value is wrong.")
        return (self.conn.affected_rows(),result)

    def fetch_queryresult(self, result, maxrows=1, how=0, moreinfo=False):
            if result == None : return None
            dataset =  result.fetch_row(maxrows,how)
            if moreinfo is False :
                return dataset
            else :
                num_fields = result.num_fields()
                num_rows = result.num_rows()
                field_flags = result.field_flags()
                info = (num_fields,num_rows,field_flags)
                return (dataset,info)

    def fetch_rows(self):
        k = "aa"
        v = "1211"

        sqlCmd  = "select * from %s WHERE k='%s'" %(table,k)

        lines , res = self.query(sqlCmd)
        data = self.fetch_queryresult(res, maxrows=20, how=1, moreinfo=False)
        for r in data:
            print r

    def update(self):
        k = "aa"
        v = "1211"
        print "\nthread_name: %s" % threading.currentThread().getName()
        self.conn.autocommit(0)
        cur     = self.conn.cursor()
        sqlCmd  = "update %s set v='%s' WHERE k='%s'" %(table,v,k)
        print "\nsqlCmd: %s" % sqlCmd
        #exit(0)
        ret      = cur.execute(sqlCmd)
        print cur.fetchone()
        print "\nret: %s\n" % str(ret)
        self.conn.commit()

    def dump(self):
        cmd = "/usr/local/mysql-5.6.17/bin/mysql -NB -u'%s' -p'%s' -h'%s' -P'%s' -e\"select id,k,v from test.t \
        where length(k)>0 limit 100 \" > %s" % (user, passwd, host, port, "./data/mysql.test.t")

        print "dump cmd: %s" % cmd
        ret = os.system(cmd)
        print "dump ret: %s" % ret

    def mysql_thread(self):
        threads = []
        for i in range(100):
            worker = threading.Thread(target=self.select,name="Worker %d" % i)
            threads.append(worker)

        for i in range(100):
            threads[i].start()

        for i in range(100):
            threads[i].join()


if __name__ == "__main__":

    db = mysql_t()
    db.select()
    #print "total: %d"%total