class Movie:
	def __init__(self, title, cinema):
		self.title = title
		self.cinema = cinema

	def __str__(self):
		return self.title