import pygame, sys
from button import Button

music_file = "assets/bensound-funkyelement.mp3"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

pygame.init()

SCREEN = pygame.display.set_mode((1000, 707))   #(1280, 720)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/wallpaper.jpg")
cat = pygame.image.load("assets/cat.jpg")
Mus = pygame.image.load("assets/Museum Interior (1).jpg")
col_1 = "Orange"
col_2 = "Green"

villain = "Cathlene Magic"
hero = "Superhero"
points = 0

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/BADABB__.TTF", size)

def get_font2(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Hey Comic.ttf", size)


def play():
#CHAPTER 1
    points = 0
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(60).render("Chapter 1: Mr.Whiskers", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(500, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(500, 430), 
                            text_input="Play", font=get_font(80), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        #global points
        #points = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    play_screen1()#main_menu()

        pygame.display.update()

def play_screen1():

    #import time

    
    
    #print("CITIZEN: Oh, thank goodness you're here! " + villain
    #      + " is destroying our city and we need your help to stop them!")
    #time.sleep(2)
    #hero = input("What is your name, superhero?\n")
    #print("Welcome " + hero + "!")
     #counting sustainability points
    #def chooseanswer():  #input validation
    #    time.sleep(2)
    #    answer = ""
    #    while answer != "A" and answer != "B":
    #        answer = input("Choose A or B\n") #make upper case
    #        answer = answer.upper()
    #    return answer

#Game starts

    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        #Dialogue 1
        screen_text11 = get_font2(30).render("CITIZEN- Oh, thank goodness you're here!", True, "Black")
        screen_rect11 = screen_text11.get_rect(center=(350, 100))  #(200, 100))   #(640, 260))
        SCREEN.blit(screen_text11, screen_rect11)

        screen_text12 = get_font2(30).render(villain + " is destroying our city and we need your", True, "Black")
        screen_rect12 = screen_text11.get_rect(center=(350, 175))   #(640, 280))
        SCREEN.blit(screen_text12, screen_rect12)


        screen_text13 = get_font2(30).render("help to stop them!", True, "Black")
        screen_rect13 = screen_text11.get_rect(center=(350, 210))   #(640, 280))
        SCREEN.blit(screen_text13, screen_rect13)
        

        NEXT = Button(image=None, pos=(770, 500), 
                            text_input="Next", font=get_font(60), base_color= col_1, hovering_color= col_2)

        NEXT.changeColor(PLAY_MOUSE_POS)
        NEXT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT.checkForInput(PLAY_MOUSE_POS):
                    player()

        pygame.display.update()
    """
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        
        PLAY_TEXT = get_font(20).render("CITIZEN: Oh, thank goodness you're here! " + villain
          + " is destroying our city and we need your help to stop them!", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        optionA = Button(image=None, pos=(640, 460), 
                            text_input="Did " +
      villain + " put him there?!", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

    """
def player():
#Player Introduction
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        screen_text11 = get_font2(30).render("Welcome Superhero!", True, "Black")
        screen_rect11 = screen_text11.get_rect(center=(330, 100))   #(640, 260))
        SCREEN.blit(screen_text11, screen_rect11)

        #name = input()

        #screen_text12 = get_font2(30).render("Welcome " + hero + "!", True, "Black")  #hero
        #screen_rect12 = screen_text11.get_rect(center=(330, 200))   #(640, 280))
        #SCREEN.blit(screen_text12, screen_rect12)

        

        NEXT = Button(image=None, pos=(770, 500), 
                            text_input="Next", font=get_font(60), base_color="Orange", hovering_color="Green")

        NEXT.changeColor(PLAY_MOUSE_POS)
        NEXT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT.checkForInput(PLAY_MOUSE_POS):
                    play_screen2()

        pygame.display.update()

def play_screen2():
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        #Dialogue 2 - Choice 1
        screen_text21 = get_font2(30).render("CITIZEN- First things first: my darling cat Mr Whiskers", True, "Black")
        screen_text22 = get_font2(30).render("is stuck up a tree!", True, "Black")

        screen_rect21 = screen_text21.get_rect(center=(500,100))  #(350, 100))   #(640, 260))
        SCREEN.blit(screen_text21, screen_rect21)
        
        screen_rect22 = screen_text22.get_rect(center=(500, 150))   #(640, 260))
        SCREEN.blit(screen_text22, screen_rect22)
        

        CHOICE1 = Button(image=None, pos=(400, 470), 
                            text_input="Did "+villain+" put him there?!", font=get_font2(35), base_color="Orange", hovering_color="Green")

        CHOICE2 = Button(image=None, pos=(400, 550), 
                            text_input="On it!", font=get_font2(35), base_color="Orange", hovering_color="Green")

        for button in [CHOICE1, CHOICE2]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(PLAY_MOUSE_POS):
                    play_screen3()
                if CHOICE2.checkForInput(PLAY_MOUSE_POS):
                    play_screen4()

        pygame.display.update()

def play_screen3():
#Screen 3 - Choice A for Dialogue 2
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        screen_text31 = get_font2(30).render("CITIZEN- Kind of? Mr Whiskers was out in the garden", True, "Black")
        screen_rect31 = screen_text31.get_rect(center=(500, 60))   #(640, 260))
        SCREEN.blit(screen_text31, screen_rect31)

        screen_text32 = get_font2(30).render(" when the sound of " +villain +" flying past startled", True, "Black")
        screen_rect32 = screen_text32.get_rect(center=(500, 100))   #(640, 280))
        SCREEN.blit(screen_text32, screen_rect32)

        
        screen_text33 = get_font2(30).render("him and caused him to climb up the tree!", True, "Black")
        screen_rect33 = screen_text33.get_rect(center=(500, 140))   #(640, 280))
        SCREEN.blit(screen_text33, screen_rect33)

        screen_text34 = get_font2(30).render("Anyway, you better head to the cat now!", True, "Black")
        screen_rect34 = screen_text34.get_rect(center=(500, 200))   #(640, 280))
        SCREEN.blit(screen_text34, screen_rect34)


        NEXT = Button(image=None, pos=(770, 500), 
                            text_input="Next", font=get_font(60), base_color="Orange", hovering_color="Green")

        NEXT.changeColor(PLAY_MOUSE_POS)
        NEXT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT.checkForInput(PLAY_MOUSE_POS):
                    play_screen4()

        pygame.display.update()

def play_screen4():
#Screen 4 - Choice B for Dialogue 2 (also what comes after choice A)
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        
        screen_text1 = get_font2(30).render("As you approach the citizen's house, you see a scared-looking", True, "Black")
        screen_rect1 = screen_text1.get_rect(center=(500 , 50))   #(640, 260))
        SCREEN.blit(screen_text1, screen_rect1)

        screen_text2 = get_font2(30).render("black cat perched on top of a very frail-looking tree.", True, "Black")
        screen_rect2 = screen_text2.get_rect(center=(500, 80))   #(640, 360))
        SCREEN.blit(screen_text2, screen_rect2)

        screen_text3 = get_font2(30).render("Close to the tree, you spot two objects: a ladder and a saw.", True, "Black")
        screen_rect3 = screen_text3.get_rect(center=(500, 150))   #(640, 360))
        SCREEN.blit(screen_text3, screen_rect3)
        
        screen_text4 = get_font2(30).render("Which do you pick?", True, "Black")
        screen_rect4 = screen_text4.get_rect(center=(500, 190))   #(640, 360))
        SCREEN.blit(screen_text4, screen_rect4)
        
        

        CHOICE1 = Button(image=None, pos=(400, 440), #220, 440
                            text_input="Ladder", font=get_font2(50), base_color="Orange", hovering_color="Green")

        CHOICE2 = Button(image=None, pos=(400, 550), 
                            text_input="Saw", font=get_font2(50), base_color="Orange", hovering_color="Green")

        for button in [CHOICE1, CHOICE2]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(PLAY_MOUSE_POS):
                    play_screen5()
                if CHOICE2.checkForInput(PLAY_MOUSE_POS):
                    play_screen11()

        pygame.display.update()


def play_screen5():
#Screen 5 - Choose Ladder
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        
        screen_text1 = get_font2(30).render(hero +"- There's a ladder right there.", True, "Black")
        screen_rect1 = screen_text1.get_rect(center=(500, 30))   #(640, 260))
        SCREEN.blit(screen_text1, screen_rect1)

        screen_text2 = get_font2(30).render("CITIZEN- Yeah, but it's broken. You can buy a new one from", True, "Black")
        screen_rect2 = screen_text2.get_rect(center=(500, 90))   #(640, 360))
        SCREEN.blit(screen_text2, screen_rect2)

        screen_text3 = get_font2(30).render("the shop next door - I'll give you the money - or borrow one", True, "Black")
        screen_rect3 = screen_text3.get_rect(center=(500, 140))   #(640, 360))
        SCREEN.blit(screen_text3, screen_rect3)

        screen_text4 = get_font2(30).render("from Ms Smith, who lives two blocks away.", True, "Black")
        screen_rect4 = screen_text4.get_rect(center=(500, 190))   #(640, 360))
        SCREEN.blit(screen_text4, screen_rect4)
        
         

        CHOICE1 = Button(image=None, pos=(400, 470), 
                            text_input="Use a ladder", font=get_font2(35), base_color="Orange", hovering_color="Green")

        CHOICE2 = Button(image=None, pos=(400, 550), 
                            text_input="Change your mind and use a saw", font=get_font2(35), base_color="Orange", hovering_color="Green")

        for button in [CHOICE1, CHOICE2]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(PLAY_MOUSE_POS):
                    play_screen6()
                if CHOICE2.checkForInput(PLAY_MOUSE_POS):
                    play_screen11()

        pygame.display.update()

def play_screen6():
#Screen 6 - Choose Ladder twice
    #########change positions of borrow and buy
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))
        
        screen_text1 = get_font2(30).render("Do you want to buy a new one or borrow one from Ms Smith?", True, "Black")
        screen_rect1 = screen_text1.get_rect(center=(500, 100))   #(640, 260))
        SCREEN.blit(screen_text1, screen_rect1)

        CHOICE1 = Button(image=None, pos=(400, 440), 
                            text_input="Borrow", font=get_font2(50), base_color="Orange", hovering_color="Green")

        CHOICE2 = Button(image=None, pos=(440, 550), 
                            text_input="Buy", font=get_font2(50), base_color="Orange", hovering_color="Green")

        for button in [CHOICE1, CHOICE2]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        global points

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(PLAY_MOUSE_POS):
                    play_screen8()
                if CHOICE2.checkForInput(PLAY_MOUSE_POS):
                    points += 1
                    play_screen7()

        pygame.display.update()
#print(points)

def play_screen7():
#Screen 7 - Choose Buy Ladder
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        
        screen_text1 = get_font2(30).render("The citizen gives you the money and you go buy a ladder", True, "Black")
        screen_rect1 = screen_text1.get_rect(center=(500, 50))   #(640, 260))
        SCREEN.blit(screen_text1, screen_rect1)

        screen_text2 = get_font2(28).render("Using the new ladder, you successfully rescue Mr Whiskers from the tree.", True, "Black")
        screen_rect2 = screen_text2.get_rect(center=(500, 100))   #(640, 360))
        SCREEN.blit(screen_text2, screen_rect2)

        screen_text3 = get_font2(30).render("from the shop. Using the new ladder, you successfully", True, "Black")
        screen_rect3 = screen_text3.get_rect(center=(500, 150))   #(640, 360))
        SCREEN.blit(screen_text3, screen_rect3)

        screen_text4 = get_font2(30).render("rescue Mr Whiskers from the tree.", True, "Black")
        screen_rect4 = screen_text4.get_rect(center=(500, 200))   #(640, 360))
        SCREEN.blit(screen_text4, screen_rect4)

          
        script = "You know, you shouldn't really let your cat out of your house. \nIt could get hit by cars, catch diseases and kill the local wildlife."
        CHOICE1 = Button(image=None, pos=(500, 460),                        
                            text_input=script, font=get_font2(16), base_color="Orange", hovering_color="Green")

        CHOICE2 = Button(image=None, pos=(400, 550),
                            text_input="Task number one completed! See you later Mr Whiskers!", font=get_font2(20), base_color="Orange", hovering_color="Green")

        for button in [CHOICE1, CHOICE2]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        
        global points
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(PLAY_MOUSE_POS):
                    points += 2
                    part1_end1()
                if CHOICE2.checkForInput(PLAY_MOUSE_POS):
                    part1_end2()

        pygame.display.update()
        

def play_screen8():
#Screen 8 - Choose Borrow Ladder
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))
        
        screen_text1 = get_font2(30).render("CITIZEN: Great! I'll let you ride my car - unless ", True, "Black")
        screen_rect1 = screen_text1.get_rect(center=(500, 100))   #(640, 260))
        SCREEN.blit(screen_text1, screen_rect1)

        screen_text2 = get_font2(30).render("you want to walk?", True, "Black")
        screen_rect2 = screen_text2.get_rect(center=(500, 150))   #(640, 360))
        SCREEN.blit(screen_text2, screen_rect2)


        CHOICE1 = Button(image=None, pos=(400, 440), 
                            text_input="Walk", font=get_font2(50), base_color="Orange", hovering_color="Green")

        CHOICE2 = Button(image=None, pos=(400, 550), 
                            text_input="Car", font=get_font2(50), base_color="Orange", hovering_color="Green")

        for button in [CHOICE1, CHOICE2]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        
        global points

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(PLAY_MOUSE_POS):
                    points += 5
                    play_screen9()
                if CHOICE2.checkForInput(PLAY_MOUSE_POS):
                    points += 3
                    play_screen10()

        pygame.display.update()

