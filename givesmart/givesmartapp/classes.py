class Charity():
	name = ""
	initials = ""
	summary = ""
	key_statistics = ""
	image_url = ""
	categories = list()
	stats = {}
	ratings = []
	url=""
	chart_url=""
	def __init__(self, name="", initials="", summary="", key_statistics="", categories=list(), image_url="", stats={}, ratings=[], url="", chart_url=""):
		self.name = name
		self.initials = initials
		self.summary = summary
		self.key_statistics = key_statistics
		self.categories = categories
		self.image_url = image_url
		self.stats = stats
		self.ratings = ratings
		self.url=url
		self.chart_url = chart_url

class Account():
	def __init__(self, name="", liked=[]):
		self.name = name
		self.liked = liked