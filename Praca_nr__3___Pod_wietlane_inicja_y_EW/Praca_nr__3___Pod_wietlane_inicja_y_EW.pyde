wcisnieteW = False 
wcisnietaLewa = False 
wcisnietaPrawa = False 

def setup():
 
    size(1000, 1000)
 
def draw():
    if kursorNaE() and wcisnietaPrawa :
        KolorujLitereW(170, 143, 22) 
        KolorujLitereE(255,200,200) 
    elif kursorNaE(): 
        KolorujLitereW(255,200,200) 
        KolorujLitereE(170, 143, 22) 
    else: 
        KolorujLitereW(255,200,200)
        KolorujLitereE(255,200,200)
   
   
    if wcisnieteW and wcisnietaLewa: 
        KolorujLitereW(255,200,200) 
        KolorujLitereE(170, 143, 22)
    elif wcisnieteW: 
        KolorujLitereW(170, 143, 22) 
        KolorujLitereE(255,200,200) 
   
   
def KolorujLitereE(r,g,b):
     
    fill(r,g,b)
    pushMatrix() 

    rect(200, 150, 20, 100)
    rect(220, 150, 50, 20)
    rect(220, 190, 50, 20)
    rect(220, 230, 50, 20)
   
    popMatrix() 
def KolorujLitereW(r,g,b):
    fill(r,g,b)
   
    pushMatrix()
   
    quad(300, 150, 320, 150, 340, 250, 320, 250,)
    quad(360, 180, 380, 180, 340, 250, 320, 250,)
    quad(420, 150, 440, 150, 420, 250, 400, 250,)
   
    quad(360, 180, 380, 180, 420, 250, 400, 250,)
    popMatrix()
 
def kursorNaE(): 
    if mouseX>=200 and mouseX <= 200+20 and mouseY>=150 and mouseY <= 150+100 \
        or mouseX>=220 and mouseX <= 220+50 and mouseY>=150 and mouseY <= 150+20 \
        or mouseX>=220 and mouseX <= 220+50 and mouseY>=190 and mouseY <= 190+20 \
        or mouseX>=220 and mouseX <= 220+50 and mouseY>=230 and mouseY <= 230+20:
            return True
    return False
 
def keyPressed(): 
    global wcisnieteW, wcisnietaLewa, wcisnietaPrawa
    if key == CODED and keyCode == RIGHT: 
        wcisnietaPrawa = True 
    if key == CODED and keyCode == LEFT: 
        wcisnietaLewa = True 
    if key == 'w' or key == 'W': 
        wcisnieteW = True 
       
def keyReleased(): 
    global wcisnieteW, wcisnietaLewa, wcisnietaPrawa
    if key == CODED and keyCode == RIGHT: 
        wcisnietaPrawa = False 
    if key == CODED and keyCode == LEFT: 
        wcisnietaLewa = False 
    if key == 'w' or key == 'W': 
        wcisnieteW = False
        
# zabrakło podkreślenia, ale po za tym bardzo ładnie i plus do aktywności za organizację kodu
# 1,75pkt
