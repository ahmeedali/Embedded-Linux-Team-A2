from customtkinter import *
from tkinter import *
from math import *
import time
from tkinter import messagebox
import threading
import requests



window = Tk()
window.geometry("400x800")
window.configure(background="#211d31")
window.resizable(0, 0)
window.title("POMODORO TIMER")




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
    


    
start_timer = True
skip_timer  = False
stop_timer  = False
cycles      = 0  


def run_time (Mode):
    minutes,seconds = divmod (Mode , 60 )
    counter.configure(text=f"{minutes:02d}:{seconds:02d}")
    window.update()
    time.sleep(1)
    
def start_pomodoro():
    
    global start_timer 
    global skip_timer  
    global stop_timer
    global cycles 
    start_timer = True
    skip_timer  = False
    stop_timer  = False
    
    work_session = 25 * 60
    long_break   = 2 * 60
    short_break  = 1 * 60
    
    if start_timer:
            messagebox.showinfo("Work Session", message="Focus on your task for 25 minutes.")

            while work_session > 0 and not (stop_timer or skip_timer):
                run_time(work_session)
                work_session -= 1

            if skip_timer or not stop_timer:
                cycles += 1
                if cycles % 4 == 0:
                    messagebox.showinfo("Long Break", message="Take a 15-minute break.")
                    while long_break > 0 and not stop_timer:
                        run_time(long_break)
                        long_break -= 1
                else:
                    messagebox.showinfo("Short Break", message="Take a 5-minute break.")
                    while short_break > 0 and not stop_timer:
                        run_time(short_break)
                        short_break -= 1

                start_pomodoro()

        
               
                              
        
def skip_pomodoro():
    global start_timer 
    global skip_timer  
    global stop_timer
    skip_timer  = True
    stop_timer  = False
    start_timer = True
    

def end_pomodoro():
    global start_timer 
    global skip_timer  
    global stop_timer
    global cycles
    skip_timer  = False
    stop_timer  = True
    start_timer = False
    
    messagebox.showinfo("Pomodoro Ended", message="Pomodoro ended. Take a longer break.")
    counter.configure(text="00:00")
    cycles = 0
    
    
    
    
    
def start_sw():
    start.configure(file="Stop.png")
    start_b.configure(command=stop_sw)
    timer_thread = threading.Thread(target=start_pomodoro)
    timer_thread.start()
    
    

def stop_sw():
    start.configure(file="Start.png")
    start_b.configure(command=start_sw)
    end_pomodoro()       


added_tasks = []

def add_task():
    todo = entry.get()
    if todo:
        label = CTkLabel(scrollable_frame, text=todo,text_color="white")
        label.pack()
        added_tasks.append(label)
        entry.delete(0, END)
    else:
        messagebox.showinfo("Error", message="Try to enter a task")\
            
#shortcut            
def key_press(event):
    if event.keysym == "Return":
        add_task()
        
window.bind("<Key>", key_press)
                
def remove_task():
    if added_tasks:
        tasks_to_remove = added_tasks.pop()
        tasks_to_remove.destroy()

def activity_generator():
     url = requests.get ("https://www.boredapi.com/api/activity")
     messagebox.showinfo("Activity Generator", message=f"{url.json()['activity']}")

    
# will add it in v2 isa       
# def save_task():
#     with open("tasks.txt", "w") as f:
#         for task in added_tasks:
#             f.write(task["text"] + "\n")
                
# def load_tasks():
#     try:
#         with open("tasks.txt", "r") as f:
#             tasks = f.readlines()
#             for task in tasks:
#                 label = CTkLabel(scrollable_frame, text=task.strip(), text_color="white")
#                 label.pack()
#                 added_tasks.append(label)
#     except FileNotFoundError:
#         pass
              
    

# widget 
clk   = PhotoImage(file="Clock.png")
timer = PhotoImage(file="Timer.png")
skip  = PhotoImage(file="Skip.png")
start = PhotoImage(file="Start.png")
stop  = PhotoImage(file="Stop.png")




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
tomoto = Label(window,image=timer,bg="#211d31",bd=0,highlightthickness = 0)
counter = Label(window,text="00:00",font=("DS-Digital",40,"bold"),bg= "#263138",bd=0,highlightthickness = 0,fg="#91e2a8")


#creating label and button with command order 
skip_b =Button(window,image=skip,command=skip_pomodoro,bd=0,bg="#211d31",highlightthickness = 0,activebackground="#211d31")
start_b = Button(window,image=start,command=start_sw,bd=0,bg="#211d31", highlightthickness=0, activebackground="#211d31")



title_label = CTkLabel(window, text="Daily Tasks", font=CTkFont(size=20, weight="bold"),text_color="white")
scrollable_frame = CTkScrollableFrame(window, width=400, height=50,fg_color="#211d31")
entry = CTkEntry(scrollable_frame, placeholder_text="Add Todo Taskes",fg_color="#211d31",text_color="white")
add_button = CTkButton(window, text="Add", width=170, command=add_task,fg_color="#3b54cd",hover_color="#778ef9")
remove_button = CTkButton(window, text="Remove", width=170, command=remove_task,fg_color="#3b54cd",hover_color="#778ef9")
act_button = CTkButton(window, text="Suggested activities",height= 40, width=300, command=activity_generator,fg_color="#3b54cd",hover_color="#778ef9")



canvas_clk.place(x=0, y=0)

tomoto.place(x=15, y=150)
counter.place(x=72, y=295)
start_b.place(x=310, y=220)
skip_b.place(x=310, y=320)

Label(window,bg="#211d31",bd=0,highlightthickness = 0,).pack(pady=200)

title_label.pack(padx=10,pady=(20,10))
scrollable_frame.pack()
entry.pack(fill="x")
add_button.place (x=20, y=680)
remove_button.place (x=210, y=680)
act_button.place (x=50, y=740)

window.mainloop()
