import sys
import pygame as pg
import math


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")

    kou = pg.Surface((0, 0))
    kou = pg.image.load("ex01/fig/3.png")
    kou = pg.transform.flip(kou, True, False)
    kou = pg.transform.rotozoom(kou, 10, 1)
    lis = [kou]

    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr,0])
        screen.blit(pg.transform.flip(bg_img, True, False), [1600-tmr, 0])
        screen.blit(bg_img, [3200-tmr, 0])
        if tmr == 3200:
            tmr = 0
        else:
            pass
        
        screen.blit(kou, [300, 200+10*math.sin(math.radians(tmr))])
        
        pg.display.update()
        tmr += 1        
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()