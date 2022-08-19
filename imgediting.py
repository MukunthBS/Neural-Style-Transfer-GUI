from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

def execute(input_img):
# def execute():

    root = Toplevel()
    # root = Tk()
    root.title('Image Style Transfer')
    root.config(bg='#222222')
    root.geometry('700x700') 

    smallfont = ("Montserrat", 10)
    largefont = ("Montserrat", 20)


    def selected():
        global img_path, img
        # img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        img_path = input_img 
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img1 = ImageTk.PhotoImage(img)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image=img1    

    def blur(event):
        global img_path
        for m in range(0, v1.get()+1):
                img = Image.open(img_path)
                img.thumbnail((350, 350))
                img = img.filter(ImageFilter.BoxBlur(m))
                img = ImageTk.PhotoImage(img) 
                canvas2.create_image(300, 210, image=img)
                canvas2.image=img


    def resize(event):
            for m in range(0, v2.get()+1):
                img = Image.open(img_path)
                img.thumbnail((350, 350))
                width, height = img.size
                img = img.resize((width+(m*10),height+(m*10)))
                img = ImageTk.PhotoImage(img)
                canvas2.create_image(300, 210, image=img)
                canvas2.image=img


    def crop(event):
            for m in range(0, v3.get()+1):
                img = Image.open(img_path)
                width, height = img.size
                # print(width, height)
                img.thumbnail((width/1.8, height/1.8))
                left = 0+(m*10)
                top = 0+(m*10)
                right = 350-(m*10)
                bottom = 350-(m*10)
                img = img.crop((left, top, right, bottom))
                img = ImageTk.PhotoImage(img)
                canvas2.create_image(300, 210, image=img)
                canvas2.image=img

    def rotate_image(event):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            img = img.rotate(int(rotate_combo.get()))
            img = ImageTk.PhotoImage(img)
            canvas2.create_image(300, 210, image=img)
            canvas2.image=img
            
    def flip_image(event):
            global img_path, img8, img9
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            if flip_combo.get() == "Flip Left":
                img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif flip_combo.get() == "Flip Right":
                img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
            img9 = ImageTk.PhotoImage(img8)
            canvas2.create_image(300, 210, image=img9)
            canvas2.image=img9  


    img1 = None
    img3 = None
    img5 = None
    img7 = None
    img9 = None
    img11 = None


    def save():
        global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
        #file=None
        ext = img_path.split(".")[-1]
        file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
        if file: 
                if canvas2.image==img1:
                    imgg.save(file)
                elif canvas2.image==img3:
                    img2.save(file)
                elif canvas2.image==img5:
                    img4.save(file)
                elif canvas2.image==img7:
                    img6.save(file)
                elif canvas2.image==img9:
                    img8.save(file)
                elif canvas2.image==img11:
                    img10.save(file)        
    # create labels, scales and comboboxes
    blurr = Label(root, text="Blur:", font=smallfont,
        bg='#222',
        fg='#fff', width=9, anchor='e')
    blurr.place(x=15, y=8)
    v1 = IntVar()
    scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur) 
    scale1.place(x=150, y=10)


    bright = Label(root, text="Resize:", font=smallfont,
        bg='#222',
        fg='#fff', width=9, anchor='e')
    bright.place(x=8, y=50)
    v2 = IntVar()   
    scale2 = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=resize) 
    scale2.place(x=150, y=55)


    contrast = Label(root, text="Crop:", font=smallfont,
        bg='#222',
        fg='#fff', width=7, anchor='e')
    contrast.place(x=35, y=92)
    v3 = IntVar()   
    scale3 = ttk.Scale(root, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=crop) 
    scale3.place(x=150, y=100)

    rotate = Label(root, text="Rotate:", font=smallfont,
        bg='#222',
        fg='#fff')
    rotate.place(x=370, y=8)
    values = [0, 90, 180, 270, 360]
    rotate_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
    rotate_combo.place(x=460, y=15)
    rotate_combo.bind("<<ComboboxSelected>>", rotate_image)


    flip = Label(root, text="Flip:", font=smallfont,
        bg='#222',
        fg='#fff')
    flip.place(x=400, y=50)
    values1 = ["Flip Left", "Flip Right"]
    flip_combo = ttk.Combobox(root, values=values1, font=('ariel 10 bold'))
    flip_combo.place(x=460, y=57)
    flip_combo.bind("<<ComboboxSelected>>", flip_image)


    canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
    canvas2.place(x=15, y=150)

    btn1 = Button(root, text="Edit Image", font=smallfont,
        bg='#222',
        fg='#fff', relief=GROOVE, command=selected)
    btn1.place(x=100, y=595)
    btn2 = Button(root, text="Save", width=12, font=smallfont,
        bg='#222',
        fg='#fff', relief=GROOVE, command=save)
    btn2.place(x=280, y=595)
    btn3 = Button(root, text="Exit", width=12, font=smallfont,
        bg='#222',
        fg='#fff', relief=GROOVE, command=root.destroy)
    btn3.place(x=460, y=595)
    root.mainloop()

# execute()
