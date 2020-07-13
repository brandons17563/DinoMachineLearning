import pygame
pygame.init()

win = pygame.display.set_mode((500, 500)) #sets size of the screen
pygame.display.set_caption("First Game") #sets title of the game

x = 50
y = 425
width = 64
height = 64
vel = 5

#character moving variables
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


# image upload for character sprite and background
# to upload images from a folder you can do pygame.image.load(pygame.path.join('<folder>','<file>'))
# OR include the path of the file in the pygame.image.load line

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()#allows us to change the fps in our game

def redrawGameWindow():
    global walkCount
    # win.fill((0,0,0)) #prevents trail of object
    win.blit(bg,(0,0))#displays the background. win.blit() is also how you display all images in pygame

    if walkCount + 1 >= 27: #would run into an index error if >27 because our frameRate will be 27 fps
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char,(x,y))
    # pygame.draw.rect(win,(255, 0, 0), (x,y,width,height)) #creates a rectangle object
    pygame.display.update() #updates the display to show the rectangle

run = True
while run: #runs the game
    clock.tick(27) # sets fps to 27
    # pygame.time.delay(50) #allows for things to move slower

    for event in pygame.event.get(): #handles quitting the game
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed() #list of keys

    if keys[pygame.K_LEFT] and x > vel: #contains object on the screen
        x-= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x+=vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump): #runs this code if person is not jumping
#        if keys[pygame.K_UP] and y > vel:
#            y-=vel
#        if keys[pygame.K_DOWN] and y < 500 - height - vel:
#            y+=vel
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else: #runs this code when the person is jumping
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y-= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    redrawGameWindow()
pygame.quit()
