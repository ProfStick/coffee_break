""" Coffee Rush.

A simple pygame game
"""

__copyright__ = "(c) Geoff Goldrick 2014"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Geoff Goldrick"
__version__ = "1.0"
__revision__ = "20150907"

""" revision notes:

"""

# dependencies
from mods import *
import pygame as P

#initialise pygame
P.init()


def main():
    # parameters
    screen_size = width, height = 800, 600

    # Define the colors we will use in RGB format
    black = [ 0, 0, 0]
    white = [255 ,255 ,255]
    blue = [ 0, 0 ,255]
    light_blue = [125,125,255]
    green = [ 0 ,255 , 0]
    red = [255 , 0, 0]

    cup_array = [] #store the cups that are created

    clock = P.time.Clock() # Create a timer used to control how often the screen updates
    loop_rate = 20 #number of times per second does loop
    move_rate = 2
    time_step = 1000 #time in millisecs between adding cups
    last_added = 0 #last time a cup was added to the cup_array
    score = 0

    cup_break = P.mixer.Sound('sound/cup_break.wav')
    background_muzak = P.mixer.Sound('sound/jungle_run_01.ogg')
    game_over_sound = P.mixer.Sound('sound/cup_shatter.wav')


    play = True
    over = False

    P.display.set_caption('Coffee Rush')
    icon = P.image.load('images/coffee_cup_32.png')
    P.display.set_icon(icon)
    screen = P.display.set_mode(screen_size)
    font = P.font.Font(None,30)

    background_muzak.play()

    while play:
        clock.tick(loop_rate) #cycle through loop 'rate' times per second
        now = P.time.get_ticks() #get the time since program started in millisecs

        event = P.event.poll() #did the player do something?

        if event.type == P.QUIT: #player clicked close so quit
            play = False
            over = True

        if event.type == P.MOUSEBUTTONDOWN:
            player_position = P.mouse.get_pos()
            for cup in cup_array:
                if cup.rectangle.collidepoint(player_position):
                    cup_array.remove(cup)
                    cup_break.play()
                    score += cup.move_rate #the faster it goes the more it adds to score

            if (score > 0) and (score % 10) == 0:
                move_rate += 1


        if (now - last_added > time_step) and (len(cup_array) < 10): #time to add a cup
            cup_array.append(Cup(screen_size,now, move_rate))
            last_added = P.time.get_ticks()

        screen.fill(light_blue) #clear the screen

        for cup in cup_array:
            if cup.temp == 'cold':
                play = False

            cup.update(now,screen_size)
            screen.blit(cup.image,cup.rectangle)

        score_text = font.render('Score: {}'.format(score),1,red,white)
        screen.blit(score_text,[10, height-30])

        P.display.flip()
        time_step = max(time_step - 1,200) #dont let it go too fast


    font_over = P.font.Font(None,100)
    over_x,over_y = font_over.size("GAME OVER")
    game_over_text = font_over.render("GAME OVER",1,red, light_blue)
    background_muzak.stop()
    game_over_sound.play()

    screen.blit(game_over_text,[(width - over_x)/2, (height - over_y)/2])
    P.display.flip()


    while not over:
        event = P.event.poll() #did the player do something?
        if event.type == P.QUIT: #player clicked close so quit
            over = True

    P.quit()


if __name__ == '__main__':
    main()