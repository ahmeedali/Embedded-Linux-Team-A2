from customtkinter import *
from tkinter import *
from math import *
import time
from tkinter import messagebox


window = Tk()
window.geometry("400x800")
window.configure(background="#211d31")
window.resizable(0, 0)
window.title("POMODORO TIMER")
# window.call('wm', 'iconphoto',window._w,PhotoImage(file="on.png"))





def update_clock():
    h   = int(time.strftime("%I"))
    min = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))

    # updating sec hand
    sec_x = sec_hand_len * sin(radians(sec * 6)) + center_x
    sec_y = -1 * sec_hand_len * cos(radians(sec * 6)) + center_y
    canvas_clk.coords(sec_hand, center_x, center_y, sec_x, sec_y)

    # updating min hand
    min_x = min_hand_len * sin(radians(min * 6)) + center_x #
    min_y = -1 * min_hand_len * cos(radians(min * 6)) + center_y
    canvas_clk.coords(min_hand, center_x, center_y, min_x, min_y)

    # updating h hand
    h_x = h_hand_len * sin(radians(h * 30 + 0.5 * min + 0.008 * sec)) + center_x
    h_y = -1 * h_hand_len * cos(radians(h * 30 + 0.5 * min + 0.008 * sec)) + center_y
    canvas_clk.coords(h_hand, center_x, center_y, h_x, h_y)

    window.after(1000, update_clock)


def start_sw ():
    start.configure(file="stop.png")
    start_b.configure(command=stop_sw)
       
def stop_sw(): 
    start.configure(file="start.png") 
    start_b.configure(command=start_sw) 
   



added_tasks = []

def add_task():
    todo = entry.get()
    if todo:
        
        label = CTkLabel(scrollable_frame, text=todo,text_color="white")
        label.pack()
        added_tasks.append(label)
        entry.delete(0, END)
    else:
        messagebox.showinfo("Error", message="Try to enter a task")
        
def remove_task():
    if added_tasks:
        tasks_to_remove = added_tasks.pop()
        tasks_to_remove.destroy()
        save_task()
        
def save_task(): 
    
    with open ("task.txt","w") as f:
        for x in added_tasks:
            f.write(add_task + "\n")
                
def load_tasks():
     try: 
         with open ("task.txt","") as f:
            tasks=f.readlines()
            tasks= added_tasks.get(0,END)
            for x in tasks:
                label = CTkLabel(scrollable_frame, text= x ,text_color="white")
                label.pack()
                added_tasks.append(label)
                
     except FileNotFoundError: 
         pass          
    


# widget 
clk = PhotoImage(file='clock.png')
po=PhotoImage(file="Pomodoro.png")
skip=PhotoImage(file="skip.png")
start=PhotoImage(file="start.png")
stop=PhotoImage(file="stop.png")

# hands postions for clock 
center_x = 195
center_y = 80
# create clock hands
h_hand_len   = 14
min_hand_len = 23
sec_hand_len = 27





canvas_clk = Canvas(window, width=400, height=162,bd=0,background="#211d31",highlightthickness = 0)
canvas_clk.create_image(200, 91, image=clk)

sec_hand = canvas_clk.create_line(194, 80,  sec_hand_len, sec_hand_len, width=1.5, fill='#3b54cd')
min_hand = canvas_clk.create_line(194, 80,  min_hand_len, min_hand_len, width=2  , fill='#e95d5d')
h_hand   = canvas_clk.create_line(194, 80,  h_hand_len  , h_hand_len  , width=2, fill='#e95d5d')
update_clock()




#creating label and button with command order 
tomoto = Label(window,image=po,bg="#211d31",bd=0,highlightthickness = 0)
timer  = Label(window,text="25:00",font=("arial",30),bg="transparent",bd=0,highlightthickness = 0)


#creating label and button with command order 
skip_b =Button(window,image=skip,bd=0,bg="#211d31",highlightthickness = 0,activebackground="#211d31")
start_b=Button(window,image=start,command=start_sw,bd=0,bg="#211d31",highlightthickness = 0,activebackground="#211d31")



title_label = CTkLabel(window, text="Daily Tasks", font=CTkFont(size=20, weight="bold"),text_color="white")
scrollable_frame = CTkScrollableFrame(window, width=400, height=50,fg_color="#211d31")
entry = CTkEntry(scrollable_frame, placeholder_text="Add todo",fg_color="#211d31",text_color="white")
add_button = CTkButton(window, text="Add", width=150, command=add_task,fg_color="#3b54cd",hover_color="#778ef9")
remove_button = CTkButton(window, text="Remove", width=150, command=remove_task,fg_color="#3b54cd",hover_color="#778ef9")





canvas_clk.place(x=0, y=0)

tomoto.place(x=67, y=150)
timer.place(x=67, y=150)
start_b.place(x=140, y=360)
skip_b.place(x=210, y=360)

Label(window,bg="#211d31",bd=0,highlightthickness = 0,).pack(pady=200)

title_label.pack(padx=10,pady=(5,10))
scrollable_frame.pack()
entry.pack(fill="x")
add_button.place (x=20, y=630)
remove_button.place (x=210, y=630)

window.mainloop()