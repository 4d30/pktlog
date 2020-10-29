#!/usr/pkg/bin/python3.7

import sys
import subprocess
import psycopg2

try:
	conn = psycopg2.connect( dbname = "bge0db", user = "pgsql")
	cur = conn.cursor()
except:
	print("Unable to connect. Exiting.")
	sys.exit(0)

try:
	dump = subprocess.Popen(['tcpdump','-n','-s0','-c2048','-i','bge0'],
	    stdout=subprocess.PIPE)

except:
	print("Cannot open new process. Exiting.")
	sys.exit(0)

for bytes in dump.stdout:
	line = bytes.decode('utf8').strip()
	token = line.split(" ")
	if token[1] == "IP":
	    timestamp = token[0]
	    src = token[2].rpartition(".")
	    dst = token[4].rpartition(".")
	    srcaddr = src[0]
	    dstaddr = dst[0]
	    srcprt = src[2]
	    dstprt = dst[2][:-1]
	    if token[5] == "UDP,":
	        transport = "UDP"
	    else:
	        transport = "TCP"
	    if token[-1].isnumeric():
	        length = token[-1]
	    else:
	        print("Non-numeric packet length")
	        print(line)
	    cur.execute("INSERT INTO iptraffic \
	        (timestamp, srcaddr, srcprt, dstaddr, dstprt, transport, length) \
	        VALUES (%s, %s, %s, %s, %s, %s, %s)",
	        (timestamp, srcaddr, srcprt, dstaddr, dstprt, transport, length))

conn.commit()
cur.close()
conn.close()
