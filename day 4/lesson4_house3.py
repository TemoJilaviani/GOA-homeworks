from turtle import * 

width(2)
speed(1000)

   #first house
color("red")
begin_fill()
forward(80)
right(90)
forward(80)
right(90)
forward(80)
right(90)
end_fill()


forward(80)
right(180)
forward(80)
left(90)
forward(30)
left(90)
color("blue")
begin_fill()
forward(30)
right(90)
forward(20)
right(90)
forward(30)
end_fill()

penup()
goto(80,2)
pendown()

   #first roof

right(135)
color("brown")
begin_fill()
forward(53.15073)
left(87)
forward(57)
end_fill()
left(138)

penup()
goto(-100,0)
pendown()

   #second house 
 
color("red")
begin_fill()
forward(80)
right(90)
forward(80)
right(90)
forward(80)
right(90)
end_fill()


forward(80)
right(180)
forward(80)
left(90)
forward(30)
left(90)
color("blue")
begin_fill()
forward(30)
right(90)
forward(20)
right(90)
forward(30)
end_fill()

penup()
goto(-20,2)
pendown()
   
   #second roof

right(135)
color("brown")
begin_fill()
forward(53.15073)
left(87)
forward(57)
end_fill()
left(138)

penup()
goto(-200,0)
pendown()

  #third house

color("red")
begin_fill()
forward(80)
right(90)
forward(80)
right(90)
forward(80)
right(90)
end_fill()


forward(80)
right(180)
forward(80)
left(90)
forward(30)
left(90)
color("blue")
begin_fill()
forward(30)
right(90)
forward(20)
right(90)
forward(30)
end_fill()

penup()
goto(-120,2)
pendown()
  
   #third roof

right(135)
color("brown")
begin_fill()
forward(53.15073)
left(87)
forward(57)
end_fill()
left(138)

penup()
goto(-300,200)
pendown()
  
  #first star

color("orange")
left(55)
forward(30)
right(120)
forward(30)
right(140)
forward(40)
right(150)
forward(40)
right(160)
forward(40)

penup()
goto(-200,195)
pendown()
  
   #second star

right(150)
forward(30)
right(120)
forward(30)
right(140)
forward(40)
right(150)
forward(40)
right(160)
forward(40)

penup()
goto(-100,203)
pendown()

   #third star

right(150)
forward(30)
right(120)
forward(30)
right(140)
forward(40)
right(150)
forward(40)
right(160)
forward(40)

penup()
goto(-5,207)
pendown()

   #4th star
 
right(150)
forward(30)
right(120)
forward(30)
right(140)
forward(40)
right(150)
forward(40)
right(160)
forward(40)

penup()
goto(270,250)
pendown()

   #draw sun

color("yellow")
begin_fill()
circle(40)
end_fill()

   #draw yard


penup()
goto(-260,-83)
pendown()

color("green")
begin_fill()

right(205)
forward(450)
right(90)
forward(200)
right(90)
forward(450)
right(90)
forward(200)
end_fill()




exitonclick()

# the end <3 
