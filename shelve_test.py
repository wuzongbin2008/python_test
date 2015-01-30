import shelve

# sh = shelve.open('./data/shelve_test', 'c')
# sh['a'] = "aaaaa"
# sh['b'] = "bbbb"
# sh.close()
#
# sh = shelve.open('./data/shelve_test')
# del sh['a']
#sh.close()

sh = shelve.open('./data/shelve_test', 'r')
arr = sh.keys()
for k in arr:
    print k