#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


def shamelessly_steal_top_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find("h2", {"class": "headline"}).text.strip()


url = "https://www.vg.no/"

first_article_title = shamelessly_steal_top_article(url)

print(f"The title of the first article is: {first_article_title}")