def play_screen9():
#Screen 9 - Choose Walk
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        
        screen_text1 = get_font2(30).render("You walk to Ms Smith's house and borrow her ladder.", True, "Black")
        screen_rect1 = screen_text1.get_rect(center=(500, 50))   #(640, 260))
        SCREEN.blit(screen_text1, screen_rect1)

        screen_text2 = get_font2(30).render("You walk back to the citizen's house and succesfully", True, "Black")
        screen_rect2 = screen_text2.get_rect(center=(500, 125))   #(640, 360))
        SCREEN.blit(screen_text2, screen_rect2)

        screen_text3 = get_font2(30).render("rescue Mr Whiskers from the tree", True, "Black")
        screen_rect3 = screen_text3.get_rect(center=(500, 175))   #(640, 360))
        SCREEN.blit(screen_text3, screen_rect3)

         
        

        CHOICE1 = Button(image=None, pos=(500, 500), 
                            text_input="You know, you shouldn't really let your cat out of your house. \nIt could get hit by cars, catch diseases and " +
         "kill the local wildlife.", font=get_font2(16), base_color="Orange", hovering_color="Green")

        CHOICE2 = Button(image=None, pos=(400, 550), 
                            text_input="Task number one completed! See you later Mr Whiskers!", font=get_font2(20), base_color="Orange", hovering_color="Green")

        for button in [CHOICE1, CHOICE2]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        global points

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(PLAY_MOUSE_POS):
                    points += 2
                    part1_end1()
                if CHOICE2.checkForInput(PLAY_MOUSE_POS):
                    part1_end2()

        pygame.display.update()

