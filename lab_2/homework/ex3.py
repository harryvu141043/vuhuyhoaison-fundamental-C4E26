def draw_square(x,y):
    import turtle
    
    t=turtle.Turtle()
    t.speed(10)
    t.color(str(y))
    for j in range(4):
        t.forward(x)
        t.left(90)
  

