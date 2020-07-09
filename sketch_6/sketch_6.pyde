class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
       
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski):
        Kwadrat.sketch(self, x, y)
        space = self.bok/paski
        _xLinii_ = 0
        for pasek in range(0, paski):
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
           
class OkraglastyKwadrat(Kwadrat): # kwadratura koła? ;)
    def sketchOkraglasty(self, x, y):
        Kwadrat.sketch(self, x, y)
       
        ellipseMode(CORNER)
        circle(x, y, self.bok)
   
           
def setup():
    size(500, 500)
    malyKwadrat = Kwadrat(50.0)
    malyKwadrat.sketch(200, 300)
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    malyKwadrat.sketch(100, 200)
    siema = OkraglastyKwadrat(100.0)
    siema.sketchOkraglasty(300, 300)
    
#2pkt
