import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import random
import pandas as pd
from data import PICTOGRAMS
from data import FONTS
from data import bcolors
import time
from os import listdir
from os.path import isfile, join
import csv

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (102, 51, 153)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 1930
SCREEN_HEIGHT = 800


def drawGUI(screen):
    screen.fill([255, 255, 255])
    pygame.draw.line(screen, BLUE, (0, 200), (1930, 200), width=5)
    pygame.draw.line(screen, BLUE, (0, 405), (1930, 405), width=5)
    pygame.draw.rect(screen, PURPLE, pygame.Rect(0, 0, 1930, 200))
    pygame.draw.rect(screen, PURPLE, pygame.Rect(0, 405, 1930, 400))
    pygame.display.update()


def drawArabic(screen, digits, digits_num, custom_font):
    step = 0
    step_inc = 70
    start_point = (SCREEN_WIDTH/2 - step_inc * digits_num // 2 , SCREEN_HEIGHT//2-140) 

    for d in digits:
        if custom_font != None:
            font = custom_font
        else: font = random.choice(FONTS)
        text = font.render(str(d), True, BLACK)
        screen.blit(text, (start_point[0] + step, start_point[1]))
        pygame.display.update()
        step += step_inc


def drawPictogram(screen, digits, images, digits_num, custom_font, height):
    step = 0
    step_inc = 190
    if height != None:
        start_point = (SCREEN_WIDTH//2 - step_inc * (digits_num // 2) - 35, height) 
    else:
        start_point = (SCREEN_WIDTH//2 - step_inc * (digits_num // 2) - 35, SCREEN_HEIGHT//2-150) 
    distance = 43

    used_images = []
    image_selected = False
    image_path = ""

    for d in digits:
        if custom_font != None:
            image_path = "/home/maxim/HMI-design/Homework 1/images/square.png"
        else:
            while not image_selected:
                image_path = random.choice(images)
                if image_path not in used_images:
                    image_selected = True
                    used_images.append(image_path)

        image = pygame.image.load(image_path)
        if d != 0:
            template = PICTOGRAMS[str(d)]
            for i in range(len(template)):
                for j in range(len(template[i])):
                    if template[i][j] == 1:
                        screen.blit(image, (start_point[0] + step + distance * j, start_point[1] + distance * i))
                        pygame.display.update()
        else:
            pygame.draw.circle(screen, BLACK, [start_point[0] + step + distance + 40, start_point[1]+50], 50)
            pygame.display.update()
        step += step_inc
        image_selected = False


def main():
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    drawGUI(screen)

    types = ["full-arabic", "full-pictogram", "random-mixed"]
    number = 0
    digits = []
    curr_type = ""
    wait_time = 0
    type_selected = False

    source_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    images = [f for f in listdir("/home/maxim/HMI-design/Homework 1/images") if isfile(join("/home/maxim/HMI-design/Homework 1/images", f))]

    for i in range(len(images)):
        images[i] = "/home/maxim/HMI-design/Homework 1/images/" + images[i] 

    name = str(input("\nEnter your name - "))
    number = 0

    while True:
        
        if number == 0:
            try:
                number = int(input("\nEnter number of digits - "))
            except Exception:
                print("Wrong value! Try again!")
                continue

        if len(digits) == 0:
            digits = []
            i = 0

            while i < number:
                digit = random.randint(0, 9)
                if digit not in digits:
                    digits.append(digit)
                    i += 1

        if len(digits) != 0 and not type_selected:
            print(f"\n1) {types[0]}")
            print(f"2) {types[1]}")
            print(f"3) {types[2]}")

            try:
                num = int(input("Enter type of digits row - "))
                curr_type = types[num-1]
            except Exception:
                print("Wrong number! Try again!")
                continue

            try:
                wait_time = float(input("\nEnter fixed time (secs) for showing - "))
                print("\nGo to screen")
            except Exception:
                print("Wrong value! Try again!")
                continue

            type_selected = True

        # digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and type_selected:

                    # timer
                    start = time.time()
                    timer_i = 3
                    timer_colors = [RED, ORANGE, GREEN]
                    colors_i = 0
                    while time.time() - start <= 3.0:
                        font = pygame.font.SysFont("arial", 80)
                        text = font.render(str(timer_i), True, timer_colors[colors_i])
                        colors_i += 1
                        timer_i -= 1
                        screen.blit(text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 140))
                        pygame.display.update()
                        time.sleep(1.0)
                        drawGUI(screen)

                    drawGUI(screen)

                    if curr_type == "full-arabic":
                        drawArabic(screen, digits, len(digits), None)

                    if curr_type == "full-pictogram":
                        drawPictogram(screen, digits, images, len(digits), None, None)

                    if curr_type == "random-mixed":
                        used_images = []
                        step_inc = 180 
                        step = 0
                        start_point = (SCREEN_WIDTH//2 - step_inc * (len(digits) // 2), SCREEN_HEIGHT//2-150)

                        for d in digits:
                            choice = random.choice(['arabic', 'pictogram'])

                            if choice == 'arabic':
                                font = random.choice(FONTS)
                                text = font.render(str(d), True, BLACK)
                                screen.blit(text, (start_point[0] + step, start_point[1]))
                                pygame.display.update()
                                step += step_inc

                            elif choice == 'pictogram':
                                distance = 43

                                image_selected = False

                                while not image_selected:
                                    image_path = random.choice(images)
                                    if image_path not in used_images:
                                        image_selected = True
                                        used_images.append(image_path)

                                image = pygame.image.load(image_path)

                                if d != 0:
                                    template = PICTOGRAMS[str(d)]
                                    for i in range(len(template)):
                                        for j in range(len(template[i])):
                                            if template[i][j] == 1:
                                                screen.blit(image, (start_point[0] + step + distance * j, start_point[1] + distance * i))
                                                pygame.display.update()
                                else:
                                    pygame.draw.circle(screen, BLACK, [start_point[0] + step + distance + 40, start_point[1]+50], 50)
                                    pygame.display.update()

                                step += step_inc
                                image_selected = False

                    start = time.time()
                    while time.time() - start <= wait_time:
                        pygame.display.update()

                    # saving generated number in image
                    image_name = ""
                    for d in digits:
                        image_name += ''.join(str(d) + " ")

                    hash = str(random.getrandbits(128))[0:8]
                    image_name += "(" + hash + ")"
                    pygame.image.save(screen, f"/home/maxim/HMI-design/Homework 1/results/{image_name}.jpg")

                    drawGUI(screen)

                    if curr_type == "full-arabic":
                        drawArabic(screen, source_digits, len(source_digits), FONTS[1])

                    if curr_type == "full-pictogram":
                        drawPictogram(screen, source_digits, images, len(source_digits), 1, None)

                    if curr_type == "random-mixed":
                        drawArabic(screen, source_digits, len(source_digits), FONTS[1])
                        drawPictogram(screen, source_digits, images, len(source_digits), 1, 500)
                
                    user_input = input("\nEnter the digits that were shown in the set (not necessarily in the correct order) - ")

                    # check for mistakes of user input
                    user_input = [int(x) for x in str(user_input)]

                    output = ""
                    mistakes = 0
                    found_digits = {}
                    for d in digits:
                        found_digits[d] = 0

                    for ud in user_input:
                        if ud in digits:
                            output += bcolors.OKGREEN + str(ud)
                            found_digits[ud] = 1
                        else:
                            output += bcolors.FAIL + str(ud)
                            mistakes += 1

                    output += " "

                    for fd in found_digits.keys():
                        if found_digits[fd] == 0:
                            output += bcolors.WARNING + str(fd)
                            mistakes += 1

                    print(output + bcolors.ENDC)
                    drawGUI(screen)

                    # saving results to csv file
                    with open('/home/maxim/HMI-design/Homework 1/results.csv', mode='a') as file:
                        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        writer.writerow([str(name), str(user_input), str(image_name), str(wait_time), str(mistakes)])

                    type_selected = False
                    digits = []
                    number = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            pygame.display.update()

if __name__ == "__main__":
    main()  