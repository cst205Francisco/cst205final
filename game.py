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

def initGrid():

	#initialize grid points
	b2 = GridPoint(0,0,0,1)
	c2 = GridPoint(0,0,1,1)
	d2 = GridPoint(0,0,1,1)
	e2 = GridPoint(0,0,1,1)
	f2 = GridPoint(0,0,1,1)
	g2 = GridPoint(0,1,1,0)
	l2 = GridPoint(0,1,0,0)
	o2 = GridPoint(0,1,0,0)
	g3 = GridPoint(1,1,0,1)
	h3 = GridPoint(0,1,1,0)
	j3 = GridPoint(0,1,0,0)
	l3 = GridPoint(1,1,0,1)
	m3 = GridPoint(0,1,1,1)
	n3 = GridPoint(0,0,1,1)
	o3 = GridPoint(1,0,1,0)
	d4 = GridPoint(0,1,0,0)
	g4 = GridPoint(1,1,0,1)
	h4 = GridPoint(1,1,1,1)
	i4 = GridPoint(0,0,1,1)
	j4 = GridPoint(1,0,1,1)
	k4 = GridPoint(0,0,1,1)
	l4 = GridPoint(1,0,1,1)
	m4 = GridPoint(1,1,1,0)
	c5 = GridPoint(0,1,0,1)
	d5 = GridPoint(1,1,1,1)
	e5 = GridPoint(0,1,1,0)
	g5 = GridPoint(1,1,0,1)
	h5 = GridPoint(1,0,1,0)
	m5 = GridPoint(1,0,0,1)
	n5 = GridPoint(0,1,1,1)
	o5 = GridPoint(0,0,1,0)
	b6 = GridPoint(0,0,0,1)
	c6 = GridPoint(1,0,1,1)
	d6 = GridPoint(1,0,1,1)
	e6 = GridPoint(1,0,1,1)
	f6 = GridPoint(0,0,1,1)
	g6 = GridPoint(1,0,1,0)
	n6 = GridPoint(1,1,0,0)
	n7 = GridPoint(1,1,0,0)
	n8 = GridPoint(1,1,0,0)
	b9 = GridPoint(0,1,0,0)
	e9 = GridPoint(1,0,1,0)
	f9 = GridPoint(0,0,1,1)
	g9 = GridPoint(0,0,1,1)
	h9 = GridPoint(0,1,1,0)
	m9 = GridPoint(0,1,0,1)
	n9 = GridPoint(1,1,1,1)
	o9 = GridPoint(0,1,1,0)
	b10 = GridPoint(1,1,0,0)
	e10 = GridPoint(1,1,0,0)
	h10 = GridPoint(1,1,0,1)
	i10 = GridPoint(0,1,1,1)
	j10 = GridPoint(0,1,1,1)
	k10 = GridPoint(0,1,1,1)
	l10 = GridPoint(0,0,1,1)
	m10 = GridPoint(1,0,1,1)
	n10 = GridPoint(1,0,1,1)
	o10 = GridPoint(1,1,1,0)
	b11 = GridPoint(1,0,0,1)
	c11 = GridPoint(0,0,1,1)
	d11 = GridPoint(0,0,1,1)
	e11 = GridPoint(1,0,1,0)
	h11 = GridPoint(1,0,0,1)
	i11 = GridPoint(1,0,1,1)
	j11 = GridPoint(1,1,1,1)
	k11 = GridPoint(1,0,1,0)
	o11 = GridPoint(1,0,0,0)
	j12 = GridPoint(1,0,0,0)

	#connect grid points
	b2.setEastObj(c2)
	c2.setWestObj(b2)
	c2.setEastObj(d2)
	d2.setWestObj(c2)
	d2.setEastObj(e2)
	e2.setWestObj(d2)
	e2.setEastObj(f2)
	f2.setWestObj(e2)
	f2.setEastObj(g2)
	g2.setWestObj(f2)
	g2.setSouthObj(g3)
	l2.setSouthObj(l3)
	o2.setSouthObj(o3)
	g3.setNorthObj(g2)
	g3.setSouthObj(g4)
	g3.setEastObj(h3)
	h3.setSouthObj(h4)
	h3.setWestObj(g3)
	j3.setSouthObj(j4)
	l3.setNorthObj(l2)
	l3.setSouthObj(l4)
	l3.setEastObj(m3)
	m3.setSouthObj(m4)
	m3.setWestObj(l3)
	m3.setEastObj(n3)
	n3.setWestObj(m3)
	n3.setEastObj(o3)
	o3.setNorthObj(o2)
	o3.setWestObj(n3)
	d4.setSouthObj(d5)
	g4.setNorthObj(g3)
	g4.setSouthObj(g5)
	g4.setEastObj(h4)
	h4.setNorthObj(h3)
	h4.setSouthObj(h5)
	h4.setWestObj(g4)
	h4.setEastObj(i4)
	i4.setWestObj(h4)
	i4.setEastObj(j4)
	j4.setNorthObj(j3)
	j4.setWestObj(i4)
	j4.setEastObj(k4)
	k4.setWestObj(j4)
	k4.setEastObj(l4)
	l4.setNorthObj(l3)
	l4.setWestObj(k4)
	l4.setEastObj(m4)
	m4.setNorthObj(m3)
	m4.setSouthObj(m5)
	m4.setWestObj(l4)
	c5.setSouthObj(c6)
	c5.setEastObj(d5)
	d5.setNorthObj(d4)
	d5.setSouthObj(d6)
	d5.setWestObj(c5)
	d5.setEastObj(e5)
	e5.setSouthObj(e6)
	e5.setWestObj(d5)
	g5.setNorthObj(g4)
	g5.setSouthObj(g6)
	g5.setEastObj(h5)
	h5.setNorthObj(h4)
	h5.setWestObj(g5)
	m5.setNorthObj(m4)
	m5.setEastObj(n5)
	n5.setSouthObj(n6)
	n5.setWestObj(m5)
	n5.setEastObj(o5)
	o5.setWestObj(n5)
	b6.setEastObj(c6)
	c6.setNorthObj(c5)
	c6.setWestObj(b6)
	c6.setEastObj(d6)
	d6.setNorthObj(d5)
	d6.setWestObj(c6)
	d6.setEastObj(e6)
	e6.setNorthObj(e5)
	e6.setWestObj(d6)
	e6.setEastObj(f6)
	f6.setWestObj(e6)
	f6.setEastObj(g6)
	g6.setNorthObj(g5)
	g6.setWestObj(f6)
	n6.setNorthObj(n5)
	n6.setSouthObj(n7)
	n7.setNorthObj(n6)
	n7.setSouthObj(n8)
	n8.setNorthObj(n7)
	n8.setSouthObj(n9)
	b9.setSouthObj(b10)
	e9.setSouthObj(e10)
	e9.setEastObj(f9)
	f9.setWestObj(e9)
	f9.setEastObj(g9)
	g9.setWestObj(f9)
	g9.setEastObj(h9)
	h9.setWestObj(g9)
	h9.setSouthObj(h10)
	m9.setSouthObj(m10)
	m9.setEastObj(n9)
	n9.setNorthObj(n8)
	n9.setSouthObj(n10)
	n9.setWestObj(m9)
	n9.setEastObj(o9)
	o9.setWestObj(n9)
	o9.setSouthObj(o10)
	b10.setNorthObj(b9)
	b10.setSouthObj(b11)
	e10.setNorthObj(e9)
	e10.setSouthObj(e11)
	h10.setNorthObj(h9)
	h10.setSouthObj(h11)
	h10.setEastObj(i10)
	i10.setSouthObj(i11)
	i10.setWestObj(h10)
	i10.setEastObj(j10)
	j10.setSouthObj(j11)
	j10.setWestObj(i10)
	j10.setEastObj(k10)
	k10.setSouthObj(k11)
	k10.setWestObj(j10)
	k10.setEastObj(l10)
	l10.setWestObj(k10)
	l10.setEastObj(m10)
	m10.setNorthObj(m9)
	m10.setWestObj(l10)
	m10.setEastObj(n10)
	n10.setNorthObj(n9)
	n10.setWestObj(m10)
	n10.setEastObj(o10)
	o10.setNorthObj(o9)
	o10.setWestObj(n10)
	b11.setNorthObj(b10)
	b11.setEastObj(c11)
	c11.setWestObj(b11)
	c11.setEastObj(d11)
	d11.setWestObj(c11)
	d11.setEastObj(e11)
	e11.setNorthObj(e10)
	e11.setWestObj(d11)
	h11.setNorthObj(h10)
	h11.setEastObj(i11)
	i11.setNorthObj(i10)
	i11.setWestObj(h11)
	i11.setEastObj(j11)
	j11.setNorthObj(j10)
	j11.setSouthObj(j12)
	j11.setWestObj(i11)
	j11.setEastObj(k11)
	k11.setNorthObj(k10)
	k11.setWestObj(j11)
	o11.setNorthObj(o10)
	j12.setNorthObj(j11)



def startGame():
	
	game = "on"

	filename = '/Users/franciscogutierrez/cst205/final/cst205final/mario.jpg'
	pic = makePicture(filename)

	filename2 = '/Users/franciscogutierrez/cst205/final/cst205final/map.jpg'
	bg = makePicture(filename2)

	lockedBG = makePicture(filename2)

	mario = Hero(0,0)
	show(bg)

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

	
	








