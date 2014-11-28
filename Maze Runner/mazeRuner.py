import pygame, random, os

from pygame.locals import *

RESOLUTION_X = 800
RESOLUTION_Y = 800
INPUT_TEMP = ""

class Maze:
	def __init__(self, mazeLayer):
		self.mazeArray = []
		self.state = 'create'
		self.mLayer = mazeLayer
		self.mLayer.fill((0,0,0,0))
		self.sLayer = mazeLayer
		self.sLayer.fill((0,0,0,0))
		for y in xrange(RESOLUTION_Y/8):
			pygame.draw.line(self.mLayer, (0,0,0,255), (0, y*8), (RESOLUTION_X, y*8))
			for x in xrange(RESOLUTION_X/8):
				self.mazeArray.append(0)
				if (y==0):
					pygame.draw.line(self.mLayer, (0,0,0,255), (x*8,0), (x*8, RESOLUTION_Y))
		
		pygame.draw.rect(self.sLayer, (0,0,255,255), Rect(0,0,8,8))
		pygame.draw.rect(self.sLayer, (255,0,255,255), Rect(((RESOLUTION_X-8),(RESOLUTION_Y-8),8,8)))
		self.totalCells = (RESOLUTION_X/8)*(RESOLUTION_Y/8)
		self.currentCell = random.randint(0, self.totalCells-1)
		self.visitedCells = 1
		self.cellStack = []
		self.compass=[(-1,0),(0,1),(1,0),(0,-1)]
		
	def update(self):
		if self.state == 'create':
			if self.visitedCells >= self.totalCells:
				self.currentCell = 0
				self.cellStack = []
				self.state = 'solve'
				return
			moved = False
			while (moved == False):
				
				x = self.currentCell % (RESOLUTION_X/8)
				y = self.currentCell / (RESOLUTION_X/8)
			
				neighbors = []
				for i in xrange (4):
					print("Within I in xrange")
					nx = x + self.compass[i][0]
					ny = y + self.compass[i][1]
					print ("X&Y",x, y)
					print("COMPASS 0,1",self.compass[i][0], self.compass[i][1])					
					print("NX, NY",nx, ny)
					print("RES X",(RESOLUTION_X/8))
					print("RES Y",(RESOLUTION_Y/8))
					print("CURRENT CELL",self.currentCell)
			
					if ((nx >= 0) and (ny >= 0) and (nx < (RESOLUTION_X/8)) and (ny < (RESOLUTION_Y/8))):
						if (self.mazeArray[(ny*(RESOLUTION_X/8)+nx)] & 0x000F) == 0:
							nidx = ny*(RESOLUTION_X/8)+nx
							neighbors.append((nidx, 1<<i))
				if len(neighbors) > 0:
					print("Within Neighbors > 0")
					idx = random.randint(0, len(neighbors)-1)
					nidx,direction = neighbors[idx]
				
					dx = x*8
					dy = y*8
					if direction & 1:
						self.mazeArray[nidx] |= (4)
						pygame.draw.line(self.mLayer, (0,0,0,0), (dx,dy+1),(dx,dy+7))
					elif direction & 2:
						self.mazeArray[nidx] |= (8)
						pygame.draw.line(self.mLayer, (0,0,0,0), (dx+1,dy+8),(dx+7,dy+8))
					elif direction & 4:
						self.mazeArray[nidx] |= (1)
						pygame.draw.line(self.mLayer, (0,0,0,0), (dx+8,dy+1),(dx+8,dy+7))
					elif direction & 8:
						self.mazeArray[nidx] |= (2)
						pygame.draw.line(self.mLayer, (0,0,0,0), (dx+1,dy),(dx+7,dy))
					self.mazeArray[self.currentCell] |= direction
				
					self.cellStack.append(self.currentCell)
				
					self.currentCell = nidx
				
					self.visitedCells = self.visitedCells + 1
					
					moved = True
				
				else:
					self.currentCell = self.cellStack.pop()
		elif self.state=='solve':
			if self.currentCell == (self.totalCells-1):
				self.state = 'reset'
				return
			moved = False
			while(moved == False):
				x = self.currentCell % (RESOLUTION_X/8)
				y = self.currentCell / (RESOLUTION_X/8)
				neighbors = []
				directions = self.mazeArray[self.currentCell] & 0xF
				for i in xrange(4):
					if (directions & (1<<i)) >0:
						nx = x + self.compass[i][0]
						ny = y + self.compass[i][1]
						if((nx>=0) and (ny>=0) and (nx < (RESOLUTION_X/8)) and (ny < (RESOLUTION_Y/8))):
							nidx = ny*(RESOLUTION_X/8)+nx
							if ((self.mazeArray[nidx] & 0xFF00) == 0):
								neighbors.append((nidx, 1<<i))
				if len(neighbors) > 0:
					idx = random.randint(0,len(neighbors)-1)
					nidx,direction = neighbors[idx]
					dx = x*8
					dy = y*8
					if direction & 1:
						self.mazeArray[nidx] |= (4 << 12)
					elif direction & 2:
						self.mazeArray[nidx] |= (8 << 12)
					elif direction & 4:
						self.mazeArray[nidx] |= (1 << 12)
					elif direction & 8:
						self.mazeArray[nidx] |= (2 << 12)
					pygame.draw.rect(self.sLayer, (0,255,0,255), Rect(dx,dy,8,8))
					self.mazeArray[self.currentCell] |= direction << 0
					self.cellStack.append(self.currentCell)
					self.currentCell = nidx
					moved = True
				else:
					pygame.draw.rect(self.sLayer, (255,0,0,255), Rect((x*8),(y*8),8,8))
					self.mazeArray[self.currentCell] &= 0xF0FF
					self.currentCell = self.cellStack.pop()
		elif self.state == 'reset':
			INPUT_TEMP = input("Press Enter to make a new maze (Escape to exit)...")
			self.__init__(self.mLayer)	

	def draw(self, displayScreen):
		displayScreen.blit(self.sLayer, (0,0))
		displayScreen.blit(self.mLayer, (0,0))

def main():
	pygame.init()
	
	displayScreen = pygame.display.set_mode((RESOLUTION_X,RESOLUTION_Y))
	pygame.display.set_caption('Maze Runner')
	pygame.mouse.set_visible(0)
	
	bGround = pygame.Surface(displayScreen.get_size())
	bGround = bGround.convert()
	bGround.fill((255,255,255))
	
	mazeLayer = pygame.Surface(displayScreen.get_size())
	mazeLayer = mazeLayer.convert_alpha()
	mazeLayer.fill((0,0,0,0))
	
	mazeOne = Maze(mazeLayer)
	
	displayScreen.blit(bGround, (0,0))
	pygame.display.flip()
	clock = pygame.time.Clock()
	
	while 1:
		clock.tick(60)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					return
		
		mazeOne.update()
		displayScreen.blit(bGround,(0,0))
		mazeOne.draw(displayScreen)
		pygame.display.flip()
	
	return

if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	RESOLUTION_X = int(input("X Resolution: "))
	RESOLUTION_Y = int(input("Y Resolution: "))
	main()
