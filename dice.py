import tkinter as tk
from   PIL  import Image, ImageTk
import random

window = tk.Tk()
window.geometry("480x300")
window.title("Dice ROLL")


 # You need to add photo in te folder where the code is saved before running the code
 # photo of dice should have similar name as entered in the list 

          
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1=tk.Label(window, image=image1)
label2=tk.Label(window, image=image2)

label1.image=image1
label2.image=image2 

label1.place(x=80,y=140)
label2.place(x=300,y=140)

def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.iamge=image1
    
    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.iamge=image2
    
button = tk.Button(window, bg='green', fg='white', font='Times 28 bold', text='ROLL', command=dice_roll)
button.place(x=160, y=20)

window.mainloop()