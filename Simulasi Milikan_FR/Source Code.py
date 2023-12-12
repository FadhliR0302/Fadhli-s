#import pygame module in this program
import pygame

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value for white,
# green, blue colour .
AliceBlue  = (240, 248, 254)
Black = (0, 0, 0)

# assigning values to X and Y variable
X = 900
Y = 800

# create the display surface object
# of specific dimension..e(X, Y).
window = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('UAS-Semester 117')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 20)

# create a text surface object,
# on which text is drawn on it.
text = font.render('SIMULASI PERCOBAAN MILIKAN', True, Black, AliceBlue)
text_1=font.render('Oleh: Fadhli Rahman', True, Black, AliceBlue)
text_2=font.render('NIM :1306621064', True,Black,AliceBlue)

textRect = text.get_rect()

baterai= pygame.image.load('batere.png')
semprot= pygame.image.load('semprotan biru.png')

# infinite loop
while True:
	window.fill(AliceBlue)

	window.blit(text, (250,50))
	window.blit(text_1,(270,100))
	window.blit(text_2,(330,150))
	pygame.draw.rect(window, (0,0,0),
                 [150, 250, 450, 350], 2)
	window.blit(baterai, (620, 250))
	window.blit(semprot,(2,400))

	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.
	for event in pygame.event.get():

		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if event.type == pygame.QUIT:

			# deactivates the pygame library
			pygame.quit()

			# quit the program.
			quit()

		# Draws the surface object to the screen.
		pygame.display.update()