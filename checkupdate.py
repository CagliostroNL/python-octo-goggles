#!/usr/bin/python3 

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as soup
import sys
import time
import smtplib

#set options for headless browser & getting the text i need
options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_options=options)
driver.get("https://www.ubnt.com/download/edgemax/edgerouter-x")
time.sleep(5) # wait 5 sec to make sure page loads. Could be done with the driver.wait but this is easier
gethtml = driver.page_source # gets the source 
html = soup(gethtml, 'html.parser') # parse it to bs4
htmlFind = html.find('td', class_='downloadResults__name') # find the strings i want
text = htmlFind.get_text()
test = "EdgeRouter ER-X/ER-X-SFP/EP-R6: Firmware v1.10.8"

if text == test:
    driver.quit()
    sys.exit()
else:
    driver.quit()
#Make's connection to mail server of google.
    user = ''
    password = ''
    sendFrom = user
    to = ""
    msg = "\n Nieuwe update beschikbaar voor unifi router"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user,password)
    server.sendmail(sendFrom, to, msg)
