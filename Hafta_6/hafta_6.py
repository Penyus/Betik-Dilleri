import requests
from bs4 import BeautifulSoup

url = 'https://milligazete.com.tr/arsiv'
r = requests.get(url)
soup = BeautifulSoup(r.content, features='html.parser')
date = soup.find(name="time", attrs={"class": "fw-bold"})
title = soup.find(name="h1").getText()
icerik = soup.find(name="div", attrs={"class": "article-text content-padding"}).find_all(name="p")
list2 = soup.find_all(name='div', attrs={'class': 'col-lg-6'})



for i in list2: 
    for link in i.find_all('a'):
        my_link = link.get('href')
        bas = 'https://milligazete.com.tr'
        yeni_link = bas + my_link
        print(yeni_link)
        with open("milligazetelinkler.txt", "a") as file:
            file.write(yeni_link.strip() + "\n")

