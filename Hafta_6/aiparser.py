import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://www.milligazete.com.tr/arsiv"

r = requests.get(base_url)
print("Main page status:", r.status_code)

soup = BeautifulSoup(r.content, "html.parser")

articles = soup.find_all("div", class_="col-lg-6")
print(f"Found {len(articles)} divs")

for item in articles:
    link = item.find("a")

    if not link:
        continue

    href = link.get("href")
    title = link.get_text(strip=True)

    article_url = urljoin(base_url, href)

    print("\nTitle:", title)
    print("URL:", article_url)

    r2 = requests.get(article_url)
    print("Article status:", r2.status_code)

    if r2.status_code != 200:
        continue

    soup2 = BeautifulSoup(r2.content, "html.parser")

    # Haber içeriği
    content = soup2.find("div", class_="col-lg-6")

    if content:
        paragraphs = content.find_all("p")
        for p in paragraphs:
            text = p.get_text(strip=True)
            if text:
                print(text)