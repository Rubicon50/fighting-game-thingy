import pygame, BaseScene
        
def charselect():
    WIDTH, HEIGHT = 1280, 720
    SCREEN = pygame.display.set_mode((WIDTH/1,HEIGHT/1))
    WIN = pygame.surface.Surface((WIDTH, HEIGHT))
    FPS = 60
    selectBackground = pygame.image.load("assets/backgrounds/charselect.png")
    shikibutton = pygame.image.load("assets/button icons/shikibutton.png")
    char2button = pygame.image.load("assets/button icons/char2button.png")
    player1text = pygame.image.load("assets/button icons/player1select.png")
    player2text = pygame.image.load("assets/button icons/player2select.png")
    buttons = [shikibutton,char2button]
    looping = True
    selected = [buttons[0]]
    brighten = 128
    dim = 128
    char2button.fill((dim, dim, dim), special_flags=pygame.BLEND_RGB_SUB)
    playerchoosing = 1
    pygame.mixer.init()
    pygame.mixer.music.load("assets/music/Actor's Anteroom.mp3")
    pygame.mixer.music.play()
    while looping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                looping = False
             
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if selected != buttons[0]:
                        #if you press up and aren't on shikibutton, that means you're on char2. This moves you back to shikibutton.
                        selected = buttons[0]
                        shikibutton.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD)
                        char2button.fill((dim, dim, dim), special_flags=pygame.BLEND_RGB_SUB)  
                    elif selected != buttons[1]:
                        #if you press up and aren't on char2button, that means you're on shikibutton. This moves you back to char2button.
                        selected = buttons[1]
                        char2button.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD) 
                        shikibutton.fill((dim, dim, dim), special_flags=pygame.BLEND_RGB_SUB) 
                if event.key == pygame.K_RIGHT:
                    if selected != buttons[1]:
                        #if you press down and aren't on char2button, that means you're on shikibutton. This moves you back to char2button.
                        selected = buttons[1]
                        char2button.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD) 
                        shikibutton.fill((dim, dim, dim), special_flags=pygame.BLEND_RGB_SUB) 
                    elif selected != buttons[0]:
                        #if you press down and aren't on shikibutton, that means you're on char2button. This moves you back to shikibutton.
                        selected = buttons[0]
                        shikibutton.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD) 
                        char2button.fill((dim, dim, dim), special_flags=pygame.BLEND_RGB_SUB) 
                if event.key == pygame.K_z:
                        if selected == buttons[0]:
                            if playerchoosing == 1:
                                player1char = "Shiki"
                                playerchoosing +=1
                                print("player1 is Shiki")
                                #adds 1 to the playerchoosing variable and returns to the top so player 2 can choose a character
                            elif playerchoosing == 2:
                                player2char = "Shiki"
                                print("player2 is Shiki")
                                #implement the code here to run basescene with the player1char and player2char variables so that baseScene can read it      
                        elif selected == buttons[1]:
                            if playerchoosing == 1:
                                player1char = "char2"
                                print("player1 is char2")
                                playerchoosing+=1
                            elif playerchoosing == 2:
                                player2char = "char2"
                                print("player2 is char2")
                                #code here for running basescene like above
        WIN.blit(selectBackground, (0,0))
        WIN.blit(shikibutton, (WIDTH/2 - 450, HEIGHT/2 - 63))
        WIN.blit(char2button, (WIDTH/2 +130, HEIGHT/2 - 50))
        if playerchoosing == 1:
            WIN.blit(player1text, (175,0))
        elif playerchoosing == 2:
            #I spent an embarassing amount of time trying to edit the number because paint3d sucks, the 2 is slightly too off-center, I do not care at this point
            WIN.blit(player2text, (175,0))
        SCREEN.blit(pygame.transform.scale(WIN, SCREEN.get_rect().size), (0, 0))
        pygame.display.flip()    

if __name__ == "main":
    charselect()