import pygame, characterselect, os

def titlescreen():
    WIDTH, HEIGHT = 1280, 720
    SCREEN = pygame.display.set_mode((WIDTH/1,HEIGHT/1))
    WIN = pygame.surface.Surface((WIDTH, HEIGHT))
    FPS = 60
    titleBackground = pygame.image.load("assets/titlescreen/title.png")
    startbutton = pygame.image.load("assets/titlescreen/startbutton.png")
    exitbutton = pygame.image.load("assets/titlescreen/exitbutton.png")
    buttons = [startbutton, exitbutton]
    looping = True
    selected = [buttons[0]]
    brighten = 128
    dim = 128
    exitbutton.fill((dim,dim,dim), special_flags=pygame.BLEND_RGB_SUB)
    pygame.mixer.init()
    pygame.mixer.music.load("assets/music/This Illusion.mp3")
    pygame.mixer.music.play()
    while looping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                looping = False
             
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if selected != buttons[0]:
                        #if you press up and aren't on startbutton, that means you're on char2. This moves you back to startbutton.
                        selected = buttons[0]
                        startbutton.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD)
                        exitbutton.fill((dim, dim, dim), special_flags=pygame.BLEND_RGB_SUB)  
                    elif selected != buttons[1]:
                        #if you press up and aren't on exitbutton, that means you're on startbutton. This moves you back to exitbutton.
                        selected = buttons[1]
                        exitbutton.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD) 
                        startbutton.fill((dim, dim, dim), special_flags=pygame.BLEND_RGB_SUB) 
                if event.key == pygame.K_RIGHT:
                    if selected != buttons[1]:
                        #if you press down and aren't on exitbutton, that means you're on startbutton. This moves you back to exitbutton.
                        selected = buttons[1]
                        exitbutton.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD) 
                        startbutton.fill((dim, dim, dim), special_flags=pygame.BLEND_RGB_SUB) 
                    elif selected != buttons[0]:
                        #if you press down and aren't on startbutton, that means you're on exitbutton. This moves you back to startbutton.
                        selected = buttons[0]
                        startbutton.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD) 
                        exitbutton.fill((dim, dim, dim), special_flags=pygame.BLEND_RGB_SUB) 
                if event.key == pygame.K_z:
                        if selected == buttons[0]:
                            characterselect.charselect()   
                        elif selected == buttons[1]:
                            os.close(2)
        WIN.blit(titleBackground, (0,0))
        WIN.blit(startbutton, (WIDTH/2 - 300, HEIGHT/2 + 90))
        WIN.blit(exitbutton, (WIDTH/2 + 100, HEIGHT/2 + 90))
        SCREEN.blit(pygame.transform.scale(WIN, SCREEN.get_rect().size), (0, 0))
        pygame.display.flip()    
                                            


titlescreen()