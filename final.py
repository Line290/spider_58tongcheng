import urllib
import urllib2
import HTMLParser
from bs4 import BeautifulSoup
import re
import MySQLdb as mdb
import json

i=1 #number order of companys
def GetOnePageUrl(url):
	global i
	flag = 0
	request = urllib2.Request(url)
	html = urllib2.urlopen(request)
	soup = BeautifulSoup(html, "lxml")
	for link in soup.find_all(name='a', attrs={"href": re.compile(r'^http://qy.58.com/mq/[0-9]*/$')}):
		#print link.get('href')
		if flag%2 == 0:
			GetOneUrlInfo(link.get('href'))
			print i
			i += 1
		flag += 1

def GetOneUrlInfo(url):
	global i
	request = urllib2.Request(url)
	html = urllib2.urlopen(request)
	soup = BeautifulSoup(html,"lxml")
	#for addr in soup.find_all(name='td',limit=5):
	#   print addr.string
	fiveinfo = soup.find_all(name='td',limit=5)
	if len(fiveinfo) == 0: #the company's link go to website which made by itself
		return
	co_name = fiveinfo[0].string
	co_type = fiveinfo[1].string
	co_numpeople = fiveinfo[2].string
	co_manager= fiveinfo[4].string
	co_tel_addr = "/tmp/pic/" + str(i) + "tel.gif"
	co_email_addr = "/tmp/pic/" + str(i) + "email.gif"
	co_connect_all = soup.find_all(name='a', attrs={"href": re.compile(r'^http://[\s\S]*.5858.com$')})
	if len(co_connect_all) != 0:
		co_connect = co_connect_all[0].get('href')
	else:
		co_connect = "the link is not formative" #company's link isn't formative
	addr = soup.find_all(name = 'span')
	co_addr = addr[18].string

#mysql
	conn = mdb.connect(host='127.0.0.1',port=3306,user='root', passwd='password',db='co58',charset='utf8')
	cursor = conn.cursor()
	cursor.execute("insert into 58co values('%d','%s','%s','%s','%s','%s','%s','%s','%s')"%(i,co_name,co_type,co_numpeople,co_manager,co_tel_addr,co_email_addr,co_connect,co_addr))
	cursor.close()
	conn.commit()
	conn.close()

#save images
	strtel = 'tel'
	stremail = 'email'
	flag = 0
	for link in soup.find_all(name='img', attrs={"src": re.compile(r'^http://image.58.com/showphone.aspx.[\s\S]*')}):
	    #print link.get('src')
	    if flag == 0:
	    	f = open(str(i)+strtel+'.gif','wb')
	    	flag += 1
	    else:
	        f = open(str(i)+stremail+'.gif','wb')
	        flag -=1
	    req = urllib2.urlopen(link.get('src'))
	    buf = req.read()
	    f.write(buf)

#there are ten pages
j = 1
while j <= 10:
    url = 'http://nj.58.com/yewu/pn' + str(j) + '/?jobfrom=mingqi'
    GetOnePageUrl(url)
    j += 1