#Imports the pygame module
import pygame

#Sets the value for the width and height of the display screen
W, H = 800, 600

#Creates the display screen
display = pygame.Surface ((W, H))
screen = pygame.display.set_mode ((W, H))
pygame.display.set_caption("Decryption")
clock = pygame.time.Clock()

#RGB example values
black = (0,0,0)
white = (255,255,255)

#The rate of change in colors

#The color directory & its values

#Initialized values for functions

#Draws the text

#Creates the color change

#Combines the color change and draw text into one function

# Initialising pygame

#Asks the user for the statement that will be decrypted

#Converts the following characters: 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

# Split into words

# Calculate number of words per line

# Divide into 3 lines

#Combines the 3 lines into one list

#Runs the program
