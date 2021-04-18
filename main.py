from pygame import *

scr = display.set_mode((1200, 675))

fps = 60

clock = time.Clock()
game = True

ball = image.load("ppb.png")
ball = transform.scale(ball,(50,50))
p1 = image.load("sh.png")
p2 = image.load("crow.png")

bg = image.load("fon.jpg")
while game:
    scr.blit(bg,(0,0))
    scr.blit(ball,(0,0))
    scr.blit(p1,(100,100))
    scr.blit(p2,(200,200))
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(fps)
