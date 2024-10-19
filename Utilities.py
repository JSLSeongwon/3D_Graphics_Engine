#stores all functions and classes so... files are cleaner 

from tkinter import *
import tkinter as tk
import numpy as np
from copy import deepcopy

def my_range(start, end, increment):
    current_value = start
    values = []
    while current_value < end:
        values.append(current_value)
        current_value += increment
    
    return values

def plot(points, canvas, x, y):
    width = (int(canvas['width']) / 2) + x*(int(canvas['width'])/20)
    height = (int(canvas['height']) / 2) - y*(int(canvas['height'])/10)

    radius = 5
    point = canvas.create_oval(width + radius, height + radius, width - radius, height - radius, fill="black", width="1", outline="")
    points.append(point)
    
def my_deep_copy(array):
    deep_array = []
    for point in array:
        deep_array.append(point)
    return deep_array
    # return [x for x in array] #John Leung's deepcopy do not steal

class Counter:
    def __init__(self):
        self.counter = 0
    
    def increment(self):
        self.counter += 1
        print(self.counter)

    def multiply_two(self):
        self.counter *= 2
        print(self.counter)

    def square(self):
        self.counter *= self.counter
        print(self.counter)


class BetterCounter(Counter):
    def subtract(self):
        self.counter -= 1
        print(self.counter)




class point():
    def __init__(self, x, y):
        self.x_point = x
        self.y_point = y
        #self.z_point = z
        self.vector = np.array([x, y]).transpose()

    
    # def rotate():

        





class Canvas_2D(Canvas):
    def __init__(self, root, width, height, bg):
        Canvas.__init__(self, master = root, width = width, height = height, bg = bg)        
        self.root = root
        self.middle_w = 1/2 * int(self['width'])
        self.middle_h = 1/2 * int(self['height'])
        # self.root.bind("<Configure>", self.resize_event)
        self.ticks = []
        self.axis_x = 0
        self.axis_y = 0

        self.points_current = []
        self.points_old = []
        self.xcoords = []
        self.ycoords = []
        self.size = 0


        self.main_x2 = self.root.winfo_width()
        self.main_y2 = self.root.winfo_height()
        self.root.bind("<Configure>", self.resize_event)
        # main_x1 = 0
        # main_y1 = 0
        # main_x2 = Canvas.root.winfo_width()
        # main_y2 = Canvas.root.winfo_height()

        # radius = 50
        # middle_w = 1/2 * int(canvas['width'])
        # middle_h = 1/2 * int(canvas['height'])


        # crosshair = canvas.create_oval(middle_w - radius, middle_h - radius, middle_w + radius, middle_h + radius, fill="DodgerBlue4", outline="red", width="1")

    def resize_event(self, event):
        self.config(width=self.root.winfo_width(), height=self.root.winfo_height())
        self.calculate_middle()
        self.delete(self.axis_x, self.axis_y)
        self.draw_axes()

        for tick in self.ticks:
            self.delete(tick) 
        self.draw_ticks()


        self.points_old = self.points_current

        for point in self.points_current:
            self.delete(point)     # Deletes off the canvas
            # self.size -= 1

        self.points_current = []
        temp_xcoords = my_deep_copy(self.xcoords)
        temp_ycoords = my_deep_copy(self.ycoords)

        for i in range(len(self.ycoords)):     
            # self.points_old = self.points_current   #only resizes one cus the size of self.points is 1 when it gets deleted
            self.plot_points(self.xcoords[i], self.ycoords[i])

        self.xcoords = temp_xcoords
        self.ycoords = temp_ycoords


        #self.points = []        # empty the list

        print(self.xcoords, self.ycoords)

    def calculate_middle(self):
        self.middle_w = 1/2 * int(self["width"])
        self.middle_h = 1/2 * int(self["height"])

    def draw_axes(self):
        self.axis_x = self.create_line(0, self.middle_h, self['width'], self.middle_h, fill="white")
        self.axis_y = self.create_line(self.middle_w, 0, self.middle_w, self['height'], fill="white")

    def draw_ticks(self):
        self.ticks = []
        x_ticks = 20
        increments_x = int(self['width'])/x_ticks
        y_ticks = 10
        increments_y = int(self['height'])/y_ticks

        x_coordinates = my_range(0, int(self['width']), increments_x)
        y_coordinates = my_range(0, int(self['height']), increments_y)
        
        for x in x_coordinates:
            self.ticks.append(self.create_line(x, int(self['height'])/2,  x + 1, int(self['height'])/2, width=10, fill="white")) 
        for y in y_coordinates:
            self.ticks.append(self.create_line(int(self['width'])/2, y, int(self['width'])/2, y + 1, width=10, fill="white")) 



    def plot_points(self, x, y):
        # self.points_current = []
        # self.xcoords = []
        # self.ycoords = []
        width = (int(self['width']) / 2) + x*(int(self['width'])/20)
        height = (int(self['height']) / 2) - y*(int(self['height'])/10)

        radius = 5
        point = self.create_oval(width + radius, height + radius, width - radius, height - radius, fill="black", width="1", outline="")
        self.points_current.append(point)
        print(self.points_current)
        self.xcoords.append(x)
        self.ycoords.append(y)
        # self.size += 1

    
        
        


# a = BetterCounter()
# a.increment()
# a.increment()
# a.increment()
# a.increment()
# a.increment()
# a.increment()
# a.increment()
# a.increment()

# a.multiply_two()
# a.square()
# a.subtract()

if (__name__ == "__main__"):
    # root = tk.Tk()
    # root.geometry('600x400')
    # root.title('3D Engine')

    # root.minsize(600, 400)
    # root.maxsize(1536, 864)

    # canvas = Canvas_2D(root, 600, 400, 'White')

    # canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    # root.mainloop()

    x = point(1,1)
    print(x.vector)
