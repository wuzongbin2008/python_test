import os
import tarfile

def py_files(members):
    for tarinfo in members:
        if os.path.splitext(tarinfo.name)[1] == ".py":
            yield tarinfo

def lists(members):
    for tarinfo in members:
        print tarinfo


tar = tarfile.open("./log/replicate.log.BJ.2014-10-24.gz")
tar.extractall(members=lists(tar))
tar.close()