#---------------------------------------
# Made by Tanishq Dubey
# Protected under the MIT Licence (2014)
# All sounds are self made except for the background music which is
#	taken from "https://soundcloud.com/8bitsongs/man-overboard-montrose-8-bit"
#	All credit for that song belongs to the respective artist
# Font used is "UbuntuMono-R.ttf"
#
# DESCRIPTION: A simple pong game made to learn pygame and game logic
#
#---------------------------------------



#Import pygame and system essentials
import pygame, sys
from pygame.locals import *

#Frames per seconds that the game will run at
#Can be changed to screen refresh rate.
FPS = 1000

#Variables that define the size of the window
#Can be changed to screensize.
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720

#Other Variables

#Thickness of all lines in the program
LINETHICKNESS = 10
#Length of the paddle
PADDLESIZE = 100
#Distance the paddle is from the edge of the screen
PADDLEOFFSET = 20



#Game Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

def main():
	
	
	#Vars to see if ball is moving
	ballDirX = 1 #1 is Right, -1 is Left
	ballDirY = 1 #1 is down, -1 is up
	#Start pygame
	pygame.init()
	
	pygame.mixer.music.load('pongMusic.mp3')
	pygame.mixer.music.play(0)
	
	#Create a display surface for the system to draw on	
	global DISPLAYSURFACE
	
	global BASICFONT, BASICFONTSIZE
	
	BASICFONTSIZE = 20
	BASICFONT = pygame.font.Font('UbuntuMono-R.ttf', BASICFONTSIZE)
	
	#Set pygame clock speed, instead of auto regulated
	FPSCLOCK = pygame.time.Clock()

	#Set the display surface to the window height and width
	DISPLAYSURFACE = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

	#Set the caption for the window
	pygame.display.set_caption("Pong")
	

	#Starting Positions of the ball and the paddles
	ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
	ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2

	playerOnePosition = (WINDOWHEIGHT - PADDLESIZE)/2
	playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE)/2
	
	score = 0
	
	#Create the paddles and the ball
	paddleOne = pygame.Rect(PADDLEOFFSET, playerOnePosition,LINETHICKNESS,PADDLESIZE)
	paddleTwo = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition,LINETHICKNESS,PADDLESIZE)
	ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

	#Functions to Draw the area and the objects
	drawArena()
	drawPaddle(paddleOne)
	drawPaddle(paddleTwo)
	drawBall(ball)
	
	#Make the cursor invisible
	pygame.mouse.set_visible(0)

	#Create the main game loop
	while True:
		#Quick way to end the loop and quit the game
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			#Check for a mouse motion
			elif event.type == MOUSEMOTION:
				mouseX, mouseY = event.pos
				paddleOne.y = mouseY
				
		#Functions to Draw the area and the objects
		drawArena()
		drawPaddle(paddleOne)
		drawPaddle(paddleTwo)
		drawBall(ball)
		
		ball = moveBall(ball, ballDirX,ballDirY)
		ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
		
		score = checkPointScored(paddleOne, ball, score, ballDirX)
		
		paddleTwo = artificalIntelligence(ball, ballDirX, paddleTwo)
		
		#Uncommentthe next line to make a AI vs AI game
		#paddleOne = artificalIntelligenceOne(ball, ballDirX, paddleOne)
		displayScore(score)
		
		ballDirX = ballDirX * checkHitBall(ball, paddleOne, paddleTwo, ballDirX)
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)

#Method to draw the court
def drawArena():
	#Fill Area with Black Color
	DISPLAYSURFACE.fill((0,0,0))
	#Draw the border of the court
	pygame.draw.rect(DISPLAYSURFACE,WHITE,((0,0),(WINDOWWIDTH,WINDOWHEIGHT)),LINETHICKNESS*2)
	#Draw the centerline of the court
	pygame.draw.line(DISPLAYSURFACE,WHITE, ((WINDOWWIDTH/2),0),((WINDOWWIDTH/2),WINDOWHEIGHT),LINETHICKNESS/4)
	
def drawPaddle(paddle):
	#Stops the paddle between the bounds of the screen
	if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
		paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
	elif paddle.top < LINETHICKNESS:
		paddle.top = LINETHICKNESS

	#Draws the paddle
	pygame.draw.rect(DISPLAYSURFACE,WHITE,paddle)
	
def drawBall(ball):
	pygame.draw.rect(DISPLAYSURFACE,WHITE,ball)
	
def moveBall(ball, ballDirX, ballDirY):
	ball.x += ballDirX
	ball.y += ballDirY
	return ball
	
def checkEdgeCollision(ball, ballDirX, ballDirY):
	wallBump = pygame.mixer.Sound('wallBump.wav')
	if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
		wallBump.play()
		ballDirY = ballDirY * -1
	if ball.left == (LINETHICKNESS) or ball.right == (WINDOWWIDTH - LINETHICKNESS):
		wallBump.play()
		ballDirX = ballDirX * -1
	return ballDirX, ballDirY
	
def artificalIntelligence(ball, ballDirX, paddleTwo):
	#If the ball is moving away from the paddle, center the paddle
	if ballDirX == -1:
		if paddleTwo.centery < (WINDOWHEIGHT/2):
			paddleTwo.y += 1
		elif paddleTwo.centery > (WINDOWHEIGHT/2):
			paddleTwo.y -= 1
	elif ballDirX == 1:
		if paddleTwo.centery < ball.centery:
			paddleTwo.y += 1
		else:
			paddleTwo.y -= 1
	return paddleTwo
	
def artificalIntelligenceOne(ball, ballDirX, paddleTwo):
	#If the ball is moving away from the paddle, center the paddle
	if ballDirX == 1:
		if paddleTwo.centery < (WINDOWHEIGHT/2):
			paddleTwo.y += 1
		elif paddleTwo.centery > (WINDOWHEIGHT/2):
			paddleTwo.y -= 1
	elif ballDirX == -1:
		if paddleTwo.centery < ball.centery:
			paddleTwo.y += 1
		else:
			paddleTwo.y -= 1
	return paddleTwo	
	
def checkHitBall(ball, paddleOne, paddleTwo, ballDirX):
	bumpOne = pygame.mixer.Sound('paddleOne.wav')
	bumpTwo = pygame.mixer.Sound('paddleTwo.wav')
	if ballDirX == -1 and paddleOne.right == ball.left and paddleOne.top < ball.top and paddleOne.bottom > ball.bottom:
		bumpOne.play()
		return -1
	elif ballDirX == 1 and paddleTwo.left == ball.right and paddleTwo.top < ball.top and paddleTwo.bottom > ball.bottom:
		bumpTwo.play()
		return -1
	else:
		return 1

def checkPointScored(paddleOne, ball, score, ballDirX):
	if ball.left == LINETHICKNESS:
		return 0
	elif ballDirX == -1 and ball.left == paddleOne.right and paddleOne.top < ball.top and paddleOne.bottom > ball.bottom:
		score += 1
		return score
	elif ball.right == WINDOWWIDTH - LINETHICKNESS:
		score += 5
		return score
	else:
		return score
		
def displayScore(score):
	resultSurf = BASICFONT.render('Score = %s' %(score), True, WHITE)
	resultRect = resultSurf.get_rect()
	resultRect.topleft = (WINDOWWIDTH - 150, 25)
	DISPLAYSURFACE.blit(resultSurf, resultRect)

if __name__ == '__main__':
	main()
