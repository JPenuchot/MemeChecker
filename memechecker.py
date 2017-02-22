import os
import sys
import glob
import imagehash

from PIL import Image

#	Input management

if not (len(sys.argv) == 2 or len(sys.argv) == 3):
	print("Usage : python3 memechecker.py [IMAGE_PATH_REGEX]")
	exit()

imglist = glob.glob(sys.argv[1])

if len(sys.argv) == 3:
	threshold = int(sys.argv[2])
else:
	threshold = 10

#	Getting everything inside the meme folder
imgbase = glob.glob("/home/jpenuchot/Pictures/denk-memes/*")

for currimg in imglist:
	try:
		cmphash = imagehash.phash(Image.open(currimg))
	except FileNotFoundError:
		print("File not found.\n")
		continue
	except IsADirectoryError:
		print("Given path is a directory.\n")
		continue
	
	#	Display hash, for fun
	print("Hash : ", cmphash, " ", currimg, "\n")
	
	#x = []
	
	print("Match\tDiff\t Hash\t\t\t Filename\n-----")
	
	#	Explore
	for impath in imgbase:
		if not os.path.isdir(impath):	#	You shall not match directories
			hsh = imagehash.phash(Image.open(impath))
			diff = hsh - cmphash
			if diff > threshold:
				print("NOPE\t", diff, "\t", hsh, "\t", impath)
			else:
				print("MATCH\t", diff, "\t", hsh, "\t", impath)