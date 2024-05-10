import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/relationship_advice/comments/1c7x5s1/our_30m_30f_tenantadopted_son_18m_is_destroying/'

headers= {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

r = requests.get(url = url, headers=headers)

s = BeautifulSoup(r.content, 'html5lib')

title = s.find('title').text 

body = s.find('div', attrs = {'class' : 'expando expando-uninitialized'})

for p in body.findAll('p'):
    print(p)
