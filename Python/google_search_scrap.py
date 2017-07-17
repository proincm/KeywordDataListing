#-*-coding:utf8;-*-
#qpy:3
#qpy:console


import urllib.request 
from bs4 import BeautifulSoup



# oq = '&oq=%s' % q
count = 29
scount = 'num=%s' % count

chrome = '&aqs=chrome..69i57.39153j0j4'
andriod  = 'ms-andriod-'

listclient = [
'hms-tmobile',
'samsung'
'america-movil',
]
client = 'ms-android-samsung'
clientstr = '&client=%s' % client
sourceid = 'chrome-mobile'
ie = 'UTF-8'


q  = 'sublime add space -indent -indentation -tab'
params = {
		'q' : q,
		'num' : count,
		'client' : client,
		'sourceid' : sourceid,
		'ie' : ie,
}


query  = urllib.parse.urlencode(params)


google = 'https://www.google.com/search?'
google += query
user_agent =  'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7' 
myuseragent = 'Mozilla/5.0 (Linux; Android 6.0.1; SM-J510GN Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36'

headers = {'User-Agent':myuseragent,} 
request = urllib.request.Request(google, None,headers) #The assembled request response = 

with urllib.request.urlopen(request) as response: 
	html = response.read()
	print (len(html))
	soup = BeautifulSoup(html) 
	
	count  = 0
	for link in soup.find_all('h3', attrs={'class' : 'r'}): 
		count += 1
		print('result number: %s\n' % count)
		print(link.a.string)
		print('%s\n' % link.a['href'][7:])
		




