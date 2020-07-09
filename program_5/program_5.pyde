class Koleczko():
    direction_x = [1, 1, -1, -1]
    direction_y = [1, -1, -1, 1]
    colores = ["#96ceb4", "#ffeead", "#ffcc5c", "#ff6f69"]
    speed = 1
    def __init__(self, x, y, extent):
        self.x = x
        self.y = y
        self.extent = extent
        self.dir = 0
    
    def moverino(self):
        for i in range(self.extent/12):
            self.x += self.speed * self.direction_x[self.dir]
            self.y += self.speed * self.direction_y[self.dir]
            fill(self.colores[self.dir])
            stroke(self.colores[(self.dir + 1) % 4])
            circle(self.x, self.y, self.extent)
        self.dir = (self.dir + 1) % 4

def setup():
    global lista
    size(500, 500)
    lista = []
    
def draw():
    background(255)
    for i in lista: i.moverino()

def mousePressed():
    lista.append(Koleczko(mouseX, mouseY, 50))

#2pkt
