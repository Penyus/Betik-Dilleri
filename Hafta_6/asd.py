import requests
from bs4 import BeautifulSoup

url = 'https://milligazete.com.tr/arsiv'
r = requests.get(url)
soup = BeautifulSoup(r.content, features='html.parser')
list2 = soup.find_all(name='div', attrs={'class': 'col-lg-6)'})
for i in lists2:
    for link in i.find_all('a'):
        my_link = link.get('href') + "\n"
        print(my_link)
        bas = 'https://milligazete.com.tr'
        yeni_link = bas + my_link
        print(yeni_link)
        