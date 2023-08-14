#!/usr/bin/python3.10
import subprocess
cmd="ls -lthr /home/satish/testtttt"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
rc=sp.wait()
out,err=sp.communicate()

print(f'The return code: {rc}')
print(f'The output :\n{out}')
print(f'The error :\n{err}')
