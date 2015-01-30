import shelve

sh = shelve.open('./data/shelve_test', 'c')
sh['a'] = "aaaaa"
sh['b'] = "bbbb"
sh.close()

sh = shelve.open('./data/shelve_test')
del sh['a']
sh.close()

sh = shelve.open('./data/shelve_test')
for item in sh.items():
    print item