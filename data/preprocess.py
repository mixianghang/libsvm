#!/usr/bin/python
'''
this is used to preprocess default_of_credit_card_clients data so that it meets input requirement of svm_light
'''
import sys
import os
from pprint import pprint

def formatSourceLine(sourceLine):
  if sourceLine[-2:] == "\r\n":
	sourceLine = sourceLine[:-2]
  elif sourceLine[-1] == "\n":
	print "nhao"
	sourceLine = sourceLine[:-1]
  attrs = sourceLine.split(",")
  #pprint(attrs)
  if len(attrs) != 25:
	sys.stderr.write("there are only {0} attributes in line\n".format(len(attrs)))
	print attrs
	return None
  formatAttrs = []
  if int(attrs[24]) == 0:
	attrs[24] = "-1"
  formatAttrs.append(attrs[24])
  index = 0
  attrNum = 1
  for index in range(1,24):
	if index >= 2 and index <= 4:#gender
	  if attrs[index] == "1":
		formatAttrs.append("{0}:{1}".format(attrNum, 1))
	  else:
		formatAttrs.append("{0}:{1}".format(attrNum, 0))
	  attrNum += 1
	  if attrs[index] == "2":
		formatAttrs.append("{0}:{1}".format(attrNum, 1))
	  else:
		formatAttrs.append("{0}:{1}".format(attrNum, 0))
	  attrNum += 1
	if index == 3:
	  if attrs[index] == "3":
		formatAttrs.append("{0}:{1}".format(attrNum, 1))
	  else:
		formatAttrs.append("{0}:{1}".format(attrNum, 0))
	  attrNum += 1
	  if attrs[index] == "4":
		formatAttrs.append("{0}:{1}".format(attrNum, 1))
	  else:
		formatAttrs.append("{0}:{1}".format(attrNum, 0))
	  attrNum += 1
	if index == 4:
	  if attrs[index] == "3":
		formatAttrs.append("{0}:{1}".format(attrNum, 1))
	  else:
		formatAttrs.append("{0}:{1}".format(attrNum, 0))
	  attrNum += 1
	if index > 4 or index <= 1:
	  formatAttrs.append("{0}:{1}".format(attrNum, attrs[index]))
	  attrNum += 1
  return " ".join(formatAttrs) + "\n"
if len(sys.argv) < 3:
  sys.stderr.write("Usage: sourceDataFile resultDataFile\n")
  sys.exit(1)

sourcePath = sys.argv[1]
resultPath = sys.argv[2]
resultFd = open(resultPath, "w")
with open(sys.argv[1], "r") as sourceFd:
  lineNum = 0
  for line in sourceFd: 
	lineNum += 1
	if lineNum == 1 or lineNum == 2:
	  continue
	formatLine = formatSourceLine(line)
	if formatLine is None:
	  sys.stderr.write("error when formatting line: {0}".format(line))
	  sys.exit(1)
#	if lineNum == 2:
#	  resultFd.write("#{0}".format(formatLine))
#	  pprint(formatLine)
	else:
	  resultFd.write(formatLine)
resultFd.close()
