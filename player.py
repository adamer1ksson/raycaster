import numpy as np
import pygame as pg
import math as math
from boundary import Boundary
DEG = 1/365

class Player:
    def __init__(self, win, x, y):
        self.pos = np.array([x, y])
        self.angle = np.array([1,0]) 
        self.size = 10
        self.win = win
        self.speed =3 
    def draw(self):
        pg.draw.circle(self.win, color="#ffffff", center=(self.pos[0], self.pos[1]), radius=self.size)
        new_v = self.pos + 20 * self.angle 
        pg.draw.line(self.win, color="#ffffff", start_pos=(self.pos[0], self.pos[1]), end_pos=(new_v[0], new_v[1])) 
     
    def rotate(self, value):
        rotation_value = -value * 20*DEG
        rotation_matrix = np.array([[math.cos(rotation_value), -math.sin(rotation_value)], [math.sin(rotation_value), math.cos(rotation_value)]])
        self.angle = np.dot(rotation_matrix, self.angle)

    def move(self):
        new_pos = self.pos + np.dot(self.angle, self.speed)
        self.pos = new_pos


    def cast(self, bound: Boundary):
        x1 = bound.a[0]
        y1 = bound.a[1]
        x2 = bound.b[0]
        y2 = bound.b[1]
        x3 = self.pos[0]
        y3 = self.pos[1]
        m  = self.pos + 10 * self.angle 
        x4 = m[0] 
        y4 = m[1] 

        den = (x1-x2) * (y3 - y4) - (y1 - y2)*(x3 -x4)
        if den == 0:
            return False

        t = ((x1-x3) * (y3 - y4) - (y1 - y3)*(x3 -x4))/den
        u = -((x1-x2) * (y1 - y3) - (y1 - y2)*(x1 -x3))/den
 
        if 0 <=t<=1 and 0 <= u:
            new_x = x1 + t*(x2-x1)
            new_y = y1 + t*(y2-y1)
            return (new_x, new_y) 
        else:
            return False




