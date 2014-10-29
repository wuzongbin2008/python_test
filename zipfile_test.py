import zipfile

filename = "./log/replicate.log.BJ.2014-10-23.gz"
z = zipfile.ZipFile(filename, 'r')

print z.read(z.namelist()[0])
