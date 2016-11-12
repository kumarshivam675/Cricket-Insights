import yaml
from os import listdir
lst = listdir("/home/aditya9509/ipl")
lst.sort(reverse=True)
count = 0
for fnum in lst:
	name = "/home/aditya9509/ipl/" + str(fnum)
	f = open(name)
	print("Processing file: "+ name+" "+ str(count) + "/"+str(len(lst)))
	match = yaml.safe_load(f)
	f.close()
	try:
		print match["info"]["outcome"]["method"]
		count = count + 1
	except:
		print "Not found."

print count
