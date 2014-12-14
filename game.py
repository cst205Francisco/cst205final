#Team 4 Kick ASCII
#Jennifer Dunham, Daniel Cadwell, Francisco Gutierrez, Hyo Lee
#CST 205 - Final

#project chimichanga

import tempfile
import urllib
import java.lang
import time

#get user OS, either 'mac' or 'win'
def getOS():
	os = ""
	ver = sys.platform.lower()
	ver = java.lang.System.getProperty("os.name").lower()
	if ver.startswith('mac'):
		os = "mac"
	if ver.startswith('win'):
		os = "win"
	return os

'''
if getOS() == "win":
	#windows
	tempFilePath = tempfile.gettempdir() + "\\file.jpg"
else:
	#mac/linux
	tempFilePath = tempfile.gettempdir() + "file.jpg"

data = urllib.urlretrieve('URL', tempFilePath)
pic = makePicture(tempFilePath)
'''

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
		self.sword = False
		self.shield = False
		self.potion = False
		self.ring = False
		self.charType = ""
	def setX(self, x):
		self.xpos = x
	def getX(self):
		return self.xpos
	def setY(self, y):
		self.ypos = y
	def getY(self):
		return self.ypos
	def hasSword(self):
		return self.sword
	def setSword(self, myBool):
		self.sword = myBool
	def hasShield(self):
		return self.shield
	def setShield(self, myBool):
		self.shield = myBool
	def hasPotion(self):
		return self.potion
	def setPotion(self, myBool):
		self.potion = myBool
	def hasRing(self):
		return self.ring
	def setRing(self, myBool):
		self.ring = myBool
	def setCharType(self, myType):
		self.charType = myType
	def getCharType(self):
		return self.charType

		

def greenScreenOffset(pic, bg, offX, offY):
	for x in range(0, getWidth(pic)):
		for y in range(0, getHeight(pic)):
			p = getPixel(pic, x, y)
			color = getColor(p)
			if distance(color, blue) > 200.0:
				setColor(getPixel(bg, x+offX, y+offY), color)
	return bg

def coverSteps(bg, lockedBG, offX, offY):
	for x in range(offX, offX+40):
		for y in range(offY, offY+40):
			p = getPixel(lockedBG, x, y)
			color = getColor(p)
			setColor(getPixel(bg, x, y), color)
	return bg

def replaceBG(oldBG, newBG):
	for x in range(0, getWidth(oldBG)):
		for y in range(0, getHeight(oldBG)):
			p = getPixel(newBG, x, y)
			color = getColor(p)
			setColor(getPixel(oldBG, x, y), color)
	return oldBG

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



#======================================================================================================================

