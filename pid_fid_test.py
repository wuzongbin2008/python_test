import hashlib

def gen_fid(checksum, size) :
    #check_cs_size(checksum, size)

    return "%s%08x" % (checksum,size)

def parse_fid():
    fid = '97e79e60f1af1a9f4572cc63ddac556600000090'
    md5 = fid[0:32]
    size = int(fid[32:40],16)
    print "md5: %s\nsize: %d\n" % (md5,size)
    return md5,size

def base62_decode(str):
    BASE_LIST = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    BASE_DICT = dict((c, v) for v, c in enumerate(BASE_LIST))
    BASE_LEN = len(BASE_LIST)

    num = 0
    for char in str :
        num = num * BASE_LEN + BASE_DICT[char]
    return num

def base62_encode(num):
    BASE_LIST = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    BASE_DICT = dict((c, v) for v, c in enumerate(BASE_LIST))
    BASE_LEN = len(BASE_LIST)

    if not num:
        return BASE_LIST[0]

    encoding = ""
    while num:
        num, rem = divmod(num, BASE_LEN)
        encoding += BASE_LIST[rem]
    return reduce(lambda x, y : y + x, encoding)

def get_uid_from_pid(pid) :
    if pid[9] == 'w' :
        if len(pid) >= 32 and pid[22] > '2' :
            return base62_decode(pid[0:8]);
        return int(pid[0:8], 16)
    else :
         base62_decode(pid[0:8])

def get_pid_dbinfo():
    pid = "005M5HiJgw1ep4dkx85r2j30go17s7hdt"
    uid = "%08x" % get_uid_from_pid(pid)
    hv = hashlib.md5(uid[0:8]).hexdigest()
    db_index = int(hv[0],16) % 4
    table = "tb_picidx_0%s" % hv[1]
    print "pid len: %d \ntable: %s \ndbno: %d"  % (len(pid),table,db_index)

def get_fid_dbinfo() :
    """ get host idx & table name of fid index """
    fid = '10f036b38011e68d46e2c287c7ac7aa500005a1d'
    #fid = '6d76e04910761522cf4c41cb77ba98fc000527b1'
    db_index = int(fid[0], 16) % 4
    table = "tb_fididx_0%s" % fid[1]
    dbno = db_index
    table = table
    print "\nlen: %d \ntable: %s \ndbno: %d"  % (len(fid),table,db_index)

def get_table_by_fid():
    fid = "160ca6250a554fe9ca1c55e7fceebd2a000efa98"
    print int(fid[0],16) % 4
    print "tb_fididx_0%s" % fid[1]

def gen_pic_dir():
    """ generate the path of pic on disk array
    Argument:
        store_id: eg: /data1
        fid = checksum + size, checksum is md5(file contents)
    """
    store_id = "data10"
    fid = "05a2434b426397566a80ffaee05fbdd9000059fe"
    size = 23038
    checksum = '05a2434b426397566a80ffaee05fbdd9'
    fid2= gen_fid(checksum,size)
    print "fid1: %s\nfid2: %s" % (fid,fid2)

    DISK_ARRAY_PREFIX = '/weibo_img/'

    prefix = fid[0:2]
    suffix = fid[2:4]
    print "prefix: %s\nsuffix: %s\n" %(prefix,suffix)
    first_dir = int(prefix,16)
    second_dir = int(suffix,16)
    print "first_dir: %s\nsecond_dir: %s\n" %(first_dir,second_dir)
    hash_dir = "/%03d/%03d/" % (first_dir,second_dir)
    path = "%s%s%s" % (DISK_ARRAY_PREFIX, store_id, hash_dir)
    #print path
    print hash_dir
    return (path, hash_dir)


if __name__ == "__main__":
    get_pid_dbinfo()