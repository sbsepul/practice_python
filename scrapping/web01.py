'''
https://www.youtube.com/watch?v=NCfmEcyqgao
'''

import urllib.request

datos = urllib.request.urlopen('https://openwebinars.net/').read().decode()

from bs4 import BeautifulSoup

soup = BeautifulSoup(datos)
tags = soup('a')
for tag in tags:
    print(tag.get)