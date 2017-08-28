# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io, sys, os, codecs

if len(sys.argv) != 3:
	print "Error expected 2 arguments"
	sys.exit(-1)

inputFileName = sys.argv[1]
outputDirectoryPath = sys.argv[2]

if not os.path.exists(outputDirectoryPath):
    os.makedirs(outputDirectoryPath)


channelsDirectory = outputDirectoryPath+"/channels/"
vodDirectory = outputDirectoryPath+"/vod/"

if not os.path.exists(channelsDirectory):
    os.makedirs(channelsDirectory)

if not os.path.exists(vodDirectory):
    os.makedirs(vodDirectory)

inputFile = io.open(inputFileName, encoding="utf-8")
categoryName = ""

while True:
	comment = inputFile.readline()
	url = inputFile.readline()
	if not url:
		break
	print comment

	if "•●★" in comment:
		categoryName = comment.split(",")[1].replace("•●★","").replace("★●•","").replace("-","").strip()
	else:
		if ".ts" in url:
			outputDirectory = channelsDirectory
		else:
			outputDirectory = vodDirectory 
		codecs.open(outputDirectory+categoryName+".m3u", "a", "utf-8-sig").write(comment)
		codecs.open(outputDirectory+categoryName+".m3u", "a", "utf-8-sig").write(url)