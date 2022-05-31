import pygame
from sys import exit

pygame.init()
# !view docs: python -m pygame.docs
# !import/initiate pygame

# !display surface(window)
screen = pygame.display.set_mode((800, 400))
#                     window width^    ^height of the window
# sets window name
pygame.display.set_caption('Game title here')
# set framerate
clock = pygame.time.Clock()

# !fonts
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
#                   font type^,     ^ font size

# !import surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('text', False, 'Black').convert()
#                              text^    ^AA     ^color
text_rect = text_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x = 600
snail_rect = snail_surface.get_rect(midbottom=(150, 300))

# ! convert alpha is == to png (removes white and black bgrd)
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

# !create a rectangle:
player_rect = player_surface.get_rect(center=(80, 300))
# marks which point of the rectange needs to be touching whatever coordinate (idk a better way to explain it)

# !keyboard input

# !gravity:
player_gravity = 0

# draw all element
# runs window forever
while True:
    # loops thru all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys exit to stop pygame error (video system not initalized)
            exit()
        # constantly prints mouse pos
        if event.type == pygame.MOUSEMOTION:  # other params are buttonup or buttondown
            pass
        # !keyboard input:
        # keydown is when pressed keyup is when released
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    print(type(player_rect))
    print(player_rect)
    # gravity in loop:
    player_gravity += 1
    player_rect.y += player_gravity

    if player_rect.bottom >= 300:
        player_rect.y = 300

    # !code to display assets/objects
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, 'Pink', text_rect, 10)
    pygame.draw.rect(screen, 'Pink', text_rect)
    screen.blit(text_surface, text_rect)

    # !blit with the rectangle
    screen.blit(player_surface, player_rect)
    # moves player same way as line 56
    # player_rect.left += 1

    # !animated:
    # every second updates x position by 1
    screen.blit(snail_surface, snail_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    # !collisions
    # if player_rect.colliderect(snail_rect):
    #    print('collided')

    # !collidepoint is for cursor collision

    # !get mouse pos
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        # shows tuple of mouse button pressed
        print(pygame.mouse.get_pressed())

    # if snail X pos gets further than coord -100 it returns to coord 800
    '''
    if snail_x < -100:
        snail_x = 800

    screen.blit(snail_surface,(snail_x,200))
    '''

    # puts everything onto the display
    pygame.display.update()
    # adds framerate to game
    clock.tick(60)
