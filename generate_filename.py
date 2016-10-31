import os

base_url = "http://www.espncricinfo.com/indian-premier-league-2016/engine/current/match/"
url = []
filename = os.listdir("./data")
for i in filename:
    url.append(base_url + i.split(".")[0] + ".html")

print len(url)