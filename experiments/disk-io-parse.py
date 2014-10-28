#!/usr/bin/python

import os
import csv


def readFile(dirname):
	cmd = 'cd ' + dirname + ';./analyze.sh'
	return os.popen(cmd).readlines()

def parseLine(line):
	res = []
	tmp = line.split(' ')
	res.append(tmp[0])
	res.append(tmp[4][0:-1])
	res.append(tmp[7])
	tmp2 = float(tmp[7]) / 1024
	res.append(str(tmp2))
	return res

def parseFile(prefix, desFile):
	writer = csv.writer(desFile)

	writer.writerow(['####', '####', prefix, '####', '####'])
	writer.writerow([' ',' ',' ','SSD',' ',' ',' ',' ',' ','HDD',' ',' ',' '])
	writer.writerow([' '] + [' ','RAND',' ',' ','SEQ',' '] * 2)
	writer.writerow(['SIZE'] + ['IOPS','BW_KB','BW_MB'] * 4)

	r1 = readFile('ran-' + prefix + '-ssd')
	r2 = readFile('seq-' + prefix + '-ssd')
	r3 = readFile('ran-' + prefix + '-hdd')
	r4 = readFile('seq-' + prefix + '-hdd')

	for i in range(len(r1)):
		l1 = parseLine(r1[i])
		l2 = parseLine(r2[i])
		l3 = parseLine(r3[i])
		l4 = parseLine(r4[i])
		writer.writerow(l1 + l2[1:] + l3[1:] + l4[1:])


### main
f = file('result.csv', 'wb')
parseFile('read', f)
f.close()




