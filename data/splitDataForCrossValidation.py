#!/usr/bin/python
'''
this is used to preprocess default_of_credit_card_clients data so that it meets input requirement of svm_light
'''
import sys
import os
from pprint import pprint
import random

if len(sys.argv) < 4:
  sys.stderr.write("Usage: sourceDataFile resultFolder folderNum\n")
  sys.exit(1)

sourcePath = sys.argv[1]
resultFolderPath = sys.argv[2]
folderNum = int(sys.argv[3])
subSets = []
for i in range(0, folderNum):
  subSets.append([]);

#split the datasets into folderNum subsets
lineNum = 0
with open(sourcePath, "r") as sourceFd:
  for line in sourceFd: 
	lineNum += 1
	subSets[lineNum % folderNum].append(line)

#check resultFolder 
if not os.path.exists(resultFolderPath):
  os.makedirs(resultFolderPath)

for i in range(0, folderNum):
  trainFile = os.path.join(resultFolderPath, "train_{0}".format(i + 1))
  testFile = os.path.join(resultFolderPath, "test_{0}".format(i + 1))
  trainFd = open(trainFile, "w")
  testFd = open(testFile, "w")
  for subIndex, subset in enumerate(subSets):
	print "num of items in subset is {0}".format(len(subset))
	if subIndex == i:
	  testFd.write("".join(subset))
	else:
	  trainFd.write("".join(subset))
  trainFd.close()
  testFd.close()
