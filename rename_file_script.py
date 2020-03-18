import sys
import os
import re
ESCAPEWORD = 'escape'
path = "/mnt/f/newfolder/"
listOfFiles = os.listdir(path)

for list in listOfFiles:
	match = re.search(ESCAPEWORD,list)
	if match:
		listOfFiles.remove(list)
i=0 
for list in listOfFiles:
	os.rename(path+list, path+'Общение'+" "+str(i+1)+'.mp4')
	i+=1
# countOfFiles = len(listOfFiles)
# os.chdir(path)
# for i in range(0,countOfFiles):
# 	os.rename(path+listOfFiles[i], 'Комплимент'+''+str(i+1)+'.mp4')

listOfFiles = os.listdir(path)
for list in listOfFiles:
	print(list)