def startGame():
	
	'''
	###

	#make variable global so game can be over during battle sequence
	global game
 
	#Collect userName for dialogs (particularly the win sequence) 
	userName = requestString("Hello, traveler!  What do you call yourself?")
	global userName

   	#initiate hitpoints - to be increased by finding shield and enchanted items and later passed to battle function
	defaultHitpoints = 20
	hitpoints = defaultHitpoints
	global hitpoints #global to be adjusted in various functions
	
	shield = "in place"
	sword = "in place"
	treasure = "in place"
	treasureDrink = "in place"
	inventory = {}
  	#global variables to be referenced and adjusted in various functions
	global hitpoints, sword, treasure, treasureDrink
	global inventory
	soundfile5 = r"C:\Users\Me\Downloads\FINAL PROJECT FILES\Inventory\sounds\Pick up item 1.wav"
	itemSound = makeSound(soundfile5)
	global itemSound
 

	###
	'''
	

	userName = requestString("Hello, traveler!  What do you call yourself?")
	if userName == None:
		userName = "MrImTooGoodToGiveAName"


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
	e9 = GridPoint(0,1,0,1)
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
	o10.setSouthObj(o11)
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

	game = "on"
	
	#gamePhase - menu, menu-map, map, battle, gameover

	gamePhase = "menu"

	if getOS() == "win":
		#windows
		tempFilePath = "C:\\Windows\\Temp\\menu.jpg"
	else:
		#mac/linux
		tempFilePath = tempfile.gettempdir() + "menu.jpg"

	data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/menu.jpg', tempFilePath)
	bg = makePicture(tempFilePath)

	show(bg)


	while game != "over":

		if gamePhase == "menu":
			#choose your character
			userInput = requestString("Choose your character!")
			if userInput == None:
				userInput = "1"
			else:
				userInput = userInput.lower()

			myHero = Hero(360,440)

			if userInput == "1":
				#Link
				gamePhase = "menu-map"

				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\linkSmall.jpg"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "linkSmall.jpg"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/linkSmall.jpg', tempFilePath)
				pic = makePicture(tempFilePath)
				myHero.setCharType("link")

			if userInput == "2":
				#Turtle
				gamePhase = "menu-map"

				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\turtleSmall.jpg"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "turtleSmall.jpg"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/turtleSmall.jpg', tempFilePath)
				pic = makePicture(tempFilePath)
				myHero.setCharType("turtle")

			if userInput == "3":
				#Princess Zelda
				gamePhase = "menu-map"

				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\princessSmall.jpg"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "princessSmall.jpg"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/princessSmall.jpg', tempFilePath)
				pic = makePicture(tempFilePath)
				myHero.setCharType("princess")

			if userInput == "4":
				#IronMan
				gamePhase = "menu-map"

				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\ironManSmall.jpg"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "ironManSmall.jpg"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/ironManSmall.jpg', tempFilePath)
				pic = makePicture(tempFilePath)
				myHero.setCharType("ironMan")
				

		if gamePhase == "menu-map":

			if getOS() == "win":
				#windows
				tempFilePath = "C:\\Windows\\Temp\\bg.jpg"
			else:
				#mac/linux
				tempFilePath = tempfile.gettempdir() + "bg.jpg"

			data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/bg.jpg', tempFilePath)
			mapBG = makePicture(tempFilePath)

			if getOS() == "win":
				#windows
				tempFilePath = "C:\\Windows\\Temp\\lockedBG.jpg"
			else:
				#mac/linux
				tempFilePath = tempfile.gettempdir() + "lockedBG.jpg"

			data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/lockedBG.jpg', tempFilePath)
			lockedBG = makePicture(tempFilePath)

			addTextWithStyle(bg, 150, 275, "Loading...", makeStyle(sansSerif, bold, 70), white)
			repaint(bg)

			replaceBG(bg, mapBG)

			greenScreenOffset(pic, bg, 360, 440)

			repaint(bg)

			currentGridPoint = j12

			gamePhase = "map"


		if gamePhase == "map":
			userInput = requestString("go where?")
			if userInput == None:
				userInput = "up"
			else:
				userInput = userInput.lower()

			if (userInput == "down" or userInput == "d") and currentGridPoint.hasSouth():
				moveDown(myHero, pic, bg, lockedBG)
				currentGridPoint = currentGridPoint.getSouthObj()

			if (userInput == "up" or userInput == "u") and currentGridPoint.hasNorth():
				moveUp(myHero, pic, bg, lockedBG)
				currentGridPoint = currentGridPoint.getNorthObj()

			if (userInput == "left" or userInput == "l") and currentGridPoint.hasWest():
				moveLeft(myHero, pic, bg, lockedBG)
				currentGridPoint = currentGridPoint.getWestObj()

			if (userInput == "right" or userInput == "r") and currentGridPoint.hasEast():
				moveRight(myHero, pic, bg, lockedBG)
				currentGridPoint = currentGridPoint.getEastObj()

			if currentGridPoint == b9:
				#shield
				if myHero.hasShield():
					printNow("Nothing to see here")
				else:
					myHero.setShield(True)
					if getOS() == "win":
						#windows
						tempFilePath = "C:\\Windows\\Temp\\item.wav"
					else:
						#mac/linux
						tempFilePath = tempfile.gettempdir() + "item.wav"

					data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/sound/item.wav', tempFilePath)
					itemSound = makeSound(tempFilePath)
					play(itemSound)
					printNow("\nYou can now use this shield to protect you from evil. You have gained 10 hit points")

			if currentGridPoint == o11:
				#sword
				if myHero.hasSword():
					printNow("Nothing to see here")
				else:
					myHero.setSword(True)
					if getOS() == "win":
						#windows
						tempFilePath = "C:\\Windows\\Temp\\item.wav"
					else:
						#mac/linux
						tempFilePath = tempfile.gettempdir() + "item.wav"

					data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/sound/item.wav', tempFilePath)
					itemSound = makeSound(tempFilePath)
					play(itemSound)
					printNow("\nYou are the chosen one, and you now possess the mightiest sword in the land. You have gained 4 hit points and double the damage!!")

			if currentGridPoint == o2:
				#potion
				if myHero.hasPotion():
					printNow("Nothing to see here")
				else:
					myHero.setPotion(True)
					if getOS() == "win":
						#windows
						tempFilePath = "C:\\Windows\\Temp\\item.wav"
					else:
						#mac/linux
						tempFilePath = tempfile.gettempdir() + "item.wav"

					data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/sound/item.wav', tempFilePath)
					itemSound = makeSound(tempFilePath)
					play(itemSound)
					printNow("\nYou have found a potion, you drink half, but stop because it tastes awful, but you feel powerful now and your hit points increase by 4")

			if currentGridPoint == b2:
				#ring
				if myHero.hasRing():
					printNow("Nothing to see here")
				else:
					myHero.setPotion(True)
					if getOS() == "win":
						#windows
						tempFilePath = "C:\\Windows\\Temp\\item.wav"
					else:
						#mac/linux
						tempFilePath = tempfile.gettempdir() + "item.wav"

					data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/sound/item.wav', tempFilePath)
					itemSound = makeSound(tempFilePath)
					play(itemSound)
					printNow("\nYou have found a magical ring that increases your hit points by 8")

			if currentGridPoint == d4:
				#setup everything for the battle
				#redraw bg
				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\vsBG.jpg"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "vsBG.jpg"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/vsBG.jpg', tempFilePath)
				vsBG = makePicture(tempFilePath)

				addTextWithStyle(bg, 150, 275, "Loading...", makeStyle(sansSerif, bold, 70), white)
				repaint(bg)

				replaceBG(bg, vsBG)

				#add chars to vs screen

				if myHero.getCharType() == "link":
					if getOS() == "win":
						#windows
						tempFilePath = "C:\\Windows\\Temp\\linkLarge.jpg"
					else:
						#mac/linux
						tempFilePath = tempfile.gettempdir() + "linkLarge.jpg"

					data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/linkLarge.jpg', tempFilePath)
					largeHero = makePicture(tempFilePath)

				if myHero.getCharType() == "turtle":
					if getOS() == "win":
						#windows
						tempFilePath = "C:\\Windows\\Temp\\turtleLarge.jpg"
					else:
						#mac/linux
						tempFilePath = tempfile.gettempdir() + "turtleLarge.jpg"

					data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/turtleLarge.jpg', tempFilePath)
					largeHero = makePicture(tempFilePath)

				if myHero.getCharType() == "princess":
					if getOS() == "win":
						#windows
						tempFilePath = "C:\\Windows\\Temp\\princessLarge.jpg"
					else:
						#mac/linux
						tempFilePath = tempfile.gettempdir() + "princessLarge.jpg"

					data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/princessLarge.jpg', tempFilePath)
					largeHero = makePicture(tempFilePath)

				if myHero.getCharType() == "ironMan":
					if getOS() == "win":
						#windows
						tempFilePath = "C:\\Windows\\Temp\\ironManLarge.jpg"
					else:
						#mac/linux
						tempFilePath = tempfile.gettempdir() + "ironManLarge.jpg"

					data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/ironManLarge.jpg', tempFilePath)
					largeHero = makePicture(tempFilePath)

				#bad guy large
				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\zomaLarge.jpg"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "zomaLarge.jpg"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/zomaLarge.jpg', tempFilePath)
				largeEnemy = makePicture(tempFilePath)

				#set largeHero
				greenScreenOffset(largeHero, bg, 38, 170)
				greenScreenOffset(largeEnemy, bg, 372, 160)
				repaint(bg)

				#play monster sound
				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\monster.wav"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "monster.wav"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/sound/monster.wav', tempFilePath)
				monsterSound = makeSound(tempFilePath)
				play(monsterSound)

				gamePhase = "battle"
				doOnce = True
				printNow("dungeon")
				#prepare hitpoints here
				heroHP = 20
				bossHitpoints = 50
				if myHero.hasSword():
					heroHP += 4
				if myHero.hasRing():
					heroHP += 8
				if myHero.hasPotion():
					heroHP += 8
				if myHero.hasShield():
					heroHP += 10

		if gamePhase == "battle":

			#doOnce, preload sounds for battle
			
			if doOnce:
				#
				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\sword.wav"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "sword.wav"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/sound/sword.wav', tempFilePath)
				swordSound = makeSound(tempFilePath)

				#
				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\punch.wav"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "punch.wav"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/sound/punch.wav', tempFilePath)
				punchSound = makeSound(tempFilePath)

				#
				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\win.wav"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "win.wav"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/sound/win.wav', tempFilePath)
				winSound = makeSound(tempFilePath)

				#
				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\gameOver.wav"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "gameOver.wav"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/sound/gameOver.wav', tempFilePath)
				gameOverSound = makeSound(tempFilePath)

				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\win.jpg"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "win.jpg"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/win.jpg', tempFilePath)
				winBG = makePicture(tempFilePath)

				if getOS() == "win":
					#windows
					tempFilePath = "C:\\Windows\\Temp\\gameOver.jpg"
				else:
					#mac/linux
					tempFilePath = tempfile.gettempdir() + "gameOver.jpg"

				data = urllib.urlretrieve('https://raw.githubusercontent.com/cst205Francisco/cst205final/master/img/gameOver.jpg', tempFilePath)
				gameOverBG = makePicture(tempFilePath)
				
				doOnce = False

			userInput = requestString("Attack or Run?")
			if userInput == None:
				userInput = "run"
			else:
				userInput = userInput.lower()

			if userInput == "run":
				
				addTextWithStyle(bg, 150, 275, "Loading...", makeStyle(sansSerif, bold, 70), white)
				repaint(bg)
				replaceBG(bg, gameOverBG)
				repaint(bg)
				printNow("Coward!  I am not above stabbing you in the back!")
				printNow("And NOW I HAVE!  Your meaningless life is OVER!")
				printNow("\n\nYou died.")

				play(gameOverSound)
				game = "over"

			if userInput == "attack":
				#battle sequence
				if myHero.hasSword():
					#sword battle
					printNow("You swing your sword and connect!")
					play(swordSound)
					damage = damageDealt()
					damage *= 2
					printNow("You connect for " + str(damage) + " damage!")
					bossHitpoints -= damage
					if bossHitpoints <= 0:
						
						time.sleep(5)
						
						#redraw bg
						addTextWithStyle(bg, 150, 275, "Loading...", makeStyle(sansSerif, bold, 70), white)
						repaint(bg)
						replaceBG(bg, winBG)
						repaint(bg)

						printNow("\nYou have defeated bad guy and saved the Universe!!")
						printNow("All is well in the kingdom.")
						printNow("Great job, " + userName + "!")
						printNow("You kicked a lot of ASCII today!")

						play(winSound)
						game = "over"
					else:
						printNow("Bad Guy has " + str(bossHitpoints) + " remaining.")
						printNow("You're getting there!\n")
						printNow("Bad guy counter-attacks!")
						damage = damageDealt()
						printNow("He strikes for " +str(damage) + " damage!")
						heroHP -= damage
						printNow("Ouch! That hurt.")

						if heroHP > 0:
							printNow("You have " + str(heroHP) + " remaining.\n")
						else:
							
							time.sleep(5)
							
							#redraw bg
							addTextWithStyle(bg, 150, 275, "Loading...", makeStyle(sansSerif, bold, 70), white)
							repaint(bg)
							replaceBG(bg, gameOverBG)
							repaint(bg)

							printNow("\nYou have been defeated.")
							printNow("You're done, dead, finito.")
							printNow("The world is a dreary, hopeless place.\n")

							play(gameOverSound)
							game = "over"

				else:
					#fist battle
					printNow("You swing your fists and connect!")
					play(punchSound)
					damage = damageDealt()
					printNow("You connect for " + str(damage) + " damage!")
					bossHitpoints -= damage
					if bossHitpoints <= 0:
						
						time.sleep(5)
						
						#redraw bg	
						addTextWithStyle(bg, 150, 275, "Loading...", makeStyle(sansSerif, bold, 70), white)
						repaint(bg)
						replaceBG(bg, winBG)
						repaint(bg)

						play(winSound)
						printNow("\nYou have defeated bad guy and saved the Universe!!")
						printNow("All is well in the kingdom.")
						printNow("Great job, " + userName + "!")
						printNow("You kicked a lot of ASCII today!")
						game = "over"
					else:
						printNow("Bad Guy has " + str(bossHitpoints) + " remaining.")
						printNow("You're getting there!\n")
						printNow("Bad guy counter-attacks!")
						damage = damageDealt()
						printNow("He strikes for " +str(damage) + " damage!")
						heroHP -= damage
						printNow("Ouch! That hurt.")

					if heroHP > 0:
						printNow("You have " + str(heroHP) + " remaining.\n")
					else:
						
						time.sleep(5)
						
						#redraw bg
						addTextWithStyle(bg, 150, 275, "Loading...", makeStyle(sansSerif, bold, 70), white)
						repaint(bg)
						replaceBG(bg, gameOverBG)
						repaint(bg)

						play(gameOverSound)
						printNow("\nYou have been defeated.")
						printNow("You're done, dead, finito.")
						printNow("The world is a dreary, hopeless place.\n")
						game = "over"

		if userInput == "exit":
			game = "over"

