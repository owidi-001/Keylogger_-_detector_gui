from tkinter import *
from tkinter import messagebox
import backend
import detector


# Launch attack
def attack():
    victim_mail = victim_mail_entry.get()
    print(victim_mail)
    backend.mail_attack(victim_mail)
    messagebox.showinfo('Attack status', 'Check your mail for logs')


if __name__ == '__main__':
    # GUI
    # Top level window
    window = Tk()
    # Window title
    window.title("Hello Hacker..")
    # Window size
    window.geometry('350x200')

    # Spacer Creation
    lbl = Label(window, text="")
    lbl.pack()

    # Input label
    victim_mail_label = Label(window, text='Enter victims mail', font=('calibre', 10, 'bold'))
    victim_mail_label.pack()

    # Spacer Creation
    lbl = Label(window, text="")
    lbl.pack()

    # Input entry box
    victim_mail_entry = Entry(window, font=('calibre', 10, 'normal'))
    victim_mail_entry.pack()

    # Spacer Creation
    lbl = Label(window, text="")
    lbl.pack()

    # Attack button 
    btn = Button(window, text='Lauch Attack', command=attack)
    btn.pack()

    # Spacer Creation
    lbl = Label(window, text="")
    lbl.pack()

    btn_detect = Button(window, text='Detect Local Attack', command=detector)
    btn_detect.pack()

    window.mainloop()