def play_screen10():
#Screen 10 - Choose Car
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        
        screen_text1 = get_font2(30).render("You ride to Ms Smith's house and borrow her ladder.", True, "Black")
        screen_rect1 = screen_text1.get_rect(center=(500, 50))   #(640, 260))
        SCREEN.blit(screen_text1, screen_rect1)

        screen_text2 = get_font2(30).render("You ride back to the citizen's house and succesfully", True, "Black")
        screen_rect2 = screen_text2.get_rect(center=(500, 125))   #(640, 360))
        SCREEN.blit(screen_text2, screen_rect2)

        screen_text3 = get_font2(30).render("rescue Mr Whiskers from the tree.", True, "Black")
        screen_rect3 = screen_text3.get_rect(center=(500, 175))   #(640, 360))
        SCREEN.blit(screen_text3, screen_rect3)
        

        CHOICE1 = Button(image=None, pos=(500, 500), 
                            text_input="You know, you shouldn't really let your cat out of your house. \nIt could get hit by cars, catch diseases and " +
         "kill the local wildlife.", font=get_font2(16), base_color="Orange", hovering_color="Green")

        CHOICE2 = Button(image=None, pos=(400, 550), 
                            text_input="Task number one completed! See you later Mr Whiskers!", font=get_font2(20), base_color="Orange", hovering_color="Green")

        for button in [CHOICE1, CHOICE2]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        global points

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(PLAY_MOUSE_POS):
                    points += 2
                    part1_end1()
                if CHOICE2.checkForInput(PLAY_MOUSE_POS):
                    part1_end2()

        pygame.display.update()


