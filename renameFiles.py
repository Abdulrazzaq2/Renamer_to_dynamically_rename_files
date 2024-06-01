# this program is to rename files easily and dynamically which really helped me,
# so I decided to share it online to help others :)
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkCustom as btn
# https://www.geeksforgeeks.org/python-gui-tkinter/
# index of 1st file in the selected folder
i = 0
files = []
class Application(object):
    def __init__(self, appName="application"):
        self.width, self.height = 1000, 450
        self.window = tk.Tk()
        self.window.config(background='black')
        self.window.title(appName)
        self.window.maxsize(self.width, self.height)
        self.window.minsize(self.width, self.height)
        self.hover_button_background = '#aa77ff'

def rename():
    print(f'Done renaming {oldName.get()} to {newName.get()}')
    # os.rename(files[i], newName)
def nextFile():
    global i, files
    if i == len(files)-1:
        return # stop if upper limit of array
    print("nextFile...")
    # get next file as i is incremented
    i += 1
    fileName, fileExt = os.path.splitext(files[i])
    oldName.set(fileName)
    newName.set(fileName)
    oldExt.set(" " + fileExt[1:])  # this [1:] for UX to delete the dot (.) from extension
    newExt.set(" " + fileExt[1:])




def prevFile():
    global i, files
    if i == 0:
        return # stop if lower limit of array
    print("Previous File")
    # get next file as i is decremented
    i -= 1
    fileName, fileExt = os.path.splitext(files[i])
    oldName.set(fileName)
    newName.set(fileName)
    oldExt.set(" " + fileExt[1:])  # this [1:] for UX to delete the dot (.) from extension
    newExt.set(" " + fileExt[1:])

# file explorer window
def browseFiles():
    global i, files

    filePath = filedialog.askdirectory()

    # Change label contents
    label_file_explorer.configure(text="Path: " + filePath)
    os.chdir(filePath)
    files = os.listdir()
    # get 1st file as i was = 0
    fileName, fileExt = os.path.splitext(files[i])
    oldName.set(fileName)
    newName.set(fileName)
    oldExt.set(" "+ fileExt[1:])  # this [1:] is for UX to delete the dot (.) from extension
    newExt.set(" "+ fileExt[1:])

app = Application("Renamer RZ")
window = app.window
font = ('Consolas', 18)
# Labels for files clarifying
tk.Label(window, text="old file name =", font=font, background="black", foreground="white").place(x=20, y=150)
tk.Label(window, text=".", font=font, background="black", foreground="white").place(x=675, y=150)
tk.Label(window, text="new file name =", font=font, background="black", foreground="white").place(x=20, y=220)
tk.Label(window, text=".", font=font, background="black", foreground="white").place(x=675, y=220)
tk.Label(window, text=".extension", font=font, background="black", foreground="white").place(x=680, y=100)
# for old and new file names Entries
font = ('Consolas', 15)
oldName = StringVar()
tk.Entry(window, textvariable=oldName, width=40, font=font).place(x=230, y=150)

# Extension of old name like ".mp4"
oldExt = StringVar()
tk.Entry(window, textvariable=oldExt, width=5, font=font).place(x=700, y=150)

newName = StringVar()
tk.Entry(window, textvariable=newName, width=40, font=font).place(x=230, y=220)

# Again extension of new name
newExt = StringVar()
tk.Entry(window, textvariable=newExt, width=5, font=font).place(x=700, y=220)


# buttons
font = ('Consolas', 13)

btn.HoverButton(master=window, text='Rename', background='#999fff',
                             font=font, command=rename,
                             activebackground=app.hover_button_background)\
                            .place(x=300, y=350)
# next file button
btn.HoverButton(master=window, text='Next file', font=font, command=nextFile,
                          background='#999fff', activebackground=app.hover_button_background)\
                         .place(x=420, y=350)
# previous file button
btn.HoverButton(master=window, text='previous file', font=font, command=prevFile,
                          background='#999fff', activebackground=app.hover_button_background)\
                         .place(x=130, y=350)
# Create a File Explorer label
label_file_explorer = Label(window, text="For selecting a folder of files:",
        width=40, height=2,fg="blue", font=font)
label_file_explorer.place(x=10, y=10)

# button select folder
btn.HoverButton(master=window, text="select Folder", font=font, command=browseFiles,
                          background='#00ffff', activebackground= "#0f80ff",\
                          height=2).place(x=380, y=10)

window.mainloop()





