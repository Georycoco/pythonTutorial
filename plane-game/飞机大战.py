import random
import time
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
        for bullet in self.bullet_list_mid:
            bullet.display_bullet_mid()
            bullet.display_bullet_left()
            bullet.display_bullet_right()
            bullet.move()

    def move_left(self):
        self.x -= 15

    def move_right(self):
        self.x += 15

    def move_up(self):
        self.y -= 15

    def move_down(self):
        self.y += 15

    def fire(self):
        self.bullet_list_mid.append(Bullet(self.screen, self.x, self.y))
        #self.bullet_list_left.append(Bullet(self.screen, self.left_x, self.left_y))
        #self.bullet_list_right.append(Bullet(self.screen, self.right_x, self.right_y))


'''left_x, left_y, right_x, right_y'''


class Bullet(object):
    def __init__(self, screen_temp, x, y):

        self.left_x = x
        self.left_y = y + 10
        self.right_x = x + 80
        self.right_y = y + 10
        self.x = x + 40
        self.y = y - 25
        self.screen = screen_temp
        # create a plane
        self.image = pygame.image.load('./fighter/image/bullet.png')

    def display_bullet_mid(self):
        self.screen.blit(self.image, (self.x, self.y))

    def display_bullet_left(self):
        self.screen.blit(self.image, (self.left_x, self.left_y))

    def display_bullet_right(self):
        self.screen.blit(self.image, (self.right_x, self.right_y))

    def move(self):
        self.y -= 8
        self.right_y -= 8
        self.left_y -= 8
        self.right_x += 1
        self.left_x -= 1


class Enemy (object):
    """create enemy plane"""
    def __init__(self, screen_temp):
        self.ran_left = random.randint(30, 130)
        self.ran_right = random.randint(150, 250)
        self.ex = random.randint(50, 350)
        self.ey = 0
        self.screen = screen_temp
        self.image = pygame.image.load('./fighter/image/enemy0.png')
        self.enemy_list = []
        self.enemy_bullet_list = []
        self.direction = 'right'

    def display(self):
        for enemy in self.enemy_list:
            enemy.display_enemy_1()
            enemy.display_enemy_2()

    def add_enemy(self):
        while True:
            self.enemy_list.append(Enemy(self.screen, self.ex, self.ey))
            time.sleep(2)

    def display_enemy_1(self):
        self.screen.blit(self.image, (self.ex, self.ey))

    def display_enemy_2(self):
        self.screen.blit(self.image, (self.ex, self.ey))

    def enemy_move(self):
        """image width is 480"""
        self.ey += 1

        if self.ex > self.ran_right:
            self.direction = 'left'
        elif self.ex <= self.ran_left:
            self.direction = 'right'

        if self.direction == 'right':
            self.ex += 0.5
        elif self.direction == 'left':
            self.ex -= 0.5


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

    enemy_0 = Enemy(screen)
    #enemy_0.__init__(screen)
    #enemy_number = 0

    while True:
        # show background image
        screen.blit(background, (0, 0))
        hero.display()
        enemy_0.add_enemy()
        enemy_0.display_enemy_1()
        enemy_0.enemy_move()
        # update content to be show in screen/fresh screen
        pygame.display.update()
        key_control(hero)


if __name__ == '__main__':
    main()
