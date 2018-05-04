import pygame
from pygame.locals import *

"""
面向对象编程,飞机大战
Object:

"""


class HeroPlane(object):
    def __init__(self, screen_temp):
        # set initial object position
        self.x = 200
        self.y = 700
        self.screen = screen_temp
        # create a plane
        self.image = pygame.image.load('./fighter/image/hero1.png')

    def display(self):
        # show player plane
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= 8

    def move_right(self):
        self.x += 8

    def move_up(self):
        self.y -= 8

    def move_down(self):
        self.y += 8


def key_control(hero_temp):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('Game Exit')
            exit()

        # check if player press any key
        elif event.type == pygame.KEYDOWN:

            if event.key == K_a or event.key == K_LEFT:  # K_LEFT =  pygame.K_LEFT
                print('move left')
                hero_temp.move_left()

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print('move right')
                hero_temp.move_right()

            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                print('move top')
                hero_temp.move_up()

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                print('move down')
                hero_temp.move_down()

            elif event.key == pygame.K_SPACE:
                print('space')


def main():
    # create window
    screen = pygame.display.set_mode((480, 852), 0, 32)

    background = pygame.image.load('./fighter/image/background.png')

    # create a plane object
    hero = HeroPlane(screen)

    while True:
        # show background image
        screen.blit(background, (0, 0))

        hero.display()

        # update content to be show in screen/fresh screen
        pygame.display.update()

        key_control(hero)


if __name__ == '__main__':
    main()
