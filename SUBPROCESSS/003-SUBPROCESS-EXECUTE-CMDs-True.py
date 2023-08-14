#!/usr/bin/python3.10
import subprocess
cmd="ls -lthr /home/satish/test"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()

print(f'The return code: {rc}')
print(f'The output :\n{out.splitlines()}')
print(f'The error :\n{err.splitlines()}')
