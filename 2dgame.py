import pygame 

pygame.init()
pygame.font.init()



screen = pygame.display.set_mode((800, 600))

playerIMG = pygame.image.load("C:\\Users\\ahsmi\\Desktop\\Pygame\\images\\project.jpg")
playerX = 0
playerY = 0
playerX_change = 0

clock = pygame.time.Clock()


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png'), pygame.image.load('R10.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png'), pygame.image.load('L10.png')]
walkFoward = [pygame.image.load('F1.png'), pygame.image.load('F2.png'), pygame.image.load('F3.png'), pygame.image.load('F4.png'), pygame.image.load('F5.png'), pygame.image.load('F6.png'), pygame.image.load('F7.png'), pygame.image.load('F8.png'), pygame.image.load('F9.png'), pygame.image.load('F10.png')]
walkBackward = [pygame.image.load('B1.png'), pygame.image.load('B2.png'), pygame.image.load('B3.png'), pygame.image.load('B4.png'), pygame.image.load('B5.png'), pygame.image.load('B6.png'), pygame.image.load('B7.png'), pygame.image.load('B8.png'), pygame.image.load('B9.png'), pygame.image.load('B10.png')]

bg = pygame.image.load('project.jpg')
BI = pygame.image.load('BI1.png')
FI = pygame.image.load('FI1.png')
LI = pygame.image.load('LI1.png')
RI = pygame.image.load('RI1.png')
DI = pygame.image.load('BI1.png')

walkCount = 0
left = False
right = False
foward = False
backward = False

my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('I need you to farm some crops [E]', False, (0, 0, 0))

x = 400
y = 300

xx = 00
yy = 00

def player(xx, yy):
    screen.blit(playerIMG, (xx, yy))



def farm():
    if -1640 < playerX < -1440  and -515 < playerY < -315:
        screen.blit(text_surface, (0,0))


def GameWindow():
    global walkCount
    
    

    if walkCount + 1 >= 30:
        walkCount = 0
        
    if left:  
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1  
        global DI
        DI = LI   
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
        DI = RI
    elif foward:
        screen.blit(walkFoward[walkCount//3], (x,y))
        walkCount += 1
        DI = FI
    elif backward:
        screen.blit(walkBackward[walkCount//3], (x,y))
        walkCount += 1
        DI = BI
    else:
        screen.blit(DI, (x, y))
        walkCount = 0
        
    pygame.display.update() 

run = True
while run:
    clock.tick(60)
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if playerX <= 412.5:
                playerX += 5
                left = True
                right = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if playerX >= -8770:
                playerX += -5
                right = True
                left = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if playerY <= 310:
                playerY += 5
                foward = True
                backward = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            if playerY  > -9875:
                playerY += -5
                backward = True
                foward  = False
    else:
        left = False
        right = False
        foward = False
        backward = False
        walkCount = 0


    screen.fill((0, 0, 0))
    
    player(playerX, playerY)
    GameWindow()
    print(playerX, " ", playerY)
    farm()
    pygame.display.update()