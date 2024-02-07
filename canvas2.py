from tkinter import *
root=Tk()

root.title("Canvas")
root.geometry("600x600")
root.configure(bg="lightblue")

lbl1=Label(root,text="enter a colour",font=("arial",18,"bold"))
lbl1.place(relx=0.5,rely=0.9,anchor=CENTER)

word=Entry(root)
word.insert(0,"blue")
word.place(relx=0.8,rely=0.9,anchor=CENTER)

canvas=Canvas(root,width=590,height=510,bg="white",highlightbackground="lightgrey")
canvas.pack()

direction=""
oldx=50
oldy=50
newx=50
newy=50

def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="right"
    draw(direction,oldx,oldy,newx,newy)
    
def left_dir(event):
    global direction
    global oldx
    global newy
    global oldy
    global newx
    
    oldx=newx
    oldy=newy
    newx=newx-5
    direction="left"
    draw(direction,oldx,oldy,newx,newy)
    
def up_dir(event):
    global direction
    global oldx
    global newy
    global oldy
    global newx
    
    oldx=newx
    oldy=newy
    newy=newy+5
    direction="up"
    draw(direction,oldx,oldy,newx,newy)
    
    
def down_dir(event):
    global direction
    global oldx
    global newy
    global oldy
    global newx
    
    oldx=newx
    oldy=newy
    newy=newy-5
    direction="down"
    draw(direction,oldx,oldy,newx,newy)

def draw(direction,oldx,oldy,newx,newy):
    color=word.get()
    if (direction=="right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=color)
    
    if(direction=="left"):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=color)
        
    if(direction=="up"):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=color)
        
    if(direction=="down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=color)
     
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)


root.mainloop()