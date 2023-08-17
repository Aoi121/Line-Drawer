import pygame, sys, random
from pygame.locals import *

pygame.init()

BACKGROUND = (177, 177 ,177)
BLACK = (20,20,20)

FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800;
WINDOW_HEIGHT = 600;

WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Game window')

class Point:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

class Chain:
	def __init__(self, points = []):
		#List of Point objects
		self.points = []
	def update_points(self, point):
		self.points.append(point)
	#def update_chain(self, chains, point):
	#	chains.append(point)
	def draw_lines(self, chains):
		for chain in chains:
			line_draw(chain.points, WINDOW, BLACK)

def points_draw(chains, SURFACE, COLOR):
	if chains:
		pass
	else:
		return 0
	i = 0
	while(i < len(chains)):
		#print(chains[i].points[0].x)
		j = 0
		while(j < len(chains[i].points)):
			point = chains[i].points[j]
			SURFACE.fill(COLOR, ((point.x, point.y), (point.width, point.height)))
			j = j + 1
		i = i + 1
	#for chain in chains:
	#	for point in chain.points:
	#		SURFACE.fill(COLOR, ((point.x, point.y), (point.width, point.height)))

def line_draw(chains, SURFACE, COLOR):
	i_c = 0
	while(i_c < len(chains)):
		while(True):
			if(len(chains[i_c].points) > 1):
				pass
			else:
				break
			i_1 = 0
			i_2 = 1

			for x in range(len(chains[i_c].points)):
				p1 = chains[i_c].points[i_1]
				p2 = chains[i_c].points[i_2]

				#print("p1.x: " + str(p1.x))
				#print("p1.y: " + str(p1.y))
				#print("p2.x: " + str(p2.x))
				#print("p2.y: " + str(p2.y))

				pygame.draw.line(SURFACE, COLOR, (p1.x, p1.y), (p2.x, p2.y))
				i_1 = i_1 + 1
				i_2 = i_2 + 1
	
				if(i_1 == len(chains[i_c].points) or i_2 == len(chains[i_c].points)):
					break
				else:
					continue
			break
		i_c = i_c + 1

def main():
	loop = True
	pos1 = (0,0)
	pos2 = (0,0)

	pos_first = True
	pos1_on = False
	pos2_on = False

	chains = []

	while loop:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_state = pygame.mouse.get_pressed()

				if(mouse_state[2] == 1):
					p = pygame.mouse.get_pos()
					point = Point(p[0], p[1], 2, 2)
					chain = Chain()
					chain.update_points(point)
					chains.append(chain)
				elif(1 in mouse_state):
					p = pygame.mouse.get_pos()
					point = Point(p[0], p[1], 2, 2)
					if chains:
						chains[-1].update_points(point)
					else:
						chain = Chain()
						chain.update_points(point)
						chains.append(chain)
					print(chains[-1].points[0].x)

				#p = pygame.mouse.get_pos()
				#point = Point(p[0], p[1], 2, 2)
				#points.append(point)

		#Processing

		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
			chains = []

		print(len(chains))

		#Rendering
		WINDOW.fill(BACKGROUND)
		points_draw(chains, WINDOW, BLACK)
		#for p in points:
		#	WINDOW.fill(BLACK, ((p.x,p.y), (p.width,p.height)))

		if chains:
			line_draw(chains, WINDOW, BLACK)

		pygame.display.update()
		fpsClock.tick(FPS)

main()