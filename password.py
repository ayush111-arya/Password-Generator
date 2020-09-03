from tkinter import *
import time
import random
import string

class Password:
    def __init__(self,mainframe, *args, **kwargs):
        self.mainframe = mainframe

        self.strength = StringVar(root)
        self.length = StringVar(root)

        Label(mainframe, text='Automatic Password Generator').grid(row=0, column=0)

        self.CHOICES_strength = {'Poor', 'Medium', 'Strong'}
        self.CHOICES_length = {'6', '7', '8'}
        self.strength.set('Select ')
        self.length.set('Select ')

        self.strength_menu = OptionMenu(mainframe, self.strength, *self.CHOICES_strength)
        Label(mainframe, text='Select the strength of password').grid(row=3, column=0)
        self.strength_menu.grid(row=3, column=1)

        self.length_menu = OptionMenu(mainframe, self.length, *self.CHOICES_length)
        Label(mainframe, text='Select the length of the password').grid(row=4, column=0)
        self.length_menu.grid(row=4, column=1)

        self.b = Button(mainframe, text='Generate', command=self.generate_password).grid(row=6, column=0, columnspan=3)

    def generate_password(self):
        a= self.strength.get()
        b= self.length.get()
        if a == 'Poor':
            password_characters = string.ascii_lowercase + string.digits
            password = ''.join(random.choice(password_characters) for i in range(int(b)))

        elif a == 'Medium':
            password_characters = string.ascii_letters + string.digits
            password = ''.join(random.choice(password_characters) for i in range(int(b)))


        elif a == 'Strong':
            password_characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(password_characters) for i in range(int(b)))

        Label(text=password).grid(row=7, column=0)




root = Tk()
root.geometry("400x400")
root.title("Automatic Password Generator")
yo=Password(root)
print(yo)
root.mainloop()


