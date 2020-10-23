from graphics import graphics
import os

sketch_name = input("Enter sketch name:\n")
s_name=sketch_name
sketch_name = sketch_name + ".js"
gui = graphics(1000,1000,"Portal")

code= []
code2= []

code.append("function() {")
code.append("    this.label = \'"+s_name+"\';")
code.append("    this.render = function() {")

class line:
    def __init__(self,x11,y11,x22,y22):
        self.x1=x11
        self.x2=x22
        self.y1=y11
        self.y2=y22

class ellipse:
    def __init__(self,x,y,w,h):
        self.x1=x
        self.y1=y
        self.w=w
        self.h=h
class rectangle:
    def __init__(self,x,y,w,h):
        self.x1=x
        self.y1=y
        self.w1=w
        self.h1=h

class cir:
    def __init__(self,x,y,r):
        self.x1=x
        self.y1=y
        self.r1=r
c1 = cir(0,0,0)
r1 = rectangle(0,0,0,0)
l1 = line(0,0,0,0)
e1 = ellipse(0,0,0,0)
def draw_button(x,y,text):
    box_length=len(text)*15
    gui.line(0+x,40+y,box_length+x,40+y,fill="Black",width=3)
    gui.line(box_length+x,0+y,box_length+x,40+y,fill="Black",width=3)
    gui.line(0+x,0+y,0+x,40+y,fill="Black",width=3)
    gui.line(x,y,x+box_length,y,fill="Black",width=3)
    gui.text(10+x,10+y,text,fill="black",size=17)

def on_line_click(callee,x,y):
    if(x>=0 and x<=155 and y>=0 and y<=40):
        gui.set_left_click_action(draw_line)
    if(x>=155 and x<=350 and y>0 and y<=40):
        gui.set_left_click_action(draw_ellipse)
    if(x>=350 and x<=575 and y>0 and y<=40):
        gui.set_left_click_action(draw_rect)
    if(x>=575 and x<=750 and y>0 and y<=40):
        gui.set_left_click_action(draw_circle)
    if(x>=750 and x<=810 and y>0 and y<=40):
        gui.clear()
        code2=[]
        draw_button(0,0,"Draw Line")
        draw_button(155,0,"Draw Ellipse")
        draw_button(350,0,"Draw Rectangle")
        draw_button(575,0,"Draw Circle")
        draw_button(750,0,"Clear")
        draw_button(910,0,"Export")
    if(x>=910 and x<=1000 and y>0 and y<=40):
        gui.set_left_click_action(export)

def export(callee,x,y):
    print("exporting")
    code2.append("}}")
    try:
        os.remove(sketch_name)
    except FileNotFoundError:
        print()
    o = open(str(sketch_name),"x")
    f = open(str(sketch_name),"w")
    for i in code:
        f.write(i)
        f.write("\n")
    for i in code2:
        f.write(i)
        f.write("\n")
    f.close()

def draw_circle(callee,x,y):
    gui.set_left_click_action(set_circle_center)

def set_circle_center(callee,x,y):
    c1.x1=x
    c1.y1=y
    gui.set_left_click_action(set_circumference)

def set_circumference(callee,x,y):
    c1.r1=(x-c1.x1)*2
    gui.ellipse(c1.x1,c1.y1,c1.r1,c1.r1)
    print(c1.x1)
    print(c1.y1)
    print(c1.r1)
    #code2.append("mDrawOval(["+c1.x1*0.001+",-1],[1,1],32,PI/2,PI/2-TAU);")
    gui.set_left_click_action(on_line_click)

def draw_rect(callee,x,y):
    gui.set_left_click_action(start_left_corner_rect)

def start_left_corner_rect(callee,x,y):
    r1.x1=x
    r1.y1=y
    gui.set_left_click_action(set_width_rect)

def set_width_rect(callee,x,y):
    r1.h=y-r1.y1
    gui.set_left_click_action(set_height_rect)

def set_height_rect(callee,x,y):
    r1.w=x-r1.x1
    gui.rectangle(r1.x1,r1.y1,r1.w,r1.h)
    gui.set_left_click_action(on_line_click)

def draw_ellipse(callee,x,y):

    gui.set_left_click_action(start_centre_ellipse)

def start_centre_ellipse(callee,x,y):
    e1.x1=x
    e1.y1=y
    gui.set_left_click_action(set_width)

def set_width(callee,x,y):
    e1.w=(x-e1.x1)*2
    gui.set_left_click_action(set_height)

def set_height(callee,x,y):
    e1.h= (y-e1.y1)*2
    gui.ellipse(e1.x1,e1.y1,e1.w,e1.h)
    e1.x1=0
    e1.y1=0
    e1.w=0
    e1.h=0
    gui.set_left_click_action(on_line_click)


def draw_line(callee,x,y):
    gui.set_left_click_action(start_line)

def start_line(callee,x,y):
    l1.x1=x
    l1.y1=y
    gui.set_left_click_action(finish_line)

def finish_line(callee,x,y):
    l1.x2=x
    l1.y2=y
    gui.line(l1.x1,l1.y1,l1.x2,l1.y2,fill="Black",width=3)
    code2.append("mLine(["+str(l1.x1*0.001)+","+str(l1.y1*0.001)+"],["+str(l1.x2*0.001)+","+str(l1.y2*0.001)+"]);")
    l1.x1=0
    l1.x2=0
    l1.y1=0
    l1.y2=0
    gui.set_left_click_action(on_line_click)

draw_button(0,0,"Draw Line")
draw_button(155,0,"Draw Ellipse")
draw_button(350,0,"Draw Rectangle")
draw_button(575,0,"Draw Circle")
draw_button(750,0,"Clear")
draw_button(910,0,"Export")
gui.set_left_click_action(on_line_click)