#======================================================================================================================

def battle(hitpoints):
  import urllib
  import tempfile
  import time #to wait for swords to finish before winning or losing sound
  
  #THIS FUNCTION SHOULD TO BE GIVEN THE CHARACTER AS A PARAMETER SO IT KNOWS WHICH LARGE IMAGE TO BE LOADED ONTO THE BG IMAGE
  game = "on" #code needed to run battle independent of game() for testing. otherwise should just carry through as global
  userName = "test player" #code needed to run battle independent of game() for testing. otherwise should just carry through as global
  treasureDrink = "obtained" #code needed to run battle independent of game() for testing. otherwise should just carry through as global
  inventory = {"half a drink": 4} #code needed to run battle independent of game() for testing. otherwise should just carry through as global
    
  #print tempfile.gettempdir() #not functioning currently JD
  #winImage = urllib.urlretrieve(http://whitenebula.com/csumb/cst205/final/battlebg.jpg, tempFilePath + "\\win.jpg")
  
  
  global userName
  global game
  global inventory
  global treasureDrink
  
  bossHitpoints = 50
  filename1 = r"C:\Users\jdunham\Desktop\battle\VS.jpg"  
  filename2 = r"C:\Users\jdunham\Desktop\battle\turtleVS.jpg"
  filename3 = r"C:\Users\jdunham\Desktop\battle\ZomaVS.jpg"
  filename4 = r"C:\Users\jdunham\Desktop\battle\GameOver.jpg"
  filename5 = r"C:\Users\jdunham\Desktop\battle\YouWin.jpg"
  soundfile1 = r"C:\Users\jdunham\Desktop\battle\monsterBattleSound.wav"
  soundfile2 = r"C:\Users\jdunham\Desktop\battle\swords2.wav"
  soundfile3 = r"C:\Users\jdunham\Desktop\battle\winning3.wav"
  soundfile4 = r"C:\Users\jdunham\Desktop\battle\sadtrombone.wav"
  
  battleStartSound = makeSound(soundfile1)
  swordsSound = makeSound(soundfile2)
  winningSound = makeSound(soundfile3)
  losingSound = makeSound(soundfile4)
  
  #intentionally using same variable name as game because map should be replaced by battle image upon commencement of battle
  bg = makePicture(filename1)
  
  #IDEALLY, THIS SHOULD BE AN IF SCENARIO THAT CHROMAKEYS YOUR CHARACTER BASED ON THE CHARACTER YOU CHOSE EARLIER

  #image original source: http://img3.wikia.nocookie.net/__cb20120602231304/mario/images/3/32/8_Bit_Mario.png
  largeChar = makePicture(filename2)
  
  #image original source: http://villains.wikia.com/wiki/File:Psaro_8-bit.jpg
  largeBadGuy = makePicture(filename3)
  
  bg = blCopy(largeChar, bg, 38, 170)
  bg = blCopy(largeBadGuy, bg, 372, 160)
  
  if treasureDrink == "obtained":
    while game != "over":
      userInput = requestString("This place is kind of scary. You're getting weak in the knees.\nMaybe you should drink the rest of that disgusting tasting potion.\nIt seemed to make you feel better.\n\nY/N")
      userInput = userInput.lower()
      if userInput == ("y" or "yes" or "drink"):
        printNow("You pour the rest of that foul-tasting liquid down your throat.\nHey! You DO feel better!\nYou gain " + str(inventory['half a drink']) + " hit points!\n")
        hitpoints += inventory['half a drink']
        del inventory['half a drink']
        printNow(inventory)
        break
      elif userInput == ("n" or "no"):
        printNow("Your taste buds thank you.\n")
        break
      else:
        printNow("\nInvalid command")  
  
  repaint(bg)
  play(battleStartSound)
  printNow("You might have found me, but you will never stop me!")
  printNow("You will never get back your precious XXXXXXXX!")
  
      
  while game != "over":
    userInput = requestString("Attack or Run?")
    userInput = userInput.lower()
    if userInput == "exit":
      game = "over"
    elif userInput == "run":
      play(losingSound)
      printNow("Coward!  I am not above stabbing you in the back!")
      printNow("And NOW I HAVE!  Your meaningless life is OVER!")
      printNow("\n\nYou died.")
      game = "over"      
    else:
    #elif userInput == "attack" or userInput == "fight": 
      #ADD IF SWORD IN INVENTORY - ELSE FIGHT WITH FISTS
      #Attack bad guy

      printNow("You swing your sword and connect!")
      play(swordsSound)
      damage = damageDealt()
      printNow("You connect for " + str(damage) + " damage!")
      bossHitpoints -= damage
      if bossHitpoints > 0:
        printNow("Bad Guy has " + str(bossHitpoints) + " remaining.")
        printNow("You're getting there!\n")
      else:
        printNow("\nYou have defeated bad guy and saved XXXXX!")
        printNow("All is well in the kingdom.")
        printNow("Great job, " + userName + "!")
        printNow("You kicked a lot of ASCII today!")
        time.sleep(5)
        play(winningSound)
                
        #intentionally using same variable name, bg, as battle screen should be replaced by game win image upon winning
        bg = makePicture(filename5)
        repaint(bg)
        game = "over"
      
      #Bad guy counter-attack
      if bossHitpoints > 0:
        printNow("Bad guy counter-attacks!")
        #play(swordsSound) #not needed - other sound is long enough for the full battle.
        damage = damageDealt()
        printNow("He strikes for " +str(damage) + " damage!")
        hitpoints -= damage
        printNow("Ouch! That hurt.")
        if hitpoints > 0:
          printNow("You have " + str(hitpoints) + " remaining.\n")
        else:
          printNow("\nYou have been defeated.")
          printNow("You're done, dead, finito.")
          printNow("XXXXX will forever be the captive of bad guy.")
          printNow("The world is a dreary, hopeless place.\n")
          time.sleep(5)
          play(losingSound)
          
          #intentionally using same variable name, bg, as battle screen should be replaced by game lose image upon losing
          bg = makePicture(filename4)
          repaint(bg)
          game = "over"        
        
