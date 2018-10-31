def setup():
    global img
    size(640, 480)
    img = loadImage("spider.png")
    
def draw():
    global img
    (0, 0, 100,100)
    image(img, 100, 0)
    
