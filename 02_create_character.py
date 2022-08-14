WIDTH = 600
HEIGHT = 400

#NEW
ship = Actor("ship-0", center=(300, 200))

def draw():
    screen.fill((255, 128, 0))
    #NEW
    ship.draw()
