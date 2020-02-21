import cv2
from PIL import Image
from PIL import ImageTk
import threading
import tkinter as tk


def button1_clicked():
    thread = threading.Thread(target=videoLoop, args=())
    thread.start()
    
def destroy():
    global exist
    exist=0
    
def videoLoop(mirror=False):
    global exist
    exist=1
    canvas = tk.Canvas(root) 
    canvas.place(x=0,y=60, width=640, height=480)
    canvas.create_rectangle(0,0,640,480,fill = "blue")
    
    No=0
    cap = cv2.VideoCapture(No)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while exist:
        ret, to_draw = cap.read()
        if mirror is True:
            to_draw = to_draw[:,::-1]

        image = cv2.cvtColor(to_draw, cv2.COLOR_BGR2RGB)
        image_1 = Image.fromarray(image)
        image_2 = ImageTk.PhotoImage(image_1)
        #cv2.imshow('test',to_draw)
        canvas.create_image(0, 0, image=image_2, anchor=tk.NW)
    cap.release()
    canvas.destroy()
    
root = tk.Tk()
root.geometry("640x540+0+0")

button1 = tk.Button(root, text="start", bg="#fff", font=("",10), command=button1_clicked)
button1.place(x=585, y=5, width=50, height=25)

button2 = tk.Button(root, text="stop", bg="#fff", font=("",10), command=destroy)
button2.place(x=585, y=30, width=50, height=25)

panel = tk.Label(root,text="image")
panel.place(x=0, y=0)

exist=1

root.mainloop()
