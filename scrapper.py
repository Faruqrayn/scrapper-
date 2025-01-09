# python -m pip install requests
# => get data from web (html, json, xml)
# python -m pip install beautifulsoup4
# => parse html

# install git
# create repository


# go to git bash (it is located in terminal)
# git config --global user.name "Faruqrayn"
# git config --global user.email "mdfarukrayn72562@gmail.com" 


# git init
#  git status => if you want to check what are the status of files
# gir diff => if you want to check what are the changes
# git add .
#  git commit -m "your message"
# copy paste git code from github and paste it into the terminal 
# git push origin => to pass the changed code into the git 

## This is the git tutorial branch

import requests
from bs4 import BeautifulSoup    # bs4 => library ,  beautifulsoup => class
import json

URL = "https://books.toscrape.com/"

def scrape_books(url):    # declaring the function to get the url
    response = requests.get(url)  # requests.get => to read the site of  
    print(response.status_code)   #print(response) => not show the statuscode
    if response.status_code != 200:
        print("ERROR")
        return
    
   # set encoding excipility to handle special character 
    response.encoding = response.apparent_encoding
    soup =  BeautifulSoup(response.text, "html.parser")   # bringing the html parser into the python through beautifulsoup 
    books = soup.find_all("article", class_= "product_pod") # entered in article then class of product_pod
    all_books = []  # creating list
    for book in books:
        title = book.h3.a["title"] # h3 tag ko (a) tag ko title jhiknu parne bhayera big bracket use hunxa
        price_text = book.find("p",class_="price_color").text   #book => already entered in article 
        currency = price_text[0]    # currency is in 0 index so its slicing first then,
        price = price_text[1:]      # price is in index 1 so after currency price print through slicing
        print(title, price, currency)
        formatted_book = {
            "title" : title,
            "currency" : currency,
            "price": price,
        }
        all_books.append(formatted_book)  # created list of dictionary  

    return all_books


books = scrape_books(URL)
with open("books1.json", "w") as f:
    json.dump(books,f, indent = 4)