import sys
import os
import platform
import subprocess

plat = platform.system()
scriptDir = sys.path[0]
hosts = os.path.join(scriptDir, 'ip.txt')
hostsFile = open(hosts, "r")
n=open("activeip.txt",'w')
lines = hostsFile.readlines()
if plat == "Linux":
    for line in lines:
        line = line.strip( )
        ping = subprocess.Popen(
            ["ping", "-c", "1", "-n", "-W", "2", line],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        out, error = ping.communicate()
        print out	
        print error
	if (ping.returncode==1):
	    print "inactive"
	elif(ping.returncode==0):
	    print line,"active"
	    n.write(line)
	    n.write("\n")

hostsFile.close()
