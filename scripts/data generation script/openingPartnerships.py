import yaml
from os import listdir
import csv

resultFile = open("openingPartnership.csv", "w+")
resultFile.write("player1,player2,team,partnership,winner,looser")
resultFile.write("\n")
currentPrt = 0
previousP1 = ""
previousP2 = ""
import os
currentP1 = ""
currentP2 = ""
op = ""
dirtyBit = 0
lst = listdir("ipl")
count = 0
brk = 0
for fnum in lst:
	count = count + 1
	name = "./ipl/" + str(fnum)
	f = open(name)
	print("Processing file: "+ name+" "+ str(count) + "/"+str(len(lst)))
	match = yaml.safe_load(f)
	f.close()
	t1 = match["info"]["teams"][0]
	t2 = match["info"]["teams"][1]
	innings = match["innings"]

	winner = ""
	looser = "Draw"
	try:
		winner = match["info"]["outcome"]["winner"]
	except:
		winner = "Draw"

	if(winner == t1):
		looser = t2
	elif(winner == t2):
		looser = t1

	for x in innings:
		currentPrt = 0
		brk = 0
		for m in x:
			d = x[m]["deliveries"]
			t = x[m]["team"]
			previousP1 = ""
			previousP2 = ""
			currentP1 = ""
			currentP2 = ""
			for i in d:
				for j in i:
					currentP1 = i[j]["batsman"]
					currentP2 = i[j]["non_striker"]

					if((previousP1 == "" and previousP2 == "") or ((previousP1 == currentP1) and (previousP2 == currentP2)) or ((previousP1 == currentP2) and (previousP2 == currentP1)) ):
						currentPrt+= i[j]["runs"]["total"]
						previousP1 = min(currentP1 , currentP2)
						previousP2 = max(currentP1 , currentP2)
						op = previousP1+","+previousP2+","+t+","+str(currentPrt)+","+winner+","+looser
						dirtyBit = 1
					else:
					#Output partnership in file
						op = previousP1+","+previousP2+","+t+","+str(currentPrt)+","+winner+","+looser
						resultFile.write(op)
						currentPrt = i[j]["runs"]["total"]
						resultFile.write("\n")
						dirtyBit = 0
						brk = 1
						break
				if(brk == 1):
					break

			if(dirtyBit == 1):
				resultFile.write(op)
				resultFile.write("\n")
				currentPrt = 0
				dirtyBit = 0
resultFile.close()
