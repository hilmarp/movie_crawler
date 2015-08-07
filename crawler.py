from lxml import html
from movie import Movie
from cinema import Cinema
import requests
import json

class Crawler:
	def __init__(self, url):
		self.url = url
		self.movies = []

	def crawl(self):
		self.get_movies_from_url(self.url)

	def get_movies_from_url(self, url):
		response = requests.get(url)
		tree = html.fromstring(response.text)

		# Inniheldur wrapper utum allir kvikmyndirnar
		# Þar eru allar upplýsingar
		movies = tree.xpath("//div[@id='utanumMynd_new']")

		# Ná í titil og bíósýningar
		for m in movies:
			title = m.xpath("div[@id='mynd_titill']/a/text()")
			cinemas = []
			times = []

			cinemaAndTimes = m.xpath("div[@id='myndbio_new' or @id='myndbio2_new']")

			for c in cinemaAndTimes:
				cinema = c.xpath("div[@id='bio']/a/text()")
				time = c.xpath("div[@id='timi_new']/div/a/span/text()")

				cinemas.append(cinema)
				times.append(time)

			self.create_movies(title, cinemas, times)

	def create_movies(self, title, cinemas, times):
		cinemaModel = Cinema(cinemas, times)
		movieModel = Movie(title, cinemaModel)

		self.movies.append(movieModel)

crawler = Crawler("http://www.kvikmyndir.is/bio/syningatimar")
crawler.crawl()

# for m in crawler.movies:
# 	print("\n")

# 	print(m.title)

# 	print(m.cinema.name)
	

# 	print("\n")