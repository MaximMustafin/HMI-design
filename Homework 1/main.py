import pygame
import random
import pandas as pd
from data import PICTOGRAMS
from data import FONTS
import time
from os import listdir
from os.path import isfile, join

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (102, 51, 153)
SCREEN_WIDTH = 1930
SCREEN_HEIGHT = 800


def drawGUI(screen):
    screen.fill([255, 255, 255])
    pygame.draw.line(screen, BLUE, (0, 200), (1930, 200), width=5)
    pygame.draw.line(screen, BLUE, (0, 405), (1930, 405), width=5)
    pygame.draw.rect(screen, PURPLE, pygame.Rect(0, 0, 1930, 200))
    pygame.draw.rect(screen, PURPLE, pygame.Rect(0, 405, 1930, 400))
    pygame.display.update()


def drawArabic(screen, digits):
    step = 0
    step_inc = 70
    start_point = (SCREEN_WIDTH/2 - step_inc * len(digits) // 2 , SCREEN_HEIGHT//2-140) 

    for d in digits:
        font = random.choice(FONTS)
        text = font.render(str(d), True, BLACK)
        screen.blit(text, (start_point[0] + step, start_point[1]))
        pygame.display.update()
        step += step_inc


def drawPictogram(screen, digits, images):
    step = 0
    step_inc = 210
    start_point = (SCREEN_WIDTH//2 - step_inc * (len(digits) // 2) - 35, SCREEN_HEIGHT//2-150) 
    distance = 43

    print(digits)
    for d in digits:
        image_path = random.choice(images)
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


def main():
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    drawGUI(screen)

    formats = ["arabic", "pictogram"]
    types = ["full-arabic", "full-pictogram", "random-mixed"]
    number = 0
    digits = []
    curr_type = ""
    type_selected = False

    images = [f for f in listdir("/home/maxim/HMI-design/Homework 1/images") if isfile(join("/home/maxim/HMI-design/Homework 1/images", f))]

    for i in range(len(images)):
        images[i] = "/home/maxim/HMI-design/Homework 1/images/" + images[i] 

    # name = str(input("Enter your name - "))

    while True:

        if len(digits) == 0:
            number = random.randint(1, 9)
            digits = []
            i = 0

            while i < number:
                digit = random.randint(0, 9)
                if digit not in digits:
                    digits.append(digit)
                    i += 1

        if len(digits) != 0 and not type_selected:
            print(f"1) {types[0]}")
            print(f"2) {types[1]}")
            print(f"3) {types[2]}")
            num = int(input("Enter type of digits row: "))

            try:
                curr_type = types[num-1]
            except Exception:
                print("Wrong number! Try again!")
                continue

            type_selected = True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and type_selected:
                    drawGUI(screen)

                    wait_time = 0

                    if curr_type == "full-arabic":
                        drawArabic(screen, digits)
                        wait_time = len(digits) / 2

                    if curr_type == "full-pictogram":
                        drawPictogram(screen, digits, images)
                        wait_time = len(digits)

                    if curr_type == "random-mixed":
                        choice = random.choice([0, 1])
                        wait_time = len(digits)

                        if choice == 0:
                            drawArabic(screen, digits)
                        else:
                            drawPictogram(screen, digits, images)

                    start = time.time()

                    while time.time() - start <= wait_time:
                        pygame.display.update()

                    type_selected = False
                    digits = []
                    drawGUI(screen)

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            pygame.display.update()



if __name__ == "__main__":
    main()  