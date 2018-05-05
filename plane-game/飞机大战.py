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
        self.left_x = 210
        self.left_y = 710
        self.right_x = 240
        self.right_y = 710

        self.screen = screen_temp
        # create a plane
        self.image = pygame.image.load('./fighter/image/hero1.png')
        self.bullet_list_mid = [] # bullet showing on screen
        #self.bullet_list_left = []
        #self.bullet_list_right = []

    def display(self):
        # show player plane
        self.screen.blit(self.image, (self.x, self.y))

        ''', self.bullet_list_left, self.bullet_list_right:'''
        for bullets in self.bullet_list_mid:
            bullet.display_bullet_mid()
            '''
            for bullets in self.bullet_list_left():
                bullet.display_bullet_left()
                for bullets in self.bullet_list_right():
                    bullet.display_bullet_right()
            '''
            bullet.move()

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10

    def fire(self):
        self.bullet_list_mid.append(bullet(self.screen, self.x, self.y, self.left_x, self.left_y, self.right_x, self.right_y))
        #self.bullet_list_mid.append(bullet(self.screen, self.x, self.y))
        #self.bullet_list_left.append(bullet(self.screen, self.left_x, self.left_y))
        #self.bullet_list_left.append(bullet(self.screen, self.right_x, self.right_y))


'''left_x, left_y, right_x, right_y'''


class bullet(object):
    def __init__(self, screen_temp, x, y, left_x, left_y, right_x, right_y):
        self.x = x + 40
        self.y = y - 25
        self.left_x = x + 30
        self.left_y = y - 10
        self.right_x = x + 50
        self.right_y = y - 10
        self.screen = screen_temp
        # create a plane
        self.image = pygame.image.load('./fighter/image/bullet.png')

    def display_bullet_mid(self):
        self.screen.blit(self.image, (self.x, self.y, self.left_x, self.left_y, self.right_x, self.right_y))

    #def display_bullet_left(self):
    #    self.screnn.blit(self.image, (self.left_x, self.left_y))

    #def display_bullet_right(self):
    #   self.screen.blit(self.image, (self.right_x, self.right_y))

    def move(self):
        self.y -= 15
        self.right_y -= 15
        self.left_y -= 15


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
                print('space/shoot')
                hero_temp.fire()


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
