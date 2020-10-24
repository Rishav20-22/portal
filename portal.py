
import os
import tkinter
import time

class graphics:
    def __init__(self, w, h, title):
        ''' Initialize the graphics object.
        Creates a new tkinter Tk object, 
        and a tkinter Canvas object,
        placed insize the Tk object.
        '''
        self.primary = tkinter.Tk()
        self.primary.title(title)
        self.primary.geometry('%dx%d+%d+%d' % (w, h, 50, 100))
        self.canvas = tkinter.Canvas(self.primary, width=w, height=h, highlightthickness=0)
        self.canvas.focus_set()
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.images = {}
        self.frame_count = 0
        self.__handle_motion()

    '''
    BEGIN PRIVATE FUNCTION(S)
    '''

    def __handle_motion(self):
        ''' Ensure mouse x and y coordinates are updated when mouse moves.
        '''
        def motion_action(event):
            self.mouse_x = event.x
            self.mouse_y = event.y
        self.canvas.bind('<Motion>', motion_action)

    '''
    END PRIVATE FUNCTION(S)
    '''

    def resize(self, width, height):
        self.primary.geometry(str(width) + 'x' + str(height))

    def text(self, x, y, content, fill='black', size=17):
        ''' Draw text on the canvas.
        Must always specify the text, x, y position.
        Can optionally specify the fill color and size.
        '''
        text = self.canvas.create_text(x, y, text=content, fill=fill, font=('Arial', size), anchor='nw')
        self.canvas.move(text, 0, 0)
   
    def set_left_click_action(self, callee):
        ''' Call the callee function whenever the left click happens.
        callee should take two parameters, the mouse x and mouse y coordinates.
        '''
        def left_click_action(event):
            callee(self, event.x, event.y)
        ''' <Button-1> is the left-most mouse button '''
        self.canvas.bind('<Button-1>', left_click_action)
    
    def set_right_click_action(self, callee):
        ''' Call the callee function whenever the right click happens.
        callee should take two parameters, the mouse x and mouse y coordinates.
        '''
        def right_click_action(event):
            callee(self, event.x, event.y)
        ''' <Button-2> or <Button-3> is the right-most mouse button.
        Both are set just in case '''
        self.canvas.bind('<Button-2>', right_click_action)
        self.canvas.bind('<Button-3>', right_click_action)
    
    def set_keyboard_action(self, callee):
        ''' Call the callee function whenever a keyboard key is pressed.
        callee should take one parameter, a char representing the key.
        '''
        def keyboard_action(event):
            callee(self, event.char)
        self.canvas.bind('<KeyPress>', keyboard_action)

    def get_color_string(self, red, green, blue):
        ''' accepts three ints that should represent and RGB color.
        Returns a hex string'''
        hex_string = hex(red)[2:].rjust(2, '0') + \
                     hex(green)[2:].rjust(2, '0') + \
                     hex(blue)[2:].rjust(2, '0')
        return '#' + hex_string

    def triangle(self, x1, y1, x2, y2, x3, y3, fill='black'):
        ''' Draw a triangle.
        The three corners of the triangle are specified with the parameter coordinates.
        '''
        r = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=fill)
        self.canvas.move(r, 0, 0)
    
    def line(self, x1, y1, x2, y2, fill='black', width=3):
        ''' Draw a line.
        The two ends of the line are specified with the parameter coordinates.
        '''
        r = self.canvas.create_line(x1, y1, x2, y2, fill=fill, width=width)
        self.canvas.move(r, 0, 0)
    
    def ellipse(self, x, y, w, h, fill='black'):
        ''' Draw an ellipse on the canvas.
        Specify x, y (center of ellipse) and width / height.
        '''
        r = self.canvas.create_oval(x-(w/2), y-(h/2), x+(w/2), y+(h/2), fill="", outline='black',width=3)
        self.canvas.move(r, 0, 0)
    
    def rectangle(self, x, y, w, h, fill='', outline="black"):
        ''' Draw a rectangle on the canvas.
        Specify x, y (top-left corner) and width / height.
        '''
        r = self.canvas.create_rectangle(x, y, x+w, h+y, fill="", outline='black',width=4)
        self.canvas.move(r, 0, 0)
    
    def image(self, x, y, up_scale, down_scale, file_name):
        ''' Draw an image on the canvas.
        Specify x, y (top-left corner) and width / height.
        '''
        if file_name not in self.images:
            self.images[file_name] = tkinter.PhotoImage(file=file_name)
        self.images[file_name] = self.images[file_name].zoom(up_scale, up_scale)
        self.images[file_name] = self.images[file_name].subsample(down_scale, down_scale)
        i = self.canvas.create_image(x, y, anchor='nw', image=self.images[file_name])
        self.canvas.move(i, 0, 0)
        return self.images[file_name]

    def update(self):
        ''' Does an idle task update and regular update.
        '''
        self.primary.update_idletasks()
        self.primary.update()

    def frame_space(self, frame_rate):
        ''' Sleeps for a time that corresponds to the provided frame rate.
        '''
        sleep_ms = 1.0 / float(frame_rate)
        time.sleep(sleep_ms)

    def update_frame(self, frame_rate):
        ''' Updates and sleeps.
        This should be called at the end of each iteration of a users draw loop.
        '''
        self.update()
        self.frame_space(frame_rate)
        self.frame_count += 1
    
    def clear(self):
        ''' Clears the canvas.
        '''
        self.canvas.delete('all')


sketch_name =  input("Enter sketch name:\n")
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

    for i in code2:
        f.write(i)

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
    
    code2.append("mDrawOval(["+str((c1.x1+c1.r1)*0.001)+","+str((c1.x1-c1.r1)*0.001)+"],["+str((c1.y1+c1.r1)*0.001)+","+str((c1.y1-c1.r1)*0.001)+"],32,PI/2,PI/2-TAU);")
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
    code2.append("mLine(["+str(r1.x1*0.001)+","+str(r1.y1*0.001)+"],["+str((r1.x1+r1.w)*0.001)+","+str((r1.y1)*0.001)+"]);")
    code2.append("mLine(["+str(r1.x1*0.001)+","+str(r1.y1*0.001)+"],["+str(r1.x1*0.001)+","+str((r1.y1+r1.h)*0.001)+"]);")
    code2.append("mLine(["+str((r1.x1+r1.w)*0.001)+","+str((r1.y1)*0.001)+"],["+str((r1.x1+r1.w)*0.001)+","+str((r1.y1+r1.h)*0.001)+"]);")
    code2.append("mLine(["+str(r1.x1*0.001)+","+str((r1.y1+r1.h)*0.001)+"],["+str((r1.x1+r1.w)*0.001)+","+str((r1.y1+r1.h)*0.001)+"]);")

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

x = input("")