def play_screen11():
#Screen 11 - Choose Saw
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        
        screen_text1 = get_font2(30).render("Using the saw, you cut down the tree.", True, "Black")
        screen_rect1 = screen_text1.get_rect(center=(500, 100))   #(640, 260))
        SCREEN.blit(screen_text1, screen_rect1)
        

        screen_text2 = get_font2(30).render("As it falls, Mr Whiskers jumps to the ground and runs", True, "Black")
        screen_rect2 = screen_text2.get_rect(center=(500, 175))   #(640, 360))
        SCREEN.blit(screen_text2, screen_rect2)

        screen_text3 = get_font2(30).render("back inside the citizen's house.", True, "Black")
        screen_rect3 = screen_text3.get_rect(center=(500, 225))   #(640, 360))
        SCREEN.blit(screen_text3, screen_rect3)

        

        global points
        points = - 5

        CHOICE1 = Button(image=None, pos=(500, 500), 
                            text_input="You know, you shouldn't really let your cat out of your house. \nIt could get hit by cars, catch diseases and " +
         "kill the local wildlife.", font=get_font2(16), base_color="Orange", hovering_color="Green")

        CHOICE2 = Button(image=None, pos=(400, 550), 
                            text_input="Task number one completed! See you later Mr Whiskers!", font=get_font2(20), base_color="Orange", hovering_color="Green")

        for button in [CHOICE1, CHOICE2]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(PLAY_MOUSE_POS):
                    points += 2
                    part1_end1()
                if CHOICE2.checkForInput(PLAY_MOUSE_POS):
                    part1_end2()

        pygame.display.update()


def part1_end1():
#Ending 1
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        global points
        #print(points)

        screen_text11 = get_font2(30).render("CITIZEN- You're right " + hero + ", I promise that ", True, "Black")
        screen_rect11 = screen_text11.get_rect(center=(500, 100))   #(640, 260))
        SCREEN.blit(screen_text11, screen_rect11)
        
        
        screen_text12 = get_font2(30).render("from now on Mr Whiskers will stay inside.", True, "Black")
        screen_rect12 = screen_text11.get_rect(center=(500, 150))   #(640, 280))
        SCREEN.blit(screen_text12, screen_rect12)
        
        
        #screen_text13 = get_font2(30).render("End of Chapter 1 Total score: " + str(points)+"/7", True, "Black")
        #screen_rect13 = screen_text13.get_rect(center=(500, 250))   #(640, 280))
        #SCREEN.blit(screen_text13, screen_rect13)
        

        CONTINUE = Button(image=None, pos=(760, 500), 
                            text_input="Continue", font=get_font(60), base_color="Orange", hovering_color="Green")

        CONTINUE.changeColor(PLAY_MOUSE_POS)
        CONTINUE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE.checkForInput(PLAY_MOUSE_POS):
                    play2()

        pygame.display.update()

