# _______________________________________________________________________________________
# ___________________________________Welcome_____________________________________________
# _______________________________________________________________________________________

import pygame               # Importing modules
import random
import math
from pygame import mixer    # Helps handling music
pygame.init()               # Initialisation of pygame


# _______________________________________________________________________________________

# Screen Orientation and Manipulation

# Creating screen and giving access to display
screenx = 1200      # Defined screen var for screen size and other use
screeny = 800
screen = pygame.display.set_mode( ( screenx, screeny ) )


# Title, Icon, BackGround, BGMusic
pygame.display.set_caption("Space War")         # For changing name on title bar
icon = pygame.image.load('GameIcon.png')        # It stores game-icon
pygame.display.set_icon(icon)                   # It shows game-icon
bg = pygame.image.load('SpaceBG.jpg')           # It stores back-ground image
mixer.music.load('SpaceM.mp3')                  # It loads music
mixer.music.play(-1)     # This starts playing music; -1 for never ending music until pygame window stays opened


# _______________________________________________________________________________________

# Defining Attributes of Characters

# Player attributes setting
playerimg = pygame.image.load('Spaceship.png')
playerx = screenx//2      # Initial x coord of player
playery = screeny*(5/6)   # Initial y coord of player
deltaXplayer = 0          # Initilly, No change in x coord of player
deltaYplayer = 0          # Initilly, No change in y coord of player

def player(x,y):                    # Player attributes,functions
    screen.blit(playerimg, (x,y))   # Draws player on screen


# Enemies attributes setting
numOfEnemies =  10       # It defines number of enemies to be shown on screen
enemyimg = []
enemyx  = []            # Initialising lists for five enemies
enemyy  = []
deltaXenemy = []        # Change in coords is same and constant for all enemies
deltaYenemy = []
speedx =  (2 + (random.randint(0,5))/10)/5
speedy =  (1.5 + (random.randint(0,5))/10)/5

def enemy(x,y):
    screen.blit(enemyimg[i], (x,y))                 # Draws i'th  enemy on screen
for i in range(numOfEnemies):                       # Iterating for loop for each enemy
    enemyimg.append(pygame.image.load('UFO.png'))   # Shows enemy image
    enemyx.append(random.randint(65,screenx-65))    # Assigns a random x position to an enemy
    enemyy.append(random.randint(65,screeny-251))   # Assigns a random y position to an enemy
    deltaXenemy.append(speedx)     # We want change in x coord of each enemy equal 
    deltaYenemy.append(speedy)     # We want change in y coord of each enemy equal


# Attack attributes setting
attackimg = pygame.image.load('Fireball.png')
attackx = 0             # Initial x coord of attack
attacky = playery - 5   # Initial y coord of attack
deltaYattack = 1        # Change in y coord of attack
inventory = 'Full'      # For only one fireball at a time in our inventory

def attack(x,y):                    # Attack attributes,functions
    global inventory
    inventory = 'Empty'             # When attack is used, our inventory becomes empty
    screen.blit(attackimg, (x,y))   # Draws attack on screen


# _______________________________________________________________________________________

# Hit Checker

def hit( x1 , y1 , x2 , y2 ):            # When our attck hits enemy
    d = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
    if d < 40:
        return True
    else:
        return False

def GOcheck( x1 , y1 , x2 , y2 ):        # When the enemy hits our player
    d = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
    if d < 50:
        return True
    else:
        return False

# _______________________________________________________________________________________

# Score
Currentscore = 0
scoreX  = 30        # x coord for showing score
scoreY  = 15        # y coord for showing score
stdfont = pygame.font.Font('freesansbold.ttf', 30)     # Font name and size loading
scorefont = pygame.font.Font('freesansbold.ttf', 50)

def score(x,y):     # This shows the score on screenfront
    Score = stdfont.render('SCORE : '+ str(Currentscore), True, (0,255,0))   # We need to render in order to show text on screenfront
    screen.blit(Score, (x,y))

# _______________________________________________________________________________________

# Game Over = GO

gofont = pygame.font.Font('freesansbold.ttf', 50) 

def GOdisp():
    overbg = pygame.image.load('BG.png')
    screen.blit( overbg, (0,0) )
    GoFont = gofont.render('GAME OVER', True, (0,255,0) )
    Inter  = scorefont.render("Your final score is..", True, (0,255,0) )
    Scored = scorefont.render(str(Currentscore), True, (0,255,0) )
    screen.blit(GoFont, (450,300))
    screen.blit(Inter , (380,350))
    screen.blit(Scored, (585,400))

