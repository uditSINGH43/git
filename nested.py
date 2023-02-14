from turtle import *
speed('fastest')
pencolor('pink')
fillcolor('yellow')
pensize(4)
side=6
for i in range(side):
    fd(100)
    begin_fill()
    for i in range(side):
        fd(20)
        for i in range(side):
            fd(40)
            lt(360/side)
            dot(8)
        rt(360/side)
    end_fill()
    lt(360/side)
    

hideturtle()
mainloop()