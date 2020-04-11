def setup ():
    size(400,600)
    point(50,50)
    rectMode(CORNER)
def draw ():
    print(mouseX,mouseY,mousePressed)
    clear()
    if mousePressed: 
        rect(mouseX,300,width/2,100)# tam gdzie można warto wykorzystać zmienne zależne, jak height i width
    # miało się też coś zadziać, gdy nie klikamy
# 1,5pkt
