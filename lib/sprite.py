import pygame
from lib.color import *

class Sprite:
    def __init__(self, display, pos, push, friction, max_velocity):
        self.display = display
        self.x = pos[0]
        self.y = pos[1]
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.push = push
        self.friction = friction
        self.max_v = max_velocity
        self.left = False
        self.down = False
        self.up = False
        self.right = False
        self.downpace = False

        self.radious = 40

    def draw(self):
        pygame.draw.circle(self.display, white, [int(self.x), int(self.y)], self.radious)

    def change_values(self):
        self.vx += self.ax
        new_x = self.x + self.vx

        self.vy += self.ay
        new_y = self.y + self.vy

        if self.vx > self.max_v:
            self.vx = self.max_v
        if self.vy > self.max_v:
            self.vy = self.max_v
        if self.vx < -self.max_v:
            self.vx = -self.max_v
        if self.vy < -self.max_v:
            self.vy = -self.max_v

        
        if self.vx < self.friction and self.vx > -self.friction and \
           (not self.left) and (not self.right):
            self.vx = 0
            
        if self.vx < 0:
            self.vx += self.friction
        elif self.vx > 0:
            self.vx -= self.friction

        if self.vy < self.friction and self.vy > -self.friction and \
           (not self.up) and (not self.down):
            self.vy = 0
        if self.vy < 0:
            self.vy += self.friction
        elif self.vy > 0:
            self.vy -= self.friction

        return new_x, new_y

    def update(self):       
        # these reset acceleration to 0 when a button is not pressed
        if not (self.left and self.right):
            self.ax = 0

        if not (self.up and self.down):
            self.ay = 0

        if self.right:
            self.ax = -self.push
        if self.left:
            self.ax = self.push
        if self.down:
            self.ay = -self.push
        if self.up:
            self.ay = self.push

        self.x, self.y = self.change_values()

        self.draw()





