# -*- coding: utf-8 -*-

import sys,json
from datetime import datetime

def main(argv):
	c = 0;
	errors=0
	i=2;sessionID=0;
	while i<11:
		aolfile = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL"+str(i)+".txt"
		writeFile = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL_userSessionQuery"+str(i)+".txt"
		oFile = open(writeFile, 'w')
		i+=1;
		c = 1
		prevTime = "2004-03-22 21:52:45"
		prevTime = datetime.strptime(prevTime, "%Y-%m-%d %H:%M:%S") 
		prevUser = str(1)
		nUsers = 0
		with open(aolfile) as infile:
			for line in infile:
				if c==1:
					c+=1
					continue
				#try:
				parts = line.split('\t')
				user = parts[0]
				query = parts[1]
				time = str.strip(parts[2])
				time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S") 
				diff = time - prevTime
				diffm = (diff.seconds/60)
				session = sessionID
				if diffm > 100 or prevUser!=user:
					session = sessionID+1
					sessionID+=1
				if prevUser!=user:
					nUsers+=1
				line1 = user +"\t"+str(session)+"\t"+query
				oFile.write(line1+'\n')
				
				prevTime = time
				prevUser = user
				#except:
					#print "error: "
					#print line
					#errors += 1
				c=c+1
				if c%100000 == 0:
					print c
					#break
			oFile.close()
		print ("Done with: ",aolfile)
		print ("no of users: ",nUsers)

	print c
	print errors
	oFile.close()

if __name__ == '__main__':
  main(sys.argv)