# -*- coding: utf-8 -*-

import sys,json
from datetime import datetime
import numpy
import math

def main(argv):
	c = 0;
	errors=0
	i=1;sessionID=0;
	words = []
	wordFile = "tasks.txt"
	with open(wordFile) as infile:
			for line in infile:
				word = line
				words.append(str.strip(word))
	nWords = len(words)
	counts = numpy.zeros((nWords,nWords))
	nS=0
	while i<11:
		aolfile = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL_sessionLine"+str(i)+".txt"
		i+=1;
		c = 1

		with open(aolfile) as infile:
			for line in infile:
				nS+=1
				ii=0
				temp = []
				for w in words:
					if w in line:
						#counts[ii][ii]+=1
						temp.append(1)
						#print (w,line,1)
					else:
						temp.append(0)
						#print (w,line,0)
					ii+=1
				ii=0
				for w in words:
					if temp[ii]==1:
						jj=0
						for w1 in words:
							if temp[jj]==1:
								counts[ii][jj]+=1
							jj+=1
					ii+=1
				#print line
				c=c+1
				if c%100000 == 0:
					print c
					#break

		print ("Done with: ",aolfile)
	print counts
	print "computing the task coherence metric now..."
	pmiN=0;pmiD=0
	ii=0
	for w1 in words:
		jj=0
		for w2 in words:
			if w1==w2:
				continue
			den = counts[ii][ii]*counts[jj][jj]
			if den == 0:
				den = 1
			tt = (counts[ii][jj]*nS)/den
			if tt==0:
				tt=1
			tt = math.log(tt,2)
			pmiN+=tt
			pmiD+=1
			print (w1,w2,tt)
			jj+=1
		ii+=1

	pmi = pmiN/pmiD
	print ("nS = ",nS)
	print ("final pmi score: ",pmi)
	print c
	print errors
	

if __name__ == '__main__':
  main(sys.argv)