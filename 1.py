import re
import sys
import time
import pyping
import threading
import subprocess
import os
with open("MOCK_DATA.txt") as i:
    #i=open("ad.txt")
    x=[]
    for l in i:
        l=l.strip()
        y=re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",l)
        x.extend(y)
    print x
#for a in x:
p=open("ip.txt",'w')
for a in x:
    p.write(a)
    p.write("\n")
p.close()