def part1_end2():
#Ending 2
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(cat, (0, 0))

        global points
        #print(points)

        screen_text11 = get_font2(30).render("CITIZEN- You go " + hero + "!", True, "Black")
        screen_rect11 = screen_text11.get_rect(center=(500, 100))   #(640, 260))
        SCREEN.blit(screen_text11, screen_rect11)

        #screen_text12 = get_font2(30).render("End of Chapter 1\nTotal score: " + str(points)+"/7", True, "Black")
        #screen_rect12 = screen_text11.get_rect(center=(500, 200))   #(640, 280))
        #SCREEN.blit(screen_text12, screen_rect12)
        

        CONTINUE = Button(image=None, pos=(760, 500), 
                            text_input="Next", font=get_font(60), base_color="Orange", hovering_color="Green")

        CONTINUE.changeColor(PLAY_MOUSE_POS)
        CONTINUE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE.checkForInput(PLAY_MOUSE_POS):
                    play2()

        pygame.display.update()

    
###########################################################    
#def options():
 #   while True:
  #      OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

   #     SCREEN.fill("white")

    #    OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
     #   OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
      #  SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

       # OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                           # text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        #OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        #OPTIONS_BACK.update(SCREEN)

       # for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
         #       pygame.quit()
          #      sys.exit()
           # if event.type == pygame.MOUSEBUTTONDOWN:
            #    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                  #  main_menu()
#
        #pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Local Superhero", True, "Red")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

#makes various buttons
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="Start", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        #OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                           # text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

#dont change anything under here
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
#switches to different functions i.e. screens for each button
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

#main_menu()

###################### Chapter Two #############################
import pygame, sys
from button import Button


pygame.init()

SCREEN = pygame.display.set_mode((1000, 707))   #(1280, 720)
pygame.display.set_caption("Local Superhero")

BG = pygame.image.load("assets/wallpaper.jpg")
font = pygame.font.Font("assets/Hey Comic.TTF", 30)
#def get_font(size): # Returns Press-Start-2P in the desired size
    #return pygame.font.Font("assets/Hey Comic.TTF", size)

#usertxt = ''

#points = 100

def play2():
    

    
    
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = pygame.image.load("assets/cat.jpg")
        SCREEN.blit(ch1_bg, (0, 0))

        PLAY_TEXT = get_font(100).render("End of Chapter 1", True, "Red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(550, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        screen_text12 = get_font2(30).render("Total score: " + str(points)+"/7", True, "Black")
        screen_rect12 = screen_text12.get_rect(center=(500, 200))   #(640, 280))
        SCREEN.blit(screen_text12, screen_rect12)
        


        PLAY_BACK = Button(image=None, pos=(850, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        
        PLAY_NEXT = Button(image=None, pos=(650, 600), 
                            text_input="NEXT", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_NEXT.changeColor(PLAY_MOUSE_POS)
        PLAY_NEXT.update(SCREEN)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_NEXT.checkForInput(PLAY_MOUSE_POS):
                    ch2_1()

        pygame.display.update()

def ch2_1():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

        PLAY_TEXT = get_font2(60).render("Chapter 2: Going to the Museum", True, "Red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(500, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_TEXT1 = get_font2(30).render("CITIZEN- Good morning Superhero!", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("Would you fancy a trip to the Museum?", True, "Purple") 
        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 250))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)


        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="Isn't the city under attack by Cathlene Magic?", font=get_font2(30), base_color="Orange", hovering_color="Green")

        PLAY_B = Button(image=None, pos=(500, 510), 
                            text_input="Sure thing!", font=get_font2(30), base_color="Orange", hovering_color="Green")


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

        PLAY_B.changeColor(PLAY_MOUSE_POS)
        PLAY_B.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    ch2_2()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_B.checkForInput(PLAY_MOUSE_POS):
                    ch2_2_5()

        pygame.display.update()


def ch2_2():
    global points
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

      

        PLAY_TEXT1 = get_font2(27).render("CITIZEN- Not at this exact second, no. It'll probably be in around 3 to 5 hours", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("though - Cathlene Magic likes to attack in the afternoon.", True, "Purple") 
        PLAY_TEXT3 = get_font2(30).render("I thought a nice trip to the Museum would be preferable to", True, "Purple") 
        PLAY_TEXT4 = get_font2(30).render("us sitting around twiddling our thumbs.", True, "Purple")
        PLAY_TEXT5 = get_font2(30).render("Ok, let's go! Fancy a trip on my car?", True, "Purple")
                            
        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 100))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 150))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)

        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        PLAY_RECT4 = PLAY_TEXT4.get_rect(center=(500, 250))
        SCREEN.blit(PLAY_TEXT4, PLAY_RECT4)

        PLAY_RECT5 = PLAY_TEXT5.get_rect(center=(500, 300))
        SCREEN.blit(PLAY_TEXT5, PLAY_RECT5)


        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="Only if I get to choose the music!", font=get_font2(30), base_color="Orange", hovering_color="Green")

        PLAY_B = Button(image=None, pos=(500, 500), 
                            text_input="How about we take the tube instead?", font=get_font2(30), base_color="Orange", hovering_color="Green")


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

        PLAY_B.changeColor(PLAY_MOUSE_POS)
        PLAY_B.update(SCREEN)

    


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    points = points - 1
                    ch2_3()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_B.checkForInput(PLAY_MOUSE_POS):
                    points += 2
                    ch2_3()
                    
                    

        pygame.display.update()

