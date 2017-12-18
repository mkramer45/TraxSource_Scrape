import bs4
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import sqlite3

my_url = 'https://www.traxsource.com/genre/20/techno/top'
# opening up connecting, grabbing the page

#for url in my_url:

uClient = uReq(my_url)
# this will offload our content in'to a variable
page_html = uClient.read()
# closes our client
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"trk-list-cont"})
contain = containers[0]
container = containers[0]