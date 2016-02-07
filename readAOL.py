# -*- coding: utf-8 -*-

import sys,json

def main(argv):
	c = 0;
	errors=0
	oFile = open('queryentity.txt', 'w')
	i=1
	while i<11:
		aolfile = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL"+str(i)+".txt"
		i+=1;
		c = 1
		with open(aolfile) as infile:
			for line in infile:
				#part2 = line.split('\t')[1]		
				c=c+1
				if c%100000 == 0:
					print c
		print ("Done with: ",aolfile)

	print c
	print errors
	oFile.close()

if __name__ == '__main__':
  main(sys.argv)