#======================================================================================================================

def damageDealt():
	import random
	for x in range(10):
		damage = random.randint(1,5)
	return damage
  
#======================================================================================================================

def blCopy(source, target, targetX, targetY):
  """copy a picture onto a target picture excluding blue"""
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      if distance(color, blue) > 170.0:
        setColor(getPixel(target, x+targetX, y+targetY), color)
  return target    	
  	
#======================================================================================================================

#Sword function

def swordFunc():
  
  # Global variables
  global game
  global inventory
  global sword
  global userInput
  global hitpoints
  # List of words to obtain items
  swordList = ["sword", "get sword", "take sword", "pickup sword", "pull sword", "pick up sword"]
  # Ask for user input
  userInput = requestString("You are near a sword")
  userInput = userInput.lower()
  # Loop through exit and items
  while game != "over":
    if userInput == "exit":
      game = "over"
    elif userInput in swordList:
      inventory["sword"] = 4
      sword = "obtained"
      play(itemSound)
      printNow("\nYou are the chosen one, and you now possess the mightiest sword in the land. You have gained " + str(inventory["sword"]) + " hit points")
      printNow("Inventory: " + inventory)
      return
    else:
      printNow("\nInvalid command")

#======================================================================================================================

#Shield function
            
def shieldFunc():
  # Global variables
  global game
  global inventory
  global shield
  global userInput
  global hitpoints
  # List of words to obtain items
  shieldList = ["shield", "get shield", "take shield", "pickup shield", "pull shield", "pick up shield"]
  # Ask for user input
  userInput = requestString("you are near a shield ")
  userInput = userInput.lower()
  # Loop through exit and items
  while game != "over":
    if userInput == "exit":
      game = "over"
    elif userInput in shieldList:
      inventory["shield"] = 10
      shield = "obtained"
      play(itemSound)
      printNow("\nYou can now use this shield to protect you from evil. You have gained " + str(inventory["shield"]) + " hit points")
      printNow("Inventory: " + inventory)
      return
    else:
      printNow("\nInvalid command")

