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
        self.screen = screen_temp
        # create a plane
        self.image = pygame.image.load('./fighter/image/hero1.png')
        self.bullet_list_mid = [] # bullet showing on screen

    def display(self):
        # show player plane
        self.screen.blit(self.image, (self.x, self.y))

        ''', self.bullet_list_left, self.bullet_list_right:'''
        for bullets in self.bullet_list_mid:
            #bullets.display_bullet_mid()
            bullets.display_bullet_left()
            bullets.display_bullet_right()
            bullets.move()
            if bullets.judge():  #check if bullets out of margin
                self.bullet_list_mid.remove(bullets)
                # 这个方法容易漏删， 因为删除一个元素后面的往前补，会跳过一个，而这里display()会不不断调用，所以没有这个问题
                # 实际开发的时候把想要删除的元素先存进另一个列表里
                # a = [1,2,3,4,5,6,7]  b = [3,4]
                # for i in b:
                #   a.remove(i)

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

    #def display_bullet_mid(self):
    #    self.screen.blit(self.image, (self.x, self.y))

    def display_bullet_left(self):
        self.screen.blit(self.image, (self.left_x, self.left_y))

    def display_bullet_right(self):
        self.screen.blit(self.image, (self.right_x, self.right_y))

    def move(self):
        self.y -= 8
        self.right_y -= 8
        self.left_y -= 8
        #self.right_x += 1
        #self.left_x -= 1

    def judge(self):
        if self.left_y < 10:
            return True
        else:
            return False


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

    def display_enemy(self):
        self.screen.blit(self.image, (self.ex, self.ey))

        for bullets in self.enemy_bullet_list:
            bullets.display_bullet()
            bullets.move()
            if bullets.judge():  #check if bullets out of margin
                self.enemy_bullet_list.remove(bullets)

    def enemy_move(self):
        """image width is 480"""
        self.ey += 0.5

        if self.ex > self.ran_right:
            self.direction = 'left'
        elif self.ex <= self.ran_left:
            self.direction = 'right'

        if self.direction == 'right':
            self.ex += 0.5
        elif self.direction == 'left':
            self.ex -= 0.5

    def fire(self):
        #由于程序在一个while循环内，不能用sleep,所以写一个random，当随机到特定数字时再调用
        #if random.randint(1, 00) == 25:
        random_num = random.randint(1, 200)
        if random_num == 120 or random_num == 90:
            self.enemy_bullet_list.append(EnemyBullet(self.screen, self.ex, self.ey))


class EnemyBullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 22
        self.y = y + 40
        self.screen = screen_temp
        # create a plane
        self.image = pygame.image.load('./fighter/image/bullet1.png')

    def display_bullet(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 830:
            return True
        else:
            return False


def key_control(hero_temp):
    key_state = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('Game Exit')
            exit()

        if key_state[K_RIGHT]:
            print('move to right')
            hero_temp.x += 10
        if key_state[K_LEFT]:
            print('move to left')
            hero_temp.x -= 10
        if key_state[K_UP]:
            print('move to top')
            hero_temp.y -= 10
        if key_state[K_DOWN]:
            print('move to right')
            hero_temp.y += 10
        if key_state[K_SPACE]:
            print('space/shoot')
            hero_temp.fire()

        """
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
            """


def main():
    # create window
    screen = pygame.display.set_mode((480, 852), 0, 32)
    background = pygame.image.load('./fighter/image/background.png')
    # create a plane object
    hero = HeroPlane(screen)
    enemy_0 = Enemy(screen)

    while True:
        # show background image
        screen.blit(background, (0, 0))
        hero.display()
        enemy_0.display_enemy()
        enemy_0.enemy_move()
        enemy_0.fire()
        # update content to be show in screen/fresh screen
        pygame.display.update()
        key_control(hero)


if __name__ == '__main__':
    main()
