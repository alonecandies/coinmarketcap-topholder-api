from selenium import webdriver
from bs4 import BeautifulSoup as soup
from flask import Flask
import json
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/getTopHolders/<tokenName>')
def getTopHolder(tokenName):
    d = webdriver.Chrome()
    d.get('https://coinmarketcap.com/currencies/'+tokenName+'/holders/')
    holders = d.find_elements_by_css_selector("table tbody tr")
    topHolders = []
    for holder in holders:
        rank = holder.find_element_by_css_selector("td:nth-child(1)").text
        address = holder.find_element_by_css_selector("td:nth-child(2)").text
        amount = holder.find_element_by_css_selector("td:nth-child(3)").text
        percentage = holder.find_element_by_css_selector(
            "td:nth-child(4)").text
        topHolders.append({"rank": rank, "address": address,
                          "amount": amount, "percentage": percentage})
    return json.dumps(topHolders, separators=(',', ':'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
