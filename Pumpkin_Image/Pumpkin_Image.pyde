def setup():
    global pumpkin_image
    size(640, 480)
    pumpkin_image = loadImage("pumpkin.png")
    
def draw():
    global pumpkin_image
    image(pumpkin_image, 100, 335, 150, 150)
    
    
