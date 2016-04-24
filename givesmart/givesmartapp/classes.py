class Charity():
	name = ""
	summary = ""
	key_statistics = ""

	categories = list()
	def __init__(self, name="", summary="", key_statistics="", categories=list()):
		self.name = name
		self.summary = summary
		self.key_statistics = key_statistics
		self.categories = categories
