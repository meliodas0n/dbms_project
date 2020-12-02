from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
import sys
import os

root = Tk()
root.title("BROWSE FILES")
root.geometry("800x600")

def browse_files():
    dir_path = filedialog.askdirectory()
    subfolders = [f.path for f in os.scandir(dir_path) if f.is_dir()]

    extensions = ('.mp3', '.flac')
    file_frame = Label(master = fileframe, text = "Files Present", bg = "white", fg = "black")
    file_frame.grid(row = 0, column = 0)
    
    for root, dirs, files in os.walk(dir_path):
        for idx, file in enumerate(files):
            if file.endswith(extensions):
                file_frame_file = Label(master = file_frame, text = file, fg = "black", bg = "white")
                file_frame_file.grid(row = idx + 1, column = 0)

buttonframe = LabelFrame(root, text = "Button", font = ("times new roman", 15, "bold italic"), fg = "white", bg = "black")
buttonframe.place(x = 0, y = 0, width = 800, height = 100)
btn1 = Button(buttonframe, text = "Browse", command = browse_files, font = ("times new roman", 15, "bold italic"), fg = "black", bg = "white").grid(row = 0, column = 0, padx = 10, pady = 7)

fileframe = LabelFrame(root, text = "Files-Present", font = ("times new roman", 15, "bold italic"), bg = "white", fg = "black")
fileframe.place(x = 0, y = 100, width = 800, height = 500)

root.mainloop()