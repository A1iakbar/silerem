# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:00:53 2022

@author: Calypso
"""

#Data crawler
import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

request = requests.get('https://www.imdb.com/chart/top/')

content = request.content

soup = BeautifulSoup(content, 'html.parser')

adlar = soup.find_all('td', {"class": "titleColumn"})
iller = soup.find_all('span', {"class": "secondaryInfo"})
reytingler = soup.find_all('td', {"class": "ratingColumn imdbRating"})


film_adlar = [i.text.strip() for i in adlar]
film_iller = [k.text.strip("()") for k in iller]
film_reyting = [j.text.strip() for j in reytingler]

data = pd.DataFrame(list(zip(film_adlar, film_iller, film_reyting)), 
                    columns = ("adlar","iller","reytingler"))

data["adlar"] = data["adlar"].map(lambda setir: setir.split("\n")[1].strip(" "))

data["iller"] = data["iller"].astype("int64")
data["reytingler"] = data["reytingler"].astype("float64")

data.groupby("iller")["reytingler"].mean()

plt.figure(figsize = (20,6))

plt.plot(data.groupby("iller")["reytingler"].mean())

    