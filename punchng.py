import requests
from bs4 import BeautifulSoup
input_url = "https://punchng.com"
URL = input_url
headers = {"user-agent" : 'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'}
page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content,'html.parser')
#title = soup.find_all(class_ = "mrf-article__title")
title = soup.find_all("h3")
for a in title:
    print (a.get_text())
b = soup.find_all('section')
c = b[3]
d = c.find_all('a')
print ('--------LINK TO JUSTIN NEWS HEADLINES BELOW 👇')
for s in d:
    print (s.get('href'))
print ('CRAWLED FROM PUNCHNG by\n' '©CISCOBOT🤓')
    
#b = title.get_text()
#a = soup.find_all("a")
#b = soup.find_all('section')
#c = b[3]
#d = c.find_all('a')
#for s  in d:
#    print (s.get('href'))
#for h in b:
#    (b[3])
#mrf-buttonOpacityMid
#soup.find_all('a').get('href')