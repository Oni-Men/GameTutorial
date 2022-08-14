import math

WIDTH = 600
HEIGHT = 400

ship = Actor("ship-0", center=(300, 200))
enemy = Actor("creature", center=(300, 100))

# NEW
lasers = []

count = 0


def draw():
    screen.fill((255, 128, 0))
    ship.draw()
    enemy.draw()
    for laser in lasers:
        laser.draw()


def update(dt):
    # NEW
    global count, lasers
    count += 1
    if keyboard.up:
        ship.y -= 2
    elif keyboard.down:
        ship.y += 2
    elif keyboard.left:
        ship.x -= 2
    elif keyboard.right:
        ship.x += 2

    # NEW
    for laser in lasers[:]:
        laser.y -= 10
        if laser.distance_to(ship) > HEIGHT:
            lasers.remove(laser)

    enemy.x = 300 + math.sin(math.radians(count)) * 150


# NEW
def on_key_down(key):
    if key == keys.SPACE:
        laser = Actor("laser", center=(ship.x, ship.y))
        lasers.append(laser)