# _______________________________________________________________________________________
# _______________________________________________________________________________________




# _______________________________________________________________________________________

# Gameplay - Game Screen Handling

gamestate = True    # It is used for keeping pygame window on
got = False
while gamestate:    # Our main screen comes inside while loop

    # _______________________________________________________________________________________

    screen.fill( (0,0,0) )    # Setting default BG-colour
    screen.blit( bg, (0,0) )  # Draws Bg on screen

    player(playerx, playery)    # Calling player function
    score(scoreX,scoreY)        # Calling score function


    # _______________________________________________________________________________________

    # This for loop is checking for happening of events and controlling the player
    # An event is everything that can/will happen in your game, basically a key pressed on keyboard
    # Pygame module provides very simple functions and methods, so we have used it
    # _______________________________________________________________________________________


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:         # For closing pygame window when quit button is pressed...
            gamestate = False                 # ...by changing gamestate variable

        if event.type == pygame.KEYDOWN:      # Keydown is for checking whether any key is pressed or not
            if event.key == pygame.K_RIGHT:   # If right arrow key pressed..
                deltaXplayer = +20            # .. player moves left by 20 pixels
            if event.key == pygame.K_LEFT:    # If left arrow key pressed..
                deltaXplayer = -20            # .. player moves left by 20 pixels
            if event.key == pygame.K_SPACE:   # If spacebar is pressed..
                if inventory is 'Full':       # For firing attack, our inventory must be full
                    attackx = playerx         # For const x coord of fired attack
                    attack( attackx, attacky) # Calling attack function
                    Firing = mixer.Sound('FireSound.mp3')   # We used mixer.Sound because this sound should be heard with BGM
                    Firing.play()

        if event.type == pygame.KEYUP:        # Keyup is for checking whether any pressed key is released or not

            if (event.key == pygame.K_LEFT):  # When we release left key,
                deltaXplayer = 0              # change in x coord of player must be zero
            if (event.key == pygame.K_RIGHT): # When we release right key,
                deltaXplayer = 0              # change in x coord of player must be zero

    # _______________________________________________________________________________________

        playerx += deltaXplayer     # To keep player updated with change in x coord

        # Checking for boundaries for player so it don't go out of the screen
        if playerx <= 64:
            playerx = 64
        elif playerx >= screenx-64:
            playerx = screenx-64

    # _______________________________________________________________________________________

    # We have to call enemy only once so we've written it in running while loop
    # We have used for loop for iterating over each enemy

    for i in range(numOfEnemies):

        # _______________________________________________________________________________________

        # To Over the Game
        if GOcheck( enemyx[i] , enemyy[i] , playerx , playery ):  # If An enemy hits player...
            for i in range(numOfEnemies):                         # Disappears all enemies from screen
                enemyx[i] = 1400
                enemyy[i] = 1200
                speedx = 0
                speedy = 0
            got = True
            break

        enemy( enemyx[i] , enemyy[i] )  # Calls enemy function for An enemy

        enemyx[i] += deltaXenemy[i]     # An Enemy will continuously move in x direction
        enemyy[i] += deltaYenemy[i]     # An Enemy will continuously move in y direction

        # _______________________________________________________________________________________

        # Checking for boundaries for An enemy so it don't go out of the screen
        if enemyx[i] <= 0:
                deltaXenemy[i] =  speedx
        elif enemyx[i] >= screenx-65:
                deltaXenemy[i] = 0 - speedx
        
        if enemyy[i] <= 0:
                deltaYenemy[i] =  speedy
        elif enemyy[i] >= screeny-65:
                deltaYenemy[i] = 0 - speedy
    
        # _______________________________________________________________________________________

        # If Attack Hits an enemy
        if hit( enemyx[i] , enemyy[i] , attackx , attacky ) and (inventory is 'Empty'):   # If we've alredy fired and hit happens
                Currentscore += 1
                attacky = playery
                inventory = 'Full'
                enemyx[i] = (random.randint(65,screenx-65))
                enemyy[i] = (random.randint(65,screeny-251))
                Boom = mixer.Sound('BoomSound.mp3')
                Boom.play()
    
    # _______________________________________________________________________________________


    # To display text after Game Over
    if got:     # If game just overed
        GOdisp()
    
    # Atttack movement and its attributes
    if attacky <= 0 :
        attacky = playery
        inventory = 'Full'
    if inventory is 'Empty':
        attack( attackx , attacky)
        attacky -= deltaYattack

    # Keeping updating screen with every single data that can have been changed so far

    pygame.display.update()

    # _______________________________________________________________________________________








    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
    # _______________________________________________________________________________________