def ch2_2_5():
    global points
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

      

        
        PLAY_TEXT1 = get_font2(30).render("Ok, let's go! Fancy a trip on my car?", True, "Purple")
                            
        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
        
        
        PLAY_A = Button(image=None, pos=(500, 400), 
                            text_input="Only if I get to choose the music!", font=get_font2(30), base_color="Orange", hovering_color="Green")

        PLAY_B = Button(image=None, pos=(500, 450), 
                            text_input="How about we take the tube instead?", font=get_font2(30), base_color="Orange", hovering_color="Green")


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

        PLAY_B.changeColor(PLAY_MOUSE_POS)
        PLAY_B.update(SCREEN)

   


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    points = points - 1
                    ch2_3()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_B.checkForInput(PLAY_MOUSE_POS):
                    points += 2
                    ch2_3()
                    
                    

        pygame.display.update()



def ch2_3():
    global points
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

        
        PLAY_TEXT1 = get_font2(30).render("CITIZEN- Sure thing Superhero!", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("Oh, wait! I just remembered that I left the lights on in the living room!", True, "Purple")   

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_RECT2 = PLAY_TEXT1.get_rect(center=(220, 250))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)


        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="Go turn them off, I'll wait", font=get_font2(30), base_color="Orange", hovering_color="Green")

        PLAY_B = Button(image=None, pos=(500, 500), 
                            text_input="Forget about the lights - let's go!", font=get_font2(30), base_color="Orange", hovering_color="Green")


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

        PLAY_B.changeColor(PLAY_MOUSE_POS)
        PLAY_B.update(SCREEN)

    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    points += 3
                    ch2_4()
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_B.checkForInput(PLAY_MOUSE_POS):
                    points = points - 2
                    ch2_5()
                    

        pygame.display.update()

def ch2_4():
    global points
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))


        PLAY_TEXT1 = get_font2(30).render("CITIZEN- Ok - I promise I won't be long!", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("I'm back! And ready to - oh no! I forgot my reusable coffee cup!", True, "Purple")   

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_RECT2 = PLAY_TEXT1.get_rect(center=(300, 300))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)


        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="Go grab it - quickly!", font=get_font2(30), base_color="Orange", hovering_color="Green")

        PLAY_B = Button(image=None, pos=(500, 500), 
                            text_input="A coffee cup? Forget it - we're gonna be late!", font=get_font2(30), base_color="Orange", hovering_color="Green")


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

        PLAY_B.changeColor(PLAY_MOUSE_POS)
        PLAY_B.update(SCREEN)

    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    points += 1
                    ch2_6()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_B.checkForInput(PLAY_MOUSE_POS):
                    ch2_7()
                    

        pygame.display.update()

def ch2_5():
    global points
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))


        PLAY_TEXT1 = get_font2(30).render("CITIZEN- You're right - we don't have much time until Cathlene Magic's attack. Let's go!", True, "Purple")
         

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)


        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="PART 2", font=get_font2(30), base_color="Orange", hovering_color="Green")

        


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    ch2_8()
           

        pygame.display.update()

def ch2_6():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))


        PLAY_TEXT1 = get_font2(30).render("CITIZEN- Ok!", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("I'm ready now - for real! Let's go!", True, "Purple")

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 300))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)


        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="PART 2", font=get_font2(30), base_color="Orange", hovering_color="Green")

        


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    ch2_8()
           

        pygame.display.update()

def ch2_7():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))


        PLAY_TEXT1 = get_font2(30).render("CITIZEN- Ok, ok - I'll just drink from a disposable cup. Let's go!", True, "Purple")
        

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        
        PLAY_A = Button(image=None, pos=(500, 400), 
                            text_input="PART 2", font=get_font2(30), base_color=col_1, hovering_color=col_2)

        


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    ch2_8()
           

        pygame.display.update()

def ch2_8():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

        PLAY_TEXT = get_font(80).render("At the Museum", True, "Red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(500, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)


        PLAY_TEXT1 = get_font2(30).render("CITIZEN- We're here Superhero!", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render(" What part of the Museum do you want to go to first?", True, "Purple")
           

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 250))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)



        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="I want to see the paintings!", font=get_font2(30), base_color=col_1, hovering_color=col_2)

        PLAY_B = Button(image=None, pos=(500, 500), 
                            text_input="I want to see the sculptures!", font=get_font2(30), base_color=col_1, hovering_color=col_2)


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

        PLAY_B.changeColor(PLAY_MOUSE_POS)
        PLAY_B.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    ch2_9()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_B.checkForInput(PLAY_MOUSE_POS):
                    ch2_10()

        pygame.display.update()

