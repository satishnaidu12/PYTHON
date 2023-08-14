#!/usr/bin/python3.10
import subprocess
cmd="echo $HOME"
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()

print(f'The return code: {rc}')
print(f'The output :\n{out.splitlines()}')
print(f'The error :\n{err.splitlines()}')
