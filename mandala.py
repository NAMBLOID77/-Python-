import turtle

window = turtle.Screen()

colors=['black','blue']

t = turtle.Pen()
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%2])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.mainloop()
