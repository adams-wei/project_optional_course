# 1. go to "cmd" and input "python"
# 2. it will ask you to install python, just install
# 3. after installation, input "pip install pygame"
# 4. there you go
import pygame as pg

##### initialize
H=600
W=800
screen=pg.display.set_mode((W,H))
pg.display.set_caption("多元選修")
image_icon=pg.image.load('image/game_icon.png') #load icon
pg.display.set_icon(image_icon)


##### initialize end
##### def

class Ball:
    def __init__(self,x,y,Radius,mass):
        self.x=x
        self.y=y
        self.Radius=Radius
        self.mass=mass
        
    def draw(self,screen):
        pg.draw.circle(screen,(112,128,144),(int(self.x),int(self.y)),radius=float(self.Radius))
        #pygame.draw.circle(where, color, cneter location, radius)
        
class Planet:
    def __init__(self,x,y,Radius,mass):
        self.x=x
        self.y=y
        self.Radius=Radius
        self.mass=mass
        
    def draw(self,screen):
        pg.draw.circle(screen,(112,128,144),(int(self.x),int(self.y)),radius=float(self.Radius))

##### def end

running=True
ball=Ball(x=W/2,y=H/2,Radius=50,mass=100)
planet=Planet(x=50,y=50,Radius=20,mass=100)

while running:
    for event in pg.event.get():
        if event.type== pg.QUIT:
            running=False

    screen.fill((255,255,255))
    ball.draw(screen)
    planet.draw(screen)
    pg.display.flip()
pg.quit()