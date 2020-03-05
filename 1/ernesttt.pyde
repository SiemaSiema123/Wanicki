def setup ():
    size(400,600)
    point(50,50)
    rectMode(CORNER)
def draw ():
    print(mouseX,mouseY,mousePressed)
    clear()
    
    if mousePressed: 
        rect(mouseX,300,200,100)
        
        
