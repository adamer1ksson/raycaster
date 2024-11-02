import numpy as np
import pygame as pg

class Boundary:
    def __init__(self, win, x1, y1, x2, y2):
        self.a = np.array([x1, y1])
        self.b = np.array([x2, y2])
        self.win = win

    def draw(self):
        pg.draw.line(self.win, color="#ffffff", start_pos=(self.a[0], self.a[1]), end_pos=(self.b[0], self.b[1]))


