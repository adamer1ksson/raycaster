import pygame as pg 
import numpy as np
from boundary import Boundary
from player import Player

DEG =1/365


def main():
     
    pg.init()
    infoObject=pg.display.Info()
    width, height = infoObject.current_w, infoObject.current_h 
    width -= 100
    height -= 100
    win = pg.display.set_mode((width, height)) 
    pg.display.set_caption("My Board") 
    clock = pg.time.Clock()

    walls = []
    walls.append(Boundary(win, 100, 100, width-100, 100))
    walls.append(Boundary(win, width-100, 100, width-100, height-100))
    walls.append(Boundary(win, 100, 100, 100, height-100))
    walls.append(Boundary(win, 100, height-100, width-100, height-100))
    p = Player(win, width//2, height//2)
    
    running = True
    rotating_r = False
    rotating_l = False
    moving = False
    
    while running: 
        win.fill((0, 0, 0))
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                running = False 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    rotating_r = True
                if event.key == pg.K_LEFT:
                    rotating_l = True
                if event.key == pg.K_UP:
                    moving = True 
            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    rotating_r = False 
                if event.key == pg.K_LEFT:
                    rotating_l = False  
                if event.key == pg.K_UP:
                    moving = False 
        if rotating_r:
            p.rotate(-1)
        if rotating_l:
            p.rotate(1)
        if moving:
            p.move()

        for wall in walls:
            wall.draw()
            handle = p.raycast(wall)
            for coord in handle:
                pg.draw.circle(win,color="#ffffff", center=coord, radius=10)
        
        p.draw()
        pg.display.update()
        clock.tick(60)


if __name__ =="__main__":
    main()
