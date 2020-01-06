from turtle import *
speed(7)
width(3)

begin_fill()
fillcolor('black')
circle(100, 180)
circle(200, 180)
circle(100, -180)
end_fill()

pu()
goto(0,-200)
pd()
seth(0)
circle(200, 180)

pu()
goto(0, 130)
begin_fill()
fillcolor('white')
circle(30)
end_fill()

pu()
goto(0, -70)
begin_fill()
fillcolor('black')
circle(30)
end_fill()
ht()

mainloop()

