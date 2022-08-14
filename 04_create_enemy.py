WIDTH = 600
HEIGHT = 400

ship = Actor("ship-0", center=(300, 200))
#NEW
enemy = Actor("creature", center=(300, 100))

def draw():
    screen.fill((255, 128, 0))
    ship.draw()
    enemy.draw()

def update():
    if keyboard.up:
        ship.y -= 2
    elif keyboard.down:
        ship.y += 2
    elif keyboard.left:
        ship.x -= 2
    elif keyboard.right:
        ship.x += 2
