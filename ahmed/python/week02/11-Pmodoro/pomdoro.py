from customtkinter import *
from tkinter import *
from math import *
import time


window = Tk()
window.geometry("400x660")
window.configure(background="#211d31")
window.resizable(0, 0)
window.title("POMODORO TIMER")
# window.call('wm', 'iconphoto',window._w,PhotoImage(file="on.png"))


############################################################################################################

                                      #### Analog clock ####

############################################################################################################


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


canvas_clk = Canvas(window, width=400, height=162,bd=0,background="#211d31",highlightthickness = 0)
canvas_clk.place(x=0, y=0)

# create background
clk = PhotoImage(file='clock.png')
canvas_clk.create_image(200, 91, image=clk)



# create clock hands
# sec hand
center_x = 195
center_y = 80

sec_hand_len = 27
min_hand_len = 23
h_hand_len = 14

sec_hand = canvas_clk.create_line(194, 80,  sec_hand_len, sec_hand_len, width=1.5, fill='#3b54cd')
min_hand = canvas_clk.create_line(194, 80,  min_hand_len, min_hand_len, width=2  , fill='#e95d5d')
h_hand   = canvas_clk.create_line(194, 80,  h_hand_len  , h_hand_len  , width=3.5, fill='#e95d5d')

update_clock()


############################################################################################################

                                      #### Pomodoro Timer ####

############################################################################################################



po=PhotoImage(file="Pomodoro.png")

#creating label and button with command order 
lb_led=Label(window,image=po,bg="#211d31",bd=0,highlightthickness = 0)
lb_led.place(x=67, y=150)

skip=PhotoImage(file="skip.png")
start=PhotoImage(file="start.png")
stop=PhotoImage(file="stop.png")

#creating label and button with command order 
skip_b =Button(window,image=skip,bd=0,bg="#211d31",highlightthickness = 0,activebackground="#211d31")
start_b=Button(window,image=start,bd=0,bg="#211d31",highlightthickness = 0,activebackground="#211d31")
stop_b =Button(window,image=skip,bd=0,bg="#211d31",highlightthickness = 0,activebackground="#211d31")


start_b.place(x=140, y=360)
skip_b.place(x=210, y=360)

Label(window,bg="#211d31",bd=0,highlightthickness = 0,).pack(pady=200)




def add_todo():
    todo = entry.get()
    label = CTkLabel(scrollable_frame, text=todo)
    label.pack()
    entry.delete(0, END)


# title_label = CTkLabel(window, text="Daily Tasks", font=CTkFont(size=30, weight="bold"))
# title_label.pack(padx=10, pady=(40, 20))

scrollable_frame = CTkScrollableFrame(window, width=400, height=50,fg_color="#211d31")
scrollable_frame.pack()

entry = CTkEntry(scrollable_frame, placeholder_text="Add todo",fg_color="#211d31")
entry.pack(fill="x")
add_button = CTkButton(window, text="Add", width=400, command=add_todo,fg_color="#3b54cd",hover_color="#778ef9")
add_button.place (x=0, y=630)
window.mainloop()