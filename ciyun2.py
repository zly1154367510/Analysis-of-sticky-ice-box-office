locaFile = open("content.txt","r+")

content = locaFile.read()

content1 = content.replace(" ","")
print content
#locaFile.write(content1)