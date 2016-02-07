# -*- coding: utf-8 -*-

import sys,json
from datetime import datetime

def main(argv):
	c = 0;
	errors=0
	i=1;sessionID=0;
	while i<11:
		aolfile = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL_userSessionQuery"+str(i)+".txt"
		writeFile = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL_sessionLine"+str(i)+".txt"
		oFile = open(writeFile, 'w')
		i+=1;
		c = 1
		prevSession = 0
		sessionLine = ""
		with open(aolfile) as infile:
			for line in infile:
				parts = line.split('\t')
				session = parts[1]
				query = str.strip(parts[2])
				if prevSession!=session:
					oFile.write(sessionLine+'\n')
					sessionLine = query
				else:
					sessionLine += (" "+query)
				prevSession = session
				c=c+1
				if c%100000 == 0:
					print c
					#break
			oFile.close()
		print ("Done with: ",aolfile)

	print c
	print errors
	oFile.close()

if __name__ == '__main__':
  main(sys.argv)