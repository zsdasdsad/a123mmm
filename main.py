from pygame import *

scr = display.set_mode((1200, 675))

fps = 60

clock = time.Clock()
game = True

ball = image.load("ppb.png")
ball = transform.scale(ball,(50,50))
p1 = image.load("sh.png")
p1 = transform.scale(p1,(300,300))
p2 = image.load("crow.png")
p2 = transform.scale(p2,(100,200))

bg = image.load("fon.jpg")
while game:
    scr.blit(bg,(0,0))
    scr.blit(ball,(0,0))
    scr.blit(p1,(-90,0))
    scr.blit(p2,(1100,10))
    ball.rect.x += dx
    ball.rect.y -= dy
    if ball.rect.x > 650:
        dx = -1
    if ball.rect.y < 0:
        dy = -1
    if ball.rect.x < 0:
        dx = -1
    if ball.rect.y > 450:
        dy = -1
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(fps)
