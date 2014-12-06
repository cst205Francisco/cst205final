#Team 4 Kick ASCII
#Jennifer Dunham, Daniel Cadwell, Francisco Gutierrez, Hyo Lee
#CST 205 - Final

#project chimichanga

class GridPoint:
	def __init__(self, hasNorthIn, hasSouthIn, hasWestIn, hasEastIn):
		self.northBool = hasNorthIn
		self.southBool = hasSouthIn
		self.westBool = hasWestIn
		self.eastBool = hasEastIn
		self.northObj = False
		self.southObj = False
		self.westObj = False
		self.eastObj = False
	def hasNorth(self):
		return self.northBool
	def hasSouth(self):
		return self.southBool
	def hasWest(self):
		return self.westBool
	def hasEast(self):
		return self.eastBool
	def setNorthObj(self, objIn):
		self.northObj = objIn
	def getNorthObj(self):
		return self.northObj
	def setSouthObj(self, objIn):
		self.southObj = objIn
	def getSouthObj(self):
		return self.southObj
	def setWestObj(self, objIn):
		self.westObj = objIn
	def getWestObj(self):
		return self.westObj
	def setEastObj(self, objIn):
		self.eastObj = objIn
	def getEastObj(self):
		return self.eastObj
