def setup():
    size(600,600)
    global x, y, set_color, colors_array, mv_x, mv_y
    colors_array = ["#FF0000", "#00FF00", "#0000FF"]
    x = 0
    y = height/2
    set_color = 0
    mv_x = 1
    mv_y = 1
    
def draw():
    global x, y, set_color, colors_array, mv_x, mv_y
    shape_width = 50; shape_height = 50
    rect(x, y, shape_width, shape_height)

    fill(100, 150, 200)
    textSize(42)
    text("click to exit", width/2, height/2)

    fill(colors_array[set_color])
    x += mv_x
    y += mv_y

    if x == 0 or x == width - shape_width:
        mv_x = mv_x * -1
        set_color = (set_color + 1) % 3
    if y == 0 or y == height - shape_height:
        mv_y = mv_y * -1
        set_color = (set_color + 1) % 3
        
def mousePressed():
    exit()
