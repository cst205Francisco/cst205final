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
  filename1 = r"C:\Users\Me\Downloads\battle\VS.jpg"  
  filename2 = r"C:\Users\Me\Downloads\battle\turtleVS.jpg"
  filename3 = r"C:\Users\Me\Downloads\battle\ZomaVS.jpg"
  filename4 = r"C:\Users\Me\Downloads\battle\GameOver.jpg"
  filename5 = r"C:\Users\Me\Downloads\battle\YouWin.jpg"
  soundfile1 = r"C:\Users\Me\Downloads\battle\monsterBattleSound.wav"
  soundfile2 = r"C:\Users\Me\Downloads\battle\swords2.wav"
  soundfile3 = r"C:\Users\Me\Downloads\battle\winning3.wav"
  soundfile4 = r"C:\Users\Me\Downloads\battle\sadtrombone.wav"
  
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
  
  	


#def grCopy(source, target, targetX, targetY):
#  """copy a picture onto a target picture excluding green"""
#  for x in range (0, getWidth(source)):
#    for y in range (0, getHeight(source)):
#      color = getColor(getPixel(source, x, y))
#      if distance(color, blue) > 170.0:
#        setColor(getPixel(target, x+targetX, y+targetY), color)
#  return target  


def blCopy(source, target, targetX, targetY):
  """copy a picture onto a target picture excluding blue"""
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      if distance(color, blue) > 170.0:
        setColor(getPixel(target, x+targetX, y+targetY), color)
  return target    	