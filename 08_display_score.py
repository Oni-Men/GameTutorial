import math

WIDTH = 600
HEIGHT = 400

ship = Actor("ship-0", center=(300, 200))
enemy = Actor("creature", center=(300, 100))

score = 0 #NEW

lasers = []
count = 0

def draw():

    screen.fill((255, 128, 0))
    ship.draw()
    enemy.draw()
    for laser in lasers:
        laser.draw()

    text = "Score " + str(score)
    screen.draw.text(text, (15, 10), color=(255, 255, 255), fontsize=30)


def update(dt):
    global count, lasers, score #NEW
    count += 1
    if keyboard.up:
        ship.y -= 2
    elif keyboard.down:
        ship.y += 2
    elif keyboard.left:
        ship.x -= 2
    elif keyboard.right:
        ship.x += 2

    for laser in lasers[:]:
        laser.y -= 10
        if laser.distance_to(ship) > HEIGHT:
            lasers.remove(laser)
        elif laser.colliderect(enemy):
            lasers.remove(laser)
            score += 1 #NEW

    enemy.x = 300 + math.sin(math.radians(count)) * 150


def on_key_down(key):
    if key == keys.SPACE:
        laser = Actor("laser", center=(ship.x, ship.y))
        lasers.append(laser)
