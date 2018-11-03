#!/usr/bin/python3

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
import sys
import getopt


def google(opt1):
    url = 'http://google.com/search?q=' + opt1
    reg = Request(url, headers={'User-Agent': 'Mozilla'})
    html = urlopen(reg)
    parse = soup(html, "html.parser")   
    headers = parse.select('.r a')
    for link in headers:
        print(link.get('href'))

def bing(opt1):
    url = "https://www.bing.com/search?q=" + opt1
    reg = Request(url, headers={'User-Agent': 'Mozilla'})
    html = urlopen(reg)
    parse = soup(html, "html.parser")
    headers = parse.find_all("h2") 
    for link in headers:
        chek = link.a
        print(chek.get('href'))

def main(argv):
    searchTerm = " "
    opts, args = getopt.getopt(argv,"s:")
    for opt, arg in opts:
        if opt == "-s":
            searchTerm = arg
        else:
            print("no searchterm")
    print("[+] Searching for " + searchTerm)
    google(searchTerm)
    print("")
    bing(searchTerm)

if __name__ == "__main__":
    main(sys.argv[1:])
