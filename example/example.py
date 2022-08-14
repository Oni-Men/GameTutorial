import math

WIDTH = 600
HEIGHT = 400

ship = Actor("ship-0", center=(300, 200))
enemy = Actor("creature", center=(300, 100))
enemy.width

# NEW
fireballs = []
lasers = []
booms = []
count = 0

score = 0
hp = 10


def draw():
    screen.fill((255, 128, 0))
    for laser in lasers:
        laser.draw()
    for boom in booms:
        boom.draw()
    ship.draw()
    enemy.draw()

    screen.draw.text("SCORE: " + str(score), pos=(10, 10))
    screen.draw.text("HP: " + str(hp), pos=(10, 25))


def update(dt):
    # NEW
    global count, lasers, booms, hp, score
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
    for laser in lasers:
        laser.y -= 10
    lasers = list(filter(lambda e: e.distance_to(ship) < HEIGHT, lasers))

    enemy.x = 300 + math.sin(math.radians(count)) * 150

    if count % 2 == 0:
        boom = Actor("boom", center=(enemy.x, enemy.y))
        boom.angle = count * 10
        booms.append(boom)
    for boom in booms:
        boom.x += 2 * math.cos(math.radians(boom.angle))
        boom.y += 2 * math.sin(math.radians(boom.angle))
        if boom.distance_to(ship) < 10:
            hp -= 1
            booms.remove(boom)
    booms = list(filter(lambda e: e.colliderect(screen.surface.get_rect()), booms))


# NEW
def on_key_down(key):
    if key == keys.SPACE:
        laser = Actor("laser", center=(ship.x, ship.y))
        laser.width = 2
        laser.height = 10
        lasers.append(laser)
