# Think Python 2
# Chapter 04, page 31 &

import turtle
import math

# 4.3.2 square receives a turtle and length and draws a square
# 4.3.5 updated square to use polyline 
def square(t, len):
  polyline(t, 4, len, 360)
  
# 4.3.3 receives a turtle, number of sides and length and draws polygon
# 4.3.5 upgrade polygon to polyline which includes angle param
def polyline(t, n, len, angle):
  for i in range(n):
    t.fd(len)
    t.lt(angle/n)

# 4.3.4 receives a turtle, radius and degrees and draws arc
# 4.3.5 updated circle to use arc 
def circle(t, r):
  arc(t, r, 360)

# 4.3.5 draws fraction of circle depending on angle
def arc(t, r, angle):
  n = int(angle/4)
  arc_len = 2*math.pi*r*(angle/360)/n
  polyline(t, n, arc_len, angle)

t = turtle.Turtle()
circle(t, 50)
turtle.mainloop()