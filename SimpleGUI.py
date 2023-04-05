from tkinter import*
count = 0


def click():
    global count
    count += 1
    print(count)


# Window construction
window = Tk()
window.title("GUI")
icon = PhotoImage(file='PyLogo.png')
window.iconphoto(True, icon)
window.config(background='#253747')

# Computer picture
labelPhoto = PhotoImage(file='bg.png')
label = Label(window, text="Hello, World!", font=('Arial', 40, 'bold'), fg='white', bg='#253747', relief=RAISED,
              bd=10, padx=20, image=labelPhoto, compound='bottom')
label.pack()

# Click button
buttonPhoto = PhotoImage(file='mouse.png')
button = Button(window, text='Click here!', command=click, font=("Arial", 30, 'italic', 'bold'), fg="white", bg="#253747",
                activebackground="#253747", activeforeground='grey', state=ACTIVE, image=buttonPhoto, compound='top',
                relief=RAISED, bd=10, padx=106)
button.pack()

window.mainloop()
