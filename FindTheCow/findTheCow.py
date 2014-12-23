import pygame, sys, random, math
from pygame.locals import *

FPS = 1000
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
SIZE_SET_LEVEL = [250,150,100,75,50,25,10,5]
WHITE = (255,255,255,255)
CLICKGUESSCOLOR = (255,100,100,255)

global currentLevel 

currentLevel = 0

def main():
	pygame.init()

	screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption("Find the cow")

	global cowSound
	cowSound = pygame.mixer.Sound("CowMoo.wav")
	
	global cowImg
	cowImg = pygame.image.load("CowDraw.png").convert()
	cowImg = cowImg.convert_alpha()
	cowImg = pygame.transform.scale(cowImg, (SIZE_SET_LEVEL[currentLevel],SIZE_SET_LEVEL[currentLevel]))
	
	global backSurface
	backSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	
	global cowX
	global cowY
	
	backSurface.fill(WHITE)
	drawRandomPosition()
	pygame.display.flip()
	done = False
	
	FPSACTUAL = pygame.time.Clock()
	
	while not done:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				drawClickCircle()
				playDistanceSound()
				checkIfFound()
				
	pygame.display.flip()
	pygame.display.update()
	FPSACTUAL.tick(FPS)
	
def drawClickCircle():
	pygame.draw.circle(backSurface, CLICKGUESSCOLOR, pygame.mouse.get_pos(), 5, 5)
	pygame.display.update()

def drawRandomPosition():
	global cowX
	global cowY
	cowX = random.randint(0,WINDOWWIDTH- SIZE_SET_LEVEL[currentLevel])
	cowY = random.randint(0,WINDOWHEIGHT- SIZE_SET_LEVEL[currentLevel])
	backSurface.set_alpha(0)
	#drawCow()
	
def playDistanceSound():
	cowSound.stop()
	dist = math.hypot((pygame.mouse.get_pos()[0]-(cowX+(SIZE_SET_LEVEL[currentLevel]/2))),(pygame.mouse.get_pos()[1]-(cowY+(SIZE_SET_LEVEL[currentLevel]/2))))
	cowSound.set_volume(1/(dist/20))
	cowSound.play()

def drawCow():
	backSurface.blit(cowImg, (cowX,cowY))
	pygame.display.flip()
	pygame.display.update()

def checkIfFound():
	mouseX = pygame.mouse.get_pos()[0]
	mouseY = pygame.mouse.get_pos()[1]
	if mouseX > cowX and mouseX < cowX + SIZE_SET_LEVEL[currentLevel]:
		if mouseY > cowY and mouseY < cowY + SIZE_SET_LEVEL[currentLevel]:
			print "Found Cow"
			drawCow()
			continuePress = True
			global currentLevel
			while continuePress:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE:
							currentLevel = currentLevel + 1
							continuePress = False
							if __name__ == '__main__':
								main()

if __name__ == '__main__':
	main()