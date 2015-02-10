import os
import sys


def run_cmd(cmd):
    try:
        import subprocess
    except ImportError:
        _, result_f, error_f = os.popen3(cmd)
    else:
        process = subprocess.Popen(cmd, shell = True,
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        result_f, error_f = process.stdout, process.stderr

    try:
        errors = error_f.read()
        if errors:  pass
        result_str = result_f.read().strip()
        if result_f :   result_f.close()
        if error_f  :    error_f.close()

        return result_str
    except Exception,e:
        print e


if __name__ == "__main__":
    cmd = "ll ./"
    ret = run_cmd(cmd)
    print ret