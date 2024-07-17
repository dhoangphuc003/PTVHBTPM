import tkinter as tk
from turtle import color

def start_recording():
    status_label.config(text="Recording Started")

def pause_recording():
    status_label.config(text="Recording Paused")

def end_recording():
    status_label.config(text="Recording Ended")

# Function to create the main window
def create_main_window():
    # Initialize the main window
    root = tk.Tk()
    root.title("Frame Recorder")
    root.geometry("600x300")
    root.configure(bg='green')

    # Title label
    title_label = tk.Label(root, text="Frame Recorder", font=("Arial", 24), bg='lightpink')
    title_label.pack(pady=20)

    # FPS input frame
    fps_frame = tk.Frame(root, bg='lightpink')
    fps_frame.pack(pady=10)
    
    fps_label = tk.Label(fps_frame, text="create an", font=("Arial", 14), bg='lightpink')
    fps_label.pack(side=tk.LEFT)
    
    fps_entry = tk.Entry(fps_frame, width=5, font=("Arial", 14))
    fps_entry.pack(side=tk.LEFT, padx=5)
    
    fps_suffix_label = tk.Label(fps_frame, text="fps video", font=("Arial", 14), bg='lightpink')
    fps_suffix_label.pack(side=tk.LEFT)

    # Button frame
    button_frame = tk.Frame(root, bg='green')
    button_frame.pack(pady=20)
    
    
    pause_button = tk.Button(button_frame, text="Pause", font=("Arial", 14), command=pause_recording,bg='blue', fg="white")
    pause_button.pack(side=tk.LEFT, padx=10)
    
    start_button = tk.Button(button_frame, text="Start", font=("Arial", 14), command=start_recording)
    start_button.pack(side=tk.LEFT, padx=10)
    
    end_button = tk.Button(button_frame, text="End", font=("Arial", 14), command=end_recording)
    end_button.pack(side=tk.LEFT, padx=10)

    # Status label
    global status_label
    status_label = tk.Label(root, text="Recording Paused", font=("Arial", 14), bg='lightpink')
    status_label.pack(pady=20)

    # Start the main loop
    root.mainloop()

# Call the function to create the main window
create_main_window()
