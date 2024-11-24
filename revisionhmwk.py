import pgzrun
import random


WIDTH= 500
HEIGHT= 500

satellite= Actor("satellite")
print("setup")
def draw():
    print("draw")
    screen.blit("bground",(0,0))
    x = random.randint(0, WIDTH - 50) 
    y = random.randint(0, HEIGHT - 50)
    satellite.pos = (x, y)
    for i in range(10):
            satellite.draw()
print("outside")
pgzrun.go()        