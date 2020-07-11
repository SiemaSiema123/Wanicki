def setup():
    global rysunek
    rysunek = loadImage("cosznaukowca.jpg")
    size(303, 220)
    strokeWeight(3)
    background(255)
    noFill()
 
def draw():
    try:
        image(rysunek, 1, 2, 300, 200)
    except:
        stroke("#FF0000")
        fill(0)
        text("obraz nie dziala", 5, 215)    
    else:
        stroke("#0000FF")
    finally:
        rect(1, 2, 300, 200)
