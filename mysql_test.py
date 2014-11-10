import os
import logging
import threading
import MySQLdb
import MySQLdb.cursors

host = "127.0.0.1"
port = "3307"
user = "root"
passwd = "sina@release&1"
db_name = "test"
table = "t"

def select():
    k = "aa"
    v = "1211"
    print "\nthread_name: %s" % threading.currentThread().getName()
    conn = MySQLdb.connect(host = host, user = user,\
                 passwd = passwd, db = db_name, \
                 port = int(port), cursorclass = MySQLdb.cursors.DictCursor)

    cur     = conn.cursor()
    sqlCmd  = "select * from %s WHERE k='%s'" %(table,k)
    print "\nsqlCmd: %s" % sqlCmd
    #exit(0)
    ret = cur.execute(sqlCmd)
    row = cur.fetchone()
    print "ret: %s\n" % str(row)

def update():
    k = "aa"
    v = "1211"

    conn = MySQLdb.connect(host = host, user = user,\
                 passwd = passwd, db = db_name, \
                 port = int(port), cursorclass = MySQLdb.cursors.DictCursor)
    conn.autocommit(0)
    cur     = conn.cursor()
    sqlCmd  = "update %s set v='%s' WHERE k='%s'" %(table,v,k)
    print "update_storeid_by_gfid sqlCmd: %s" % sqlCmd
    #exit(0)
    ret      = cur.execute(sqlCmd)
    print cur.fetchone()
    print "ret: %s" % str(ret)
    conn.commit()

def dump():
    cmd = "/usr/local/mysql-5.6.17/bin/mysql -NB -u'%s' -p'%s' -h'%s' -P'%s' -e\"select k,v from test.t limit 1 \" > %s" % (user, passwd, host, port, "./mysql_t")
    #cmd = "/usr/local/mysql-5.6.17/bin/mysql -NB -u%s -p%s -h %s -P %s -e\"select k,v from t limit 1\" > %s" % (user, passwd, host, port, "./data/mysql_t")
    print cmd
    ret = os.system(cmd)

def get_table_by_fid():
    fid = "160ca6250a554fe9ca1c55e7fceebd2a000efa98"
    print int(fid[0],16) % 4
    print "tb_fididx_0%s" % fid[1]

def mysql_thread():
    threads = []
    for i in range(100):
        worker = threading.Thread(target=select,name="Worker %d" % i)
        threads.append(worker)

    for i in range(100):
        threads[i].start()

    # for i in range(100):
    #     threads[i].join()


if __name__ == "__main__":
    mysql_thread()
    print "main done"