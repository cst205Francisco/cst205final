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
   	#make variable global so game can be over during battle sequence
	global game
 
	#Collect userName for dialogs (particularly the win sequence) 
	userName = requestString("Hello, traveler!  What do you call yourself?")
	global userName

   	#initiate hitpoints - to be increased by finding shield and enchanted items and later passed to battle function
	defaultHitpoints = 10
	hitpoints = defaultHitpoints
	
	filename = r"C:\Users\jdunham\Desktop\mario.jpg"
	pic = makePicture(filename)

	filename2 = r"C:\Users\jdunham\Desktop\map.jpg"
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



def battle(hitpoints):
  import urllib
  import tempfile
  import time #to wait for swords to finish before winning or losing sound
  
  #THIS FUNCTION SHOULD TO BE PASSED THE CHARACTER AS A PARAMETER SO IT KNOWS WHICH LARGE IMAGE TO BE LOADED ONTO THE BG IMAGE
  game = "on" #code needed to run battle independent of game() for testing. otherwise should just carry through as global
  userName = "test player" #code needed to run battle independent of game() for testing. otherwise should just carry through as global
  
  #print tempfile.gettempdir() #not functioning currently JD
  #winImage = urllib.urlretrieve(http://whitenebula.com/csumb/cst205/final/battlebg.jpg, tempFilePath + "\\win.jpg")
  
  
  global userName
  global game
  
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
        

def damageDealt():
  import random
  for x in range(10):
    damage = random.randint(1,10)
  return damage  
  
def blCopy(source, target, targetX, targetY):
  """copy a picture onto a target picture excluding blue"""
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      if distance(color, blue) > 170.0:
        setColor(getPixel(target, x+targetX, y+targetY), color)
  return target    	
  	


	#pic = makePicture('/Users/franciscogutierrez/cst205/final/cst205final/mario.jpg')

	
	#bg = makePicture('/Users/franciscogutierrez/cst205/final/cst205final/map.jpg')