def ch2_9():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

      


        PLAY_TEXT1 = get_font2(30).render("CITIZEN- Me too! I think they're over this way.", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("You start walking in the direction that the citizen is pointing towards.", True, "Purple")
        PLAY_TEXT3 = get_font2(30).render("Suddenly, BOOM!", True, "Purple")
        PLAY_TEXT4 = get_font2(30).render("The room you were about to enter implodes - Cathlene Magic is here!", True, "Purple")
        PLAY_TEXT5 = get_font2(30).render("CITIZEN- Oh no - not the paintings!", True, "Purple")   

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 250))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)

        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(500, 300))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        PLAY_RECT4 = PLAY_TEXT4.get_rect(center=(500, 350))
        SCREEN.blit(PLAY_TEXT4, PLAY_RECT4)




        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="NEXT", font=get_font2(30), base_color=col_1, hovering_color=col_2)

        


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    ch2_11()
            

        pygame.display.update()

def ch2_10():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

      


        PLAY_TEXT1 = get_font2(30).render("CITIZEN- Me too! I think they're over this way.", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("You start walking in the direction that the citizen is pointing towards.", True, "Purple")
        PLAY_TEXT3 = get_font2(30).render("Suddenly, BOOM!", True, "Purple")
        PLAY_TEXT4 = get_font2(30).render("The room you were about to enter implodes - Cathlene Magic is here!", True, "Purple")
        PLAY_TEXT5 = get_font2(30).render("CITIZEN- Oh no - not the paintings!", True, "Purple")   

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 250))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)

        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(500, 300))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        PLAY_RECT4 = PLAY_TEXT4.get_rect(center=(500, 350))
        SCREEN.blit(PLAY_TEXT4, PLAY_RECT4)




        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="NEXT", font=get_font2(30), base_color=col_1, hovering_color=col_2)

        


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    ch2_11()
            

        pygame.display.update()


def ch2_11():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

  

        PLAY_TEXT1 = get_font2(29).render("Cathlene Magic- Muahaha! This whole Museum will be reduced to ashes!", True, "Purple")
           

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)



        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="Cower in fear", font=get_font2(30), base_color=col_1, hovering_color=col_2)

        PLAY_B = Button(image=None, pos=(500, 500), 
                            text_input="Charge towards Cathlene Magic", font=get_font2(30), base_color=col_1, hovering_color=col_2)


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

        PLAY_B.changeColor(PLAY_MOUSE_POS)
        PLAY_B.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    ch2_12()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_B.checkForInput(PLAY_MOUSE_POS):
                    ch2_12()

        pygame.display.update()

def ch2_12():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

  

        PLAY_TEXT1 = get_font2(30).render("CITIZEN- You can't do that Superhero!", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("Come on, follow me to the museum gift shop.", True, "Purple")
           

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 250))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)



        
        
        PLAY_A = Button(image=None, pos=(500, 450), 
                            text_input="What?", font=get_font2(30), base_color=col_1, hovering_color=col_2)

        PLAY_B = Button(image=None, pos=(500, 500), 
                            text_input="Why?", font=get_font2(30), base_color=col_1, hovering_color=col_2)


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)

        PLAY_B.changeColor(PLAY_MOUSE_POS)
        PLAY_B.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    ch2_13()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_B.checkForInput(PLAY_MOUSE_POS):
                    ch2_13()

        pygame.display.update()

def ch2_13():
    global points
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

      


        PLAY_TEXT1 = get_font2(30).render("You arrive at the gift shop and see that there's a beautiful sword", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("in the display case at the center.", True, "Purple")
        PLAY_TEXT3 = get_font2(30).render("You smile as you see it - with this, you are confident", True, "Purple")
        PLAY_TEXT4 = get_font2(30).render("that you can defeat Cathlene Magic.", True, "Purple")
        PLAY_TEXT5 = get_font2(30).render("You approach the display case.", True, "Purple")
        PLAY_TEXT6 = get_font2(30).render("SALESPERSON- Hello! Would you be interested in buying this sword?.", True, "Purple")
        PLAY_TEXT7 = get_font2(30).render("It costs ten points.", True, "Purple")
           

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 100))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 150))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)

        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        PLAY_RECT4 = PLAY_TEXT4.get_rect(center=(500, 250))
        SCREEN.blit(PLAY_TEXT4, PLAY_RECT4)

        PLAY_RECT5 = PLAY_TEXT5.get_rect(center=(500, 300))
        SCREEN.blit(PLAY_TEXT5, PLAY_RECT5)

        PLAY_RECT6 = PLAY_TEXT6.get_rect(center=(500, 350))
        SCREEN.blit(PLAY_TEXT6, PLAY_RECT6)

        PLAY_RECT7 = PLAY_TEXT7.get_rect(center=(500, 400))
        SCREEN.blit(PLAY_TEXT7, PLAY_RECT7)




        
        
        PLAY_A = Button(image=None, pos=(500, 500), 
                            text_input="You turn to the citizen and ask how many points you have.", font=get_font2(30), base_color=col_1, hovering_color= col_2)

        #Citizen needs to tell hero how many points they have


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)


        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    if points == 10:
                        good_end()
                    if points > 10:
                        good_end()
                    if points < 10:
                        bad_end()
                    
            

        pygame.display.update()

