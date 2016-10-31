import urllib
import MySQLdb

def dbOps():
	target = open("/home/aditya9509/playerDimension.csv", 'w')
	columnNames = ""
	rowStr = ""
	db = MySQLdb.connect(host="localhost", user="root", passwd="password",db="cricketStockExchange")
	cursor = db.cursor()
	columnCursor = db.cursor()
	columnCursor.execute("SHOW columns FROM players")
	for row in columnCursor.fetchall():
		columnNames+=row[0]+","
	columnNames = columnNames[:-1]
	target.write(columnNames)
	target.write("\n")
	cursor.execute("SELECT * FROM players")
	print
	for row in cursor.fetchall():
		rowStr = ""
		for x in row:
			rowStr+=str(x)+","
		rowStr = rowStr[:-1]
		target.write(rowStr)
		target.write("\n")

dbOps()
