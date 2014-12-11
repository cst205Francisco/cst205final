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

class Hero:
	def __init__(self, xposIn, yposIn):
		self.xpos = xposIn
		self.ypos = yposIn
	def setX(self, x):
		self.xpos = x
	def getX(self):
		return self.xpos
	def setY(self, y):
		self.ypos = y
	def getY(self):
		return self.ypos
		

def greenScreenOffset(pic, bg, offX, offY):
	for x in range(0, getWidth(pic)):
		for y in range(0, getHeight(pic)):
			p = getPixel(pic, x, y)
			color = getColor(p)
			if distance(color, green) > 200.0:
				setColor(getPixel(bg, x+offX, y+offY), color)
	return bg

def coverSteps(bg, lockedBG, offX, offY):
	for x in range(offX, offX+40):
		for y in range(offY, offY+40):
			p = getPixel(lockedBG, x, y)
			color = getColor(p)
			setColor(getPixel(bg, x, y), color)
	return bg

def moveUp(hero, pic, bg, lockedBG):
	x = hero.getX()
	y = hero.getY()

	coverSteps(bg, lockedBG, x, y)
	greenScreenOffset(pic, bg, x, y-40)
	repaint(bg)

	hero.setX(x)
	hero.setY(y-40)

def moveDown(hero, pic, bg, lockedBG):
	x = hero.getX()
	y = hero.getY()

	coverSteps(bg, lockedBG, x, y)
	greenScreenOffset(pic, bg, x, y+40)
	repaint(bg)

	hero.setX(x)
	hero.setY(y+40)

def moveLeft(hero, pic, bg, lockedBG):
	x = hero.getX()
	y = hero.getY()

	coverSteps(bg, lockedBG, x, y)
	greenScreenOffset(pic, bg, x-40, y)
	repaint(bg)

	hero.setX(x-40)
	hero.setY(y)

def moveRight(hero, pic, bg, lockedBG):
	x = hero.getX()
	y = hero.getY()

	coverSteps(bg, lockedBG, x, y)
	greenScreenOffset(pic, bg, x+40, y)
	repaint(bg)

	hero.setX(x+40)
	hero.setY(y)

def startGame():
	
	game = "on"

	filename = '/Users/franciscogutierrez/cst205/final/cst205final/mario.jpg'
	pic = makePicture(filename)

	filename2 = '/Users/franciscogutierrez/cst205/final/cst205final/map.jpg'
	bg = makePicture(filename2)

	lockedBG = makePicture(filename2)

	mario = Hero(0,0)

	while game != "over":
		userInput = requestString("go where?")
		userInput = userInput.lower()

		if userInput == "exit":
			game = "over"

		if userInput == "down":
			moveDown(mario, pic, bg, lockedBG)

		if userInput == "up":
			moveUp(mario, pic, bg, lockedBG)

		if userInput == "left":
			moveLeft(mario, pic, bg, lockedBG)

		if userInput == "right":
			moveRight(mario, pic, bg, lockedBG)

	

	#pic = makePicture('/Users/franciscogutierrez/cst205/final/cst205final/mario.jpg')

	
	#bg = makePicture('/Users/franciscogutierrez/cst205/final/cst205final/map.jpg')

	
	








