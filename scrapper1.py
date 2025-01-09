import requests
from bs4 import BeautifulSoup
import json

URL = "https://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    print(response.status_code)
    if response.status_code != 200:
        print("Error")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_ = "product_pod")
    all_books = []
    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_= "price_color").text  # print the currency and price of the books
        currency = price_text[0]
        price = price_text[1:]
        print(title, currency, price)
        formatted_book = {
            "title": title,
            "currency": currency,
            "price": price
        }
        all_books.append(formatted_book)


    return all_books
    
books = scrape_books(URL)
with open("books.json", "w") as f:
    json.dump(books, f, indent = 4)

