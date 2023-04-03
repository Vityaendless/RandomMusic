#installed future
from tkinter import *
from random import randint #, choice
from circle import Circle

main = Tk()
main.title("Random music")

#colors = ['white', 'pink', 'yellow', 'purple', 'blue', 'red']
min_choice = 1
max_choice = 100
stop = 0

def random_colour():
    #start['bg'] = choice(colors)
    start['state'] = 'disabled'
    cnvs.itemconfigure(obj_a.obj, fill=obj_a.colour)
    cnvs.itemconfigure(obj_b.obj, fill=obj_b.colour)
    cnvs.itemconfigure(obj_c.obj, fill=obj_c.colour)
    random_choice = randint(min_choice, max_choice)
    if obj_a.status == 1:
        obj_a.choice(obj_b, obj_c, random_choice)
    elif obj_b.status == 1:
        obj_b.choice(obj_a, obj_c, random_choice)
    elif obj_c.status == 1:
        obj_c.choice(obj_a, obj_b, random_choice)

    if stop == 1:
        return stop

    main.after(200, random_colour)

def stoping():
    global stop
    if stop == 0:
        stop = 1
        pause['bg'] = 'red'
    else:
        stop = 0
        pause['bg'] = 'white'
        random_colour()

def circle(canvas, x, y, r):
    id = canvas.create_oval(x - r, y - r, x + r, y + r, fill='white')
    return id

start = Button(main, text='Start', bg='white', command=random_colour)
pause = Button(main, text='Pause', bg='white', command=stoping)
canvas_width = 250
canvas_height = 220
cnvs = Canvas(main, width=canvas_width, height=canvas_height)

start.pack()
pause.pack()
cnvs.pack()

a = circle(cnvs, 50, 50, 40)
obj_a = Circle(a, 'red', 'sound/sound1.mp3', 1, [44, 85])
b = circle(cnvs, 190, 50, 40)
obj_b = Circle(b, 'white', 'sound/sound2.mp3', 0, [22, 88])
c = circle(cnvs, 115, 150, 40)
obj_c = Circle(c, 'white', 'sound/sound3.mp3', 0, [66, 88])

ac = cnvs.create_line(60, 90, 90, 120)
ca = cnvs.create_line(65, 87, 95, 117)
bc = cnvs.create_line(170, 85, 140, 118)
cb = cnvs.create_line(175, 88, 145, 120)
ab = cnvs.create_line(90, 50, 150, 50)
ba = cnvs.create_line(90, 55, 150, 55)

label_a = Label(text="repeat 0,14 %")
label_a.pack()
label_a.place(relx=0.05, rely=0.14)
label_b = Label(text="repeat 0,11 %")
label_b.pack()
label_b.place(relx=0.65, rely=0.14)
label_c = Label(text="repeat 0,11 %")
label_c.pack()
label_c.place(relx=0.35, rely=0.90)

main = mainloop()