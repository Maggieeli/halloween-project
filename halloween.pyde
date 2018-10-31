x = 0
y = 640

def setup():
    size(640, 480)
    
def draw():
    global x, y
    
    while x == width:
        x = 0
        
    while y == 0:
        y = 640
    
    x += 2
    y -= 2.5
    
    background(255)
    
    # ghost 1
    
    fill(107, 107, 107)
    noStroke()
    rect(x, height / 2 - 100, 95, 85, 90, 90, 0, 0)
    ellipse(x + 7, height / 2 - 12, 34, 38)
    ellipse(x + 24, height / 2 - 9, 34, 38)
    ellipse(x + 43, height / 2 - 9, 34, 38)
    ellipse(x + 60, height / 2 - 9, 29, 34)
    ellipse(x + 78, height / 2 - 12, 34, 38)
    
    ellipse(x - 10, height / 2 - 60, 30, 35)
    ellipse(x - 18, height / 2 - 45, 30, 35)
    
    
    fill(255)
    stroke(22, 22, 22)
    ellipse(x + 28, height / 2  - 66, 30, 35)
    ellipse(x + 60, height / 2 - 66, 30, 35)
    
    fill(0)
    noStroke()
    ellipse(x + 35, height / 2 - 66, 17, 22)
    ellipse(x + 67, height / 2 - 66, 17, 22)
    
    ellipse(x + 48, height / 2 - 40, 22, 17)
    
    # ghost 2
    fill(204, 201, 201)
    ellipse(y, height / 2 + 100, 110,130)
    
    ellipse(y + 55, height / 2 + 150, 40, 55)
    ellipse(y + 30, height / 2 + 160, 40, 55)
    ellipse(y, height / 2 + 160, 40, 55)
    ellipse(y - 30, height / 2 + 160, 40, 55)
    
    fill(255)
    stroke(22, 22, 22)
    ellipse(y - 20, height / 2 + 90, 28, 33)
    ellipse(y + 15, height / 2 + 90, 28, 33)
    
    fill(0)
    noStroke()
    ellipse(y - 5, height / 2 + 115, 23, 20)
    ellipse(y - 27, height / 2 + 90, 17, 22)
    ellipse(y + 8, height / 2 + 90, 17, 22)
    
    

    
