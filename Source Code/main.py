### Importing the required modules
##from tkinter import *
##import time
##
### app specific Variable
##font = "Courier 30 bold"
##app_bg = "#2E2E2E"
##main_frame_bg = "#F5F5DC"
##
##stop_time = None
##
### Function definition for the app
##state = 0
##s_s_state = None
##def update_state(new_state):
##    global state
##    state = new_state
##
##def start_stop_time():
##    global state, t2, run, stop_time
##    # there is the logic for the stop of the time in the if statement
##    if state == 0:
##        s_s_state = True
##        start_button.config(text = "Stop")
##        update_state(new_state=1)  #change the state therefore next time the text changes to start when pressed
##        run = True
##        if stop_time == None:
##            t1 = time.time()
##        else:
##            t1 = time.time() - stop_time
##            stop_time = None
##        while run and s_s_state:
##            t2 = round(time.time() - t1, 1)
##            root.update()
##            Time.set(t2)
##            root.update()
##        
##    # there is the logic for the stop of the time in the if statement
##    else:
##        s_s_state = False
##        start_button.config(text = "Start")
##        start_button.pack(side=RIGHT)
##        update_state(new_state=0)#change the state therefore next time the text changes to stop when pressed
##        stop_time = t2
##        Time.set(t2)
##        run = False
##        
##        
##
##
##def reset_time():
##    global stop_time,  t2
##    t2 = 0
##    Time.set(t2)
##    root.update()
##    stop_time = 0
##    run = False
##
##
### creating the object of tkinter to create the window
##root = Tk()
##root.geometry("600x600")
##root.resizable(False, False)
##root.title("Stop Watch - Hammail")
##
##root.configure(bg = app_bg, relief= GROOVE, borderwidth=2)
##
### Creating the screen for the time as a tkinter frame with label
##screen_label = Frame(root, borderwidth=2, bg=main_frame_bg)
##screen_label.pack()
##
##
##Time = IntVar()
##Time.set(0.00)
##
##time_label = Label(screen_label, bg=main_frame_bg, fg ="#708090", textvariable=Time, font=font)
##time_label.pack()
##
##
### Creating the button for the start stop and reset
##start_button = Button(screen_label , text = "Start", font= font, command=start_stop_time)
##start_button.pack(side=RIGHT)
##update_state(new_state=0)
##
##
##reset_button = Button(screen_label , text = "Reset", font= font, command=reset_time)
##reset_button.pack(side=LEFT)
##
##
##root.mainloop()

from tkinter import *
import time

# App specific Variables
font = "Courier 30 bold"
app_bg = "#2E2E2E"
main_frame_bg = "#F5F5DC"

# Global variables for stopwatch state
running = False  # True if the stopwatch is currently running
start_time = 0.0  # The timestamp when the stopwatch was started or resumed
elapsed_time_at_stop = 0.0  # The total elapsed time when the stopwatch was last stopped

# Function definition for the app
def update_timer():
    global elapsed_time_at_stop

    if running:
        # Calculate current elapsed time
        current_elapsed = time.time() - start_time
        total_display_time = elapsed_time_at_stop + current_elapsed
        Time.set(f"{total_display_time:.1f}") # Format to one decimal place

        # Schedule this function to run again after 100 milliseconds (0.1 seconds)
        root.after(100, update_timer)

def start_stop_time():
    global running, start_time, elapsed_time_at_stop

    if not running:  # If stopwatch is currently stopped, start it
        running = True
        start_button.config(text="Stop")
        start_time = time.time() # Record the current time as the start point for this run
        update_timer() # Start the update loop
    else:  # If stopwatch is currently running, stop it
        running = False
        start_button.config(text="Start")
        # Calculate the total elapsed time up to this stop point
        elapsed_time_at_stop += (time.time() - start_time)
        Time.set(f"{elapsed_time_at_stop:.1f}") # Update display one last time

def reset_time():
    global running, start_time, elapsed_time_at_stop
    running = False
    start_time = 0.0
    elapsed_time_at_stop = 0.0
    Time.set(0.0)
    start_button.config(text="Start") # Ensure button says "Start" after reset

# Creating the object of tkinter to create the window
root = Tk()
root.geometry("600x400") # Adjusted geometry for better fit
root.resizable(False, False)
root.title("Stop Watch - Hammail")

icon_image = PhotoImage(file="icon.png")
root.iconphoto(False, icon_image)

root.configure(bg=app_bg, relief=GROOVE, borderwidth=2)

# Creating the screen for the time as a tkinter frame with label
screen_label = Frame(root, borderwidth=2, bg=main_frame_bg, padx=20, pady=20)
screen_label.pack(pady=50) # Added some padding to center it visually

Time = DoubleVar() # Use DoubleVar for float values
Time.set(0.0)

time_label = Label(screen_label, bg=main_frame_bg, fg="#708090", textvariable=Time, font=font)
time_label.pack(pady=20) # Added some vertical padding for the label

# Creating the button for the start stop and reset
# Use a separate frame for buttons for better layout control
button_frame = Frame(screen_label, bg=main_frame_bg)
button_frame.pack(pady=10)

start_button = Button(button_frame, text="Start", font=font, command=start_stop_time, width=8)
start_button.pack(side=LEFT, padx=10)

reset_button = Button(button_frame, text="Reset", font=font, command=reset_time, width=8)
reset_button.pack(side=RIGHT, padx=10)

root.mainloop()
