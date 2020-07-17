from flask import Flask, render_template,request
from bs4 import BeautifulSoup
import requests
from Data import price,rating,title,soup
app = Flask(__name__)

# url = "https://bit.ly/2DP5ETj"
# r = requests.get(url)
# html_content = r.content
# soup = BeautifulSoup(html_content, "html.parser")
# price = soup.find("a", class_="_2cLu-l").get_text()
# price(price)

price = price(soup)
title = title(soup)
rating = rating(soup)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/products')
def Products():
    return render_template('products.html', main = [price,title,rating ])




















if __name__ == "__main__":
    app.run(debug=True, port=3000)