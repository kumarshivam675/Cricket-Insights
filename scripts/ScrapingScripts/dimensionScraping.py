import urllib
import MySQLdb

def makeLink(team , pid , pname):
	return "http://www.iplt20.com/teams/" +team.lower().replace(" " , "-")+ "/squad/"+str(pid)+"/"+pname.replace(" " , "-")+"/"

def find(url):
	bat_style = "None"
	role = "None"
	bowls = "None"
	debut = "None"
	f = urllib.urlopen(url)
	text = f.read()
	l = len(text)

	index1 = text.find("<td>Batting Style</td>")
	if(index1!= -1):
		index2 = text.find("<td>" , index1+1 , l)
		index3 = text.find("<" , index2 + 1 , l)
		bat_style = text[index2+4 : index3]

	index1 = text.find("<td>Role</td>")
	if(index1!= -1):
		index2 = text.find("<td>" , index1+1 , l)
		index3 = text.find("<" , index2 + 1 , l)
		role = text[index2+4 : index3]

	index1 = text.find("<td>Bowls</td>")
	if(index1!= -1):
		index2 = text.find("<td>" , index1+1 , l)
		index3 = text.find("<" , index2 + 1 , l)
		bowls = text[index2+4 : index3]

	index1 = text.find("<td>IPL Debut</td>")
	if(index1!= -1):
		index2 = text.find("<td>" , index1+1 , l)
		index3 = text.find("<" , index2 + 1 , l)
		debut = text[index2+4 : index3]

	return bat_style , role , bowls , debut

def dbOps():

	db = MySQLdb.connect(host="localhost", user="root", passwd="password",db="cricketStockExchange")
	cursor = db.cursor()
	cursor.execute("SELECT id , name , current_team FROM players")
	count = 0
	for row in cursor.fetchall():
		count = count + 1
		print count
		url = makeLink(row[2] , row[0] , row[1])     #row[0] :id     row[1] : pname   row[2] : team
		bat_style , role , bowls ,debut = find(url)
		cursor.execute("UPDATE players SET role = %s , batting_style = %s , bowls = %s , debut = %s Where id = %s",(role , bat_style , bowls , debut ,row[0],))
	db.commit()
	db.close()
			

dbOps()
	
