#!/usr/bin/env python3.5

import os
import sys
import glob
import imagehash

from PIL import Image

def genHashBase(imgGlob):
	imgBase = glob.glob(imgGlob)
	base = []
	for currImg in imgBase:
		try:
			base.append([currImg, imagehash.phash(Image.open(currImg))])
		except FileNotFoundError:
			continue
		except IsADirectoryError:
			continue
		except OSError:
			continue
	return base

#	Input management

if not (len(sys.argv) == 3 or len(sys.argv) == 4):
	print("Usage : memechecker.py [IMAGE_BASE_1_GLOB] [IMAGE_BASE_2_GLOB] [(Optional) THRESHOLD]")
	exit()

hashBase1 = genHashBase(sys.argv[1])
hashBase2 = genHashBase(sys.argv[2])

if len(sys.argv) == 4:
	threshold = int(sys.argv[3])
else:
	threshold = 10

print("Match\tDiff\tHash 1\t\t\tHash2\t\t\tFilename 1/2\n------")

for i in hashBase1:
	for j in hashBase2:
		diff = i[1] - j[1]
		if(diff < threshold):
			if(i[0] == j[0]):
				print("IDEM\t", diff, "\t", i[1], "\t", j[1], "\t", i[0], "\t", j[0])
			else:
				print("YES\t", diff, "\t", i[1], "\t", j[1], "\t", i[0], "\t", j[0])
		else:
			print("NO\t", diff, "\t", i[1], "\t", j[1], "\t", i[0], "\t", j[0])
