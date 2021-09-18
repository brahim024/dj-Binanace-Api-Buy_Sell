from bs4 import BeautifulSoup
from celery import shared_task
from urllib.request import urlopen, Request
import requests
from time import sleep

def create_currencies():

    responce=requests.get('https://www.investing.com/currencies/single-currency-crosses', headers={'User-Agent': 'Mozilla/5.0'})
    soup=BeautifulSoup(responce.text,'html.parser')

    currencies=soup.find("tbody").find_all("tr")[0:5]
    #enumarate row to pass index class name
    # starting index from 1
    for idx, currency in enumerate(currencies, 1):
        pair = currency.find("td", class_="plusIconTd").a.text
        # test
        bid = currency.find("td", class_=f"pid-{idx}-bid").text
        #test
        ask = currency.find("td", class_=f"pid-{idx}-ask").text
        #test
        high = currency.find("td", class_=f"pid-{idx}-high").text
        #test
        low = currency.find("td", class_=f"pid-{idx}-low").text
        #test
        change = currency.find("td", class_=f"pid-{idx}-pc").text
        # test
        change_p = currency.find("td", class_=f"pid-{idx}-pc").text
        # test
        time = currency.find("td", class_=f"pid-{idx}-time").text
        #test

        print({'pair':pair, 'bid':bid, 'ask':ask, 'high':high, 'low':low, 'change':change, 'change_p':change_p, 'time':time})
 
        
        

create_currencies()
