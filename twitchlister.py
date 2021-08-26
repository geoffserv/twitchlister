# twitchlister
#
# Proof of concept twitch bot
# 
# Renders a pygame window of a slowly crawling list
# The list is sourced from a text file
#
# Allows twitch chat to submit entries to a list
# the submitted entries, if any, are intersperced with the source file list as they come in

import pygame # brew install pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([1280,720]) # 16x9 SD for later capture in to VDMX
pygame.display.set_caption('Twitch Lister') # Set the window title for fun

screen_centerX = screen.get_rect().centerx
screen_centerY = screen.get_rect().centery
screen_bottom  = screen.get_rect().bottom

print("DEBUG -- screen_centerX:", screen_centerX)
print("DEBUG -- screen_centerY:", screen_centerY)
print("DEBUG -- screen_bottom:", screen_bottom)

# Define some colors for convenience and readability
black = (0,0,0)
white = (255,255,255)

deltaY = 0 # Track the Y offset as a textbox moves upwards

running = True # Start off in a running state.  When untrue, the program ends.

listFile = open("listlines.txt", "r") # listlines.txt contains the 'stock' list which plays in absense of chat input
listLines = listFile.readlines()

# listCrawler list will track the text and deltaY for two simultanous crawling lines of text
# We'll put the first one in now, with the first line from the listlines.txt file with a deltaY of 0

listCrawler = [ [listLines.pop(0), 0] ]

if __name__ == "__main__":

	while running and listLines: # we need to loop as long as there's text to show

		listLine = listLines.pop(0).strip() # pygame will not render control chars like newlines

		font = pygame.font.SysFont('Courier', 50)

		render_message = font.render(listLine, True, white) # by default rendered to the top-left of the screen
		render_message_height = render_message.get_rect().height

		while running and (screen_bottom + render_message_height + deltaY > 0):

			print("DEBUG -- render_message.get_rect().height:", render_message.get_rect().height, ", DeltaY", deltaY)

			screen.fill(black) # fill the screen with black, obliterating everything

			render_position = render_message.get_rect(center=(screen_centerX,
		                                                  screen_bottom + deltaY))
			#if (screen_bottom + render_message_height + deltaY < 0): # if the text is going off the screen
			#	deltaY = 0

			screen.blit(render_message, render_position)

			pygame.display.update()

			deltaY -= 1 # Decrement deltaY to create upward movement

			for event in pygame.event.get():
				if event.type == QUIT: # If the window 'close' button is clicked...
					running = False

		deltaY = 0

	pygame.quit()
