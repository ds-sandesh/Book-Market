import requests
import time
import os
import pandas as pd
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/"

def get_soup(url):
    """Downloading the book and returning it as a BeautifulSoup object"""
    response = requests.get(url)
    response.encoding = "utf-8" #fixes the strange characters in the book description
    return BeautifulSoup(response.text, "html.parser")

#Step 1: get all category links from the sidebar homepage 
home = get_soup(BASE)
category_links = (
    home.find("div", class_="side_categories").find("ul").find("ul")
    .find_all("a")
)

all_books = []

#step 2: go through each category 
for link in category_links:
    category = link.text.strip()
    url = BASE + link.get("href")
    print(f"Scraping category: {category} - {url}")

#Step 3: keep going untill there are no more pages in the category
    while url:
        soup = get_soup(url)

        for book in soup.find_all("article", class_ = "product_pod"):
            all_books.append({
                "title": book.h3.a.get("title"),
                "price": book.find("p", class_="price_color").text,
                "rating": book.find("p", class_="star-rating").get("class")[1],
                "category": category,
                "availability": book.find("p", class_="instock availability").text.strip(),
            })

        next_button = soup.find("li", class_="next")
        if next_button:
            folder = url.rsplit("/", 1)[0]
            url = folder + "/" + next_button.a.get("href")
        else:
            url = None

        time.sleep(0.5) #to avoid getting blocked by the website

#Step 4: Save the data to a CSV file
df = pd.DataFrame(all_books)
os.makedirs("data", exist_ok=True)
df.to_csv("data/raw_books.csv", index=False)

print(f"Scraping completed. {len(all_books)} books saved to data/raw_books.csv")
print(df.head())

df = pd.read_csv("data/raw_books.csv")
print(df.shape)