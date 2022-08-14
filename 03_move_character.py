WIDTH = 600
HEIGHT = 400

ship = Actor("ship-0", center=(300, 200))

def draw():
    screen.fill((255, 128, 0))
    ship.draw()

#NEW
def update():
    ship.x += 1
    ship.y += 1
    if keyboard.up:
        ship.y -= 2
    if keyboard.down:
        ship.y += 2
    if keyboard.left:
        ship.x -= 2
    if keyboard.right:
        ship.x += 2
