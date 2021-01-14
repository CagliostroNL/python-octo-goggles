from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import re
import subprocess

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("http://192.168.167.186/calllog.htm")
driver.find_element_by_id("navAnswered Calls").click()
test = driver.find_element_by_xpath("//table/tbody/tr/td").text

i = 0

for line in test.split('\n'):
	i +=1
	line = line.strip('\r')
	if i == 6:
		line5 = line
		splitter = line5.split("2.")
		phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
		regNum = phoneNumRegex.search(splitter[0])
		nummer = regNum.group()
		subprocess.run(['clip.exe'], input=nummer.strip().encode('utf-16'), check=True)
driver.close()	
