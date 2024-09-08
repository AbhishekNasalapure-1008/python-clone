# from turtle import *
# import colorsys

# speed(0)
# bgcolor('black')
# h=0
# for i in range(16):
#     for j in range(18):
#     c=colorsys.hsv_to_rgb(h,1,1)
#     color(c)
#     h+=.005
#     rt(90)
#     circle(150 -j *6,90)
#     lt(90)
#     circle(150-j *6,90)
#     rt(180)
#     circle(40,24)

# done()


from turtle import *
import colorsys
import math

speed(0)
bgcolor('black')
h=0
for i in range(16):
    for j in range(18):
        c=colorsys.hsv_to_rgb(h,1,1)
        c = '#{:02x}{:02x}{:02x}'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255))  # convert to hex color
        color(c)
        h+=0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
        circle(40, 24)

done()