#======================================================================================================================

#Treasure chest w/ ring function

def treasureFunc():
  # Global variables
  global game
  global inventory
  global userInput
  global treasure
  global hitpoints
  # List of words to obtain items  
  treasureList = ["open", "use", "treasure", "chest", "get treasure", "take treasure", "pickup treasure", "pull treasure", "pick up treasure"]
  # Ask for user input
  userInput = requestString("you are near a treasure chest ")
  userInput = userInput.lower()
  # Loop through exit and items
  while game != "over":
    if userInput == "exit":
      game = "over"
    elif userInput in treasureList:
      inventory["ring"] = 8
      ring = "obtained"
      play(itemSound)
      printNow("\nYou have found a magical ring that increases your hit points by " + str(inventory["ring"]))
      printNow("Inventory: " + inventory)
      return
    else:
      printNow("\nInvalid command")

#======================================================================================================================

#Treasure chest w/ drink function

def treasureDrinkFunc():
  # Global variables
  global game
  global inventory
  global userInput
  global treasure
  global treasureDrink
  global hitpoints
  # List of words to obtain items 
  drinkList = ["open", "use", "treasure", "chest", "get treasure", "take treasure", "pickup treasure", "pull treasure", "pick up treasure"]
  # Ask for user input
  userInput = requestString("you are near a treasure chest ")
  userInput = userInput.lower()
  # Loop through exit and items
  while game != "over":
    if userInput == "exit":
      game = "over"
    elif userInput in drinkList:
      inventory["half a drink"] = 4
      treasureDrink = "obtained"
      play(itemSound)
      printNow("\nYou have found a potion, you drink half, but stop because it tastes awful, but you feel powerful now and your hit points increase by " + str(inventory["half a drink"]))
      printNow("Inventory: " + inventory)
      return
    else:
      printNow("\nInvalid command")

#======================================================================================================================






