import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print("Status:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

movies = soup.select("h3.ipc-title__text")

print("Film sayısı:", len(movies))

for movie in movies:
    print(movie.text)