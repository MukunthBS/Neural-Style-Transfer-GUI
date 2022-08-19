from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import time
import imgediting
import styletransfer
import os

ws = Tk()
ws.title('Image Style Transfer')
ws.config(bg='#222222')
ws.geometry('640x640') 

smallfont = ("Montserrat", 10)
largefont = ("Montserrat", 20)



def onHover(button):
  
    button.bind("<Enter>", func=lambda e: button.config(
        background='#333'))

    button.bind("<Leave>", func=lambda e: button.config(
        background='#222'))
    
input_file_path = []
input_img = ""
style_img = ""
    
def open_file(prevframe, newframe):
    file_path = askopenfilename(filetypes=[('Image Files', ('.png', '.jpg', '.jpeg','jfif'))])
    if file_path:
        global input_file_path
        input_file_path.append(file_path)
        get_paths()
        uploadFiles(prevframe, newframe)

def get_paths():
    global input_img
    global style_img
    global input_file_path
    input_img = input_file_path[0]
    if(len(input_file_path)>1):
        style_img = input_file_path[1]


homePage = Frame(ws, bg='#222')

imgstyle = Label(homePage, text='Image Style Transfer', font=largefont, bg='#222', fg='#fff')
imgstyle.grid(row=0, columnspan=10, pady=10)

imgbtn = Button(homePage, text ='Select Image', font=smallfont, borderwidth=1, bg='#222', fg='#fff', command = lambda:open_file(homePage, editPage))
imgbtn.grid(row=2, columnspan=10, pady=50)
onHover(imgbtn)


homePage.grid(row=2, columnspan=10)


editPage = Frame(ws, bg='#222')

edit = Label(editPage, text='Do you want to edit the image?', font=largefont, bg='#222', fg='#fff')
edit.grid(row=0, columnspan=10, pady=10)

editbtn = Button(editPage, text ='Edit Image', font=smallfont, borderwidth=1, bg='#222', fg='#fff', command = lambda:imgediting.execute(input_img)) 
editbtn.grid(row=2, columnspan=10, pady=50)
onHover(editbtn)

skipbtn = Button(editPage, text ='Skip', font=smallfont, borderwidth=1, bg='#222', fg='#fff', command = lambda:nextPage(editPage, stylePage)) 
skipbtn.grid(row=3, columnspan=10, pady=10)
onHover(skipbtn)

editPage.grid(row=2, columnspan=10)

editPage.grid_remove()



stylePage = Frame(ws, bg='#222')

style = Label(stylePage, text='Upload Style', font=largefont, bg='#222', fg='#fff')
style.grid(row=0, columnspan=10, pady=10)

stylebtn = Button(stylePage, text ='Upload Style ', font=smallfont, borderwidth=1, bg='#222', fg='#fff', command = lambda:open_file(stylePage, transferPage))
stylebtn.grid(row=2, columnspan=10, pady=50)
onHover(stylebtn)

stylePage.grid(row=2, columnspan=10)

stylePage.grid_remove()


v1 = DoubleVar()

transferPage = Frame(ws, bg='#222')

transfer = Label(transferPage, text='Transfer Style', font=largefont, bg='#222', fg='#fff')
transfer.grid(row=0, columnspan=10, pady=10)

canvas= Canvas(transferPage, width= 600, height= 400)
print(input_img)

s1 = Scale(transferPage, variable = v1, from_ = 1, to = 200, orient = HORIZONTAL, bg='#222', fg='#fff')
s1.grid(row=1, columnspan=10, pady=20)

transferbtn = Button(transferPage, text ='Generate ', font=smallfont, borderwidth=1, bg='#222', fg='#fff', command = lambda:styletransfer.execute(input_img,style_img,s1.get()))
transferbtn.grid(row=4, columnspan=10, pady=50)
onHover(transferbtn)


transferPage.grid(row=2, columnspan=10)

transferPage.grid_remove()



def uploadFiles(prevframe, newframe):
    pb1 = Progressbar(ws, orient=HORIZONTAL, length=300, mode='determinate')
    pb1.grid(row=3, columnspan=10)
    for i in range(50):
        ws.update_idletasks()
        pb1['value'] += 5
        time.sleep(0.01)
    pb1.destroy()
    time.sleep(0.5)
    nextPage(prevframe, newframe)
    

def nextPage(prevframe, newframe):
    prevframe.grid_remove()
    newframe.grid()



n_rows = 5
n_columns = 6
for j in range(n_rows):
    ws.grid_rowconfigure(j, weight = 1)
for j in range(n_columns):
    ws.grid_columnconfigure(j, weight = 1)


ws.mainloop()
