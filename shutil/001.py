#!/usr/bin/python3.10
import shutil
#copy, copy2, copyfile, copyfile, copyfileobj, copymode, copystat, copytree.
src="/root/PYTHON/shutil/sourcepath/1.txt"
dest="/root/PYTHON/shutil/destinationpath/1.txt"
shutil.copyfile(src,dest) #Doesn't preserve the permission use copy

src="/root/PYTHON/shutil/sourcepath/2.txt"
dest="/root/PYTHON/shutil/destinationpath/2.txt"
shutil.copy(src,dest) #Permission is preserved but timestamp will be different.

src="/root/PYTHON/shutil/sourcepath/3.txt"
dest="/root/PYTHON/shutil/destinationpath/3.txt"
shutil.copy2(src,dest) #Copy file to destination with same timestamp with same permission.


src="/root/PYTHON/shutil/sourcepath/4.log"          #should be present
dest="/root/PYTHON/shutil/destinationpath/4.log"    #should be present
shutil.copymode(src,dest) #Only permission will be assigned of src to dest but content will not be copied.

src="/root/PYTHON/shutil/sourcepath/5.log"
dest="/root/PYTHON/shutil/destinationpath/5.log"
shutil.copystat(src,dest) #only metadata will be copied not the content.

f1=open('/root/PYTHON/shutil/sourcepath/xyz.txt','r')
f2=open('/root/PYTHON/shutil/destinationpath/abc.txt','w')
shutil.copyfileobj(f1,f2) #will create abc.txt and copy metadata with content.

#src="/root/PYTHON/shutil/sourcepath"
#shutil.copytree(src,'/tmp/sourcepath')

shutil.rmtree('/tmp/sourcepath')
