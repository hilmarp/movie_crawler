from lxml import html
from movie import Movie
import requests
import json

# Síðan sem á að vinna með
page = "http://www.kvikmyndir.is/bio/syningatimar"

# Ná í síðuna og parsa með fromstring
response = requests.get(page)
tree = html.fromstring(response.text)

# /bla.html verður http://kvikmyndir.is/bla.html
tree.make_links_absolute(page)

# Ná í alla titla
titles = tree.xpath("//div[@id='mynd_titill']/a/text()")
movies = []

for title in titles:
	print(title)