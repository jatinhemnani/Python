from bs4 import BeautifulSoup
import requests

url = "https://bit.ly/3ezbogK"
r = requests.get(url)
html_content = r.content
soup = BeautifulSoup(html_content, "html.parser")

def title(soup):
    
    title = soup.find("h1", class_="_9E25nV").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item


def price(soup):
    # soup = BeautifulSoup(html_content, "html.parser")
    title = soup.find("h1", class_="_9E25nV").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating(soup):
    # soup = BeautifulSoup(html_content, "html.parser")
    title = soup.find("h1", class_="_9E25nV").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item
