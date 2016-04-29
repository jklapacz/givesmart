class Charity():
	name = ""
	initials = ""
	summary = ""
	key_statistics = ""
	image_url = ""
	categories = list()
	stats = {}
	ratings = []
	def __init__(self, name="", initials="", summary="", key_statistics="", categories=list(), image_url="", stats={}, ratings=[]):
		self.name = name
		self.initials = initials
		self.summary = summary
		self.key_statistics = key_statistics
		self.categories = categories
		self.image_url = image_url
		self.stats = stats
		self.ratings = ratings

