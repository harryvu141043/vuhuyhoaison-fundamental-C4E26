def draw_star(x,y,len):
    import turtle
    t=turtle.Turtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(5):
        t.right(144)
        t.forward(len)
    
draw_star(90,189,1000)
