

class Maze:
	def __init__(self, mazeLayer):
		self.visitedArray = []
		self.state = 'create'
		self.mLayer = mazeLayer
		self.mLayer.fill((0,0,0,0))
		self.sLayer = mazeLayer
		self.sLayer.fill((0,0,0,0))
		for y in xrange(RESOLUTION_Y/10):
			pygame.draw.line(self.mLayer, (255,255,255,255), (0,y*10), (RESOLUTION_X, y*10))
			for x in xrange(RESOLUTION_X/10):
				self.mazeArray.append(0)
				if (y==0):
					pygame.draw.line(self.mLayer, (255,255,255,255), (x*10,0), (x*10, RESOLUTION_Y))
					
		self.totalCells = (RESOLUTION_X/10)*(RESOLUTION_Y/10)
		self.currentCell = random.randint(0, self.totalCells - 1)
		self.visitedCells = 1
		self.cellStack = []
		self.compass=[(-1,0),(0,1),(1,0),(0,-1)] #WEST, EAST, SOUTH, NORTH
		
	def update(self):
		if self.state == 'create':
			
		