def good_end():
    global points
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

        script = "CITIZEN- You have " + str(points) + "! That's enough for the sword!"

        PLAY_TEXT0 = get_font2(30).render(script, True, "Purple")
        PLAY_TEXT1 = get_font2(30).render("The salesperson hands you the sword.", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("You rush to the room where Cathlene Magic is", True, "Purple")
        PLAY_TEXT3 = get_font2(30).render("destroying the art and strike them with your sword.", True, "Purple")
        PLAY_TEXT4 = get_font2(30).render("They scream and fall to the ground, disentegrating into a pile of ashes.", True, "Purple")
        PLAY_TEXT5 = get_font2(30).render("CITIZEN- Hah! Looks like you were the one who ended up", True, "Purple")
        PLAY_TEXT6 = get_font2(30).render("being reduced to a pile of ashes, Cathlene Magic!", True, "Purple")
        PLAY_TEXT7 = get_font2(29).render("As the citizen says this, you realise that Cathlene Magic is an anagram -" , True, "Purple")
        PLAY_TEXT8 = get_font2(30).render("the real villain was Climate Change all along!", True, "Purple")
  
           
        PLAY_RECT0 = PLAY_TEXT0.get_rect(center=(500, 150))
        SCREEN.blit(PLAY_TEXT0, PLAY_RECT0)

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 250))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)

        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(500, 300))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        PLAY_RECT4 = PLAY_TEXT4.get_rect(center=(500, 350))
        SCREEN.blit(PLAY_TEXT4, PLAY_RECT4)

        PLAY_RECT5 = PLAY_TEXT5.get_rect(center=(500, 400))
        SCREEN.blit(PLAY_TEXT5, PLAY_RECT5)

        PLAY_RECT6 = PLAY_TEXT6.get_rect(center=(500, 450))
        SCREEN.blit(PLAY_TEXT6, PLAY_RECT6)
        
        PLAY_RECT7 = PLAY_TEXT7.get_rect(center=(500, 500))
        SCREEN.blit(PLAY_TEXT7, PLAY_RECT7)

        
        PLAY_RECT8 = PLAY_TEXT8.get_rect(center=(500, 550))
        SCREEN.blit(PLAY_TEXT8, PLAY_RECT8)





        
        
        PLAY_A = Button(image=None, pos=(500, 650), 
                            text_input="THE END", font=get_font2(40), base_color=col_1, hovering_color=col_2)

        


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            

        pygame.display.update()

def bad_end():
    global points
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")
        ch1_bg = Mus
        SCREEN.blit(ch1_bg, (0, 0))

        script = "CITIZEN- You have " + str(points) + "! That's not enough for the sword!"

        PLAY_TEXT0 = get_font2(30).render(script, True, "Purple")
        PLAY_TEXT1 = get_font2(30).render("You beg with the salesperson, but they say ", True, "Purple")
        PLAY_TEXT2 = get_font2(30).render("that they are unable to give the sword a discount.", True, "Purple")
        PLAY_TEXT3 = get_font2(25).render("By the sound of the explosions, you can tell that Cathlene Magic is getting closer.", True, "Purple")
        PLAY_TEXT4 = get_font2(25).render("Suddenly, BOOM! The Museum's celing collapses. In your last moments, you realise - ", True, "Purple")
        PLAY_TEXT5 = get_font2(30).render("Cathelene Magic is an anagram - their real identity is Climate Change", True, "Purple")
           

        PLAY_RECT0 = PLAY_TEXT0.get_rect(center=(500, 150))
        SCREEN.blit(PLAY_TEXT0, PLAY_RECT0)

        PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(500, 200))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_RECT2 = PLAY_TEXT2.get_rect(center=(500, 250))
        SCREEN.blit(PLAY_TEXT2, PLAY_RECT2)

        PLAY_RECT3 = PLAY_TEXT3.get_rect(center=(500, 300))
        SCREEN.blit(PLAY_TEXT3, PLAY_RECT3)

        PLAY_RECT4 = PLAY_TEXT4.get_rect(center=(500, 350))
        SCREEN.blit(PLAY_TEXT4, PLAY_RECT4)

        PLAY_RECT5 = PLAY_TEXT5.get_rect(center=(500, 400))
        SCREEN.blit(PLAY_TEXT5, PLAY_RECT5)




        
        
        PLAY_A = Button(image=None, pos=(500, 600), 
                            text_input="GAME OVER", font=get_font2(40), base_color=col_1, hovering_color=col_2)

        


        PLAY_A.changeColor(PLAY_MOUSE_POS)
        PLAY_A.update(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_A.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            

        pygame.display.update()



def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("Be a Superhero!", True, "Red")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
