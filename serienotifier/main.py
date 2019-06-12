#!/usr/bin/python3

import mysql.connector
import json
import requests
import smtplib
import datetime

class movie: 
    def __init__(self):
        self.dbase = mysql.connector.connect(
        host= "192.168.2.201",
        user= "",
        passwd = "",
        database = "movies"
        )

    def getData(self):
        self.mycursor = self.dbase.cursor()
        self.mycursor.execute("SELECT id, date, mail, title FROM movies" )
        return self.mycursor.fetchall()

    def updateDate(self, movieID, date):
        self.mycursor.execute("SELECT id, date FROM movies")
        self.mycursor.fetchall()
        self.mycursor.execute(f"UPDATE movies SET date = '{date}'  WHERE id ='{movieID}'")
        self.dbase.commit()

    def updateMail(self, movieID):
        self.mycursor.execute("SELECT id, mail FROM movies")
        self.mycursor.fetchall()
        self.mycursor.execute(f"UPDATE movies SET mail ='yes' WHERE id ='{movieID}'")
        self.dbase.commit()

    def getSeason(self, movieID):
        baseUrl = 'http://www.omdbapi.com/?apikey='
        apiKey = ''
        self.url = f"{baseUrl}{apiKey}&i={movieID}"
        req = requests.get(self.url)
        getj = json.loads(req.text)
        selectob = getj["totalSeasons"][0]
        return selectob

    def getDate(self, season):
        urlReq = requests.get(f"{self.url}&Season={season}")
        getj = json.loads(urlReq.text)
        title = getj["Title"]
        release = getj["Episodes"][0]['Released']
        return release
 
    def mail(self, title):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("mail", "passw")
        subject = f"{title} wordt vandaag uit gezonden"
        body = f"{title} wordt vandaag uit gezonden"
        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail("from-mail", "to-mail", msg)



x = datetime.datetime.now()
day = x.strftime("%Y-%m-%d")
getM = movie()

for row in getM.getData():
    if row[1] == 'N/A':
        season = getM.getSeason(row[0])
        date = getM.getDate(season)
        getM.updateDate(row[0], date)
        continue
    elif row[1] != 'N/A': 
        if row[2] == "no":
            if row[1] == day:
                getM.mail(row[3])
                getM.updateMail(row[0])
                continue
            else:
                continue
        else:
            continue
