import sys
import os
import re
ESCAPEWORD = 'escape'
path = "/mnt/f/newfolder/"
listOfFiles = os.listdir(path)
countOfFiles = len(listOfFiles)
os.chdir(path)
for i in range(0,countOfFiles):
	match = re.search(ESCAPEWORD,listOfFiles[i])
	if not match:
		os.rename(path+listOfFiles[i], path+'Saying'+" "+str(i+1)+'.txt')

#debugging information
listOfFiles = os.listdir(path)
for list in listOfFiles:
	print(list)