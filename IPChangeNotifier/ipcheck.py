#!/usr/bin/python3                                          

import smtplib
import requests                                                               
import sys                                                                     
import fileinput
ip_addr = "0.0.0.0"             
url = requests.get("https://api.myip.com/")                                   
ip = url.json()['ip']                                          
                                                                              
if ip_addr == ip:
    sys.exit()                                                          
else:                                                                     
    #Replace IP in var ip_addr. 
    for line in fileinput.FileInput("ipcheck.py", inplace=1):                                           
                line = line.replace(ip_addr, ip)                         
                sys.stdout.write(line)                                                                  
    #Mail new ip address.
    server = smtplib.SMTP('smtp.gmail.com', 587)                        
    server.ehlo()                                                          
    server.starttls()                                                                   
    server.login("e-mail", "password")                                                                           
    msg = 'Subject: {}\n\n{}'.format("IP Address changed", "IP changed to" + ip)
    server.sendmail("", "mailaddress to send to", msg)
