__author__ = 'wj'

a = True

def for_t():
    for i in range(1, 5):
        print i

def while_t():
    while not a:
        print "a is true"
    else:
        print "a is false"

def do_while():
    n = 1
    cnt = 5
    while n <= cnt:
        print n
        n += 1

def none_t():
    a = None
    if a:
        print "a is not None"
    else:
        print "a is None"

def range_t():
    for i in range(1):
        print i


s = "a"
t = "c"
b = s if t == "c" else "b"
print b