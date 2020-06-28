add_library('pdf')
def setup():
    global zdjecie, was, czapka
    size(500, 500) # to nie sąproporcje zdjęcia dokumentowego, po za tym rozciąga to zdjęcie
    zdjecie = loadImage("alibaba.jpg")
    was = loadImage("wons.png")
    czapka = loadImage("fedorka.png")

def draw():
    beginRecord(PDF, "pedeefik.pdf")
    image(zdjecie, 0,0, height, width)

    if keyCode == LEFT:
        image(was, 180, 235, 175, 175)
        
    elif keyCode == RIGHT:
        image(czapka, 25, -50, 450, 250)

def mousePressed():
    endRecord()
    exit()
    
# 1,5pkt
