from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry('720x720')

window.title('Hangman Game')

window.config(bg='black')

icon_photo=PhotoImage(file='F:\\PES\\B_Tech (Sem_1)\\Python Language\\hangman_iconphoto.png')
window.iconphoto(True,icon_photo)

w_image=PhotoImage(file='C:\\Users\\chitt\\Downloads\\Hangman_photo_window.png')

y_image=PhotoImage(file='C:\\Users\\chitt\\Downloads\\yes_icon (1) (1).png')

frame=Frame(window,width=700,bg='black')
frame.grid(row=0,column=0,padx=110,pady=10)

lb1=Label(frame,text='Hangman Game',fg='Yellow',bg='black',font=('Lucida Calligraphy',35),bd=10,padx=15,pady=50,image=w_image,compound='bottom')
lb1.grid(row=0,column=5,columnspan=2)

list1=Listbox(frame,bg='#fcd703',fg='black',font=('Times of Roman',20),width=15,selectbackground='green',relief=SUNKEN,bd=10,cursor='arrow')
list1.grid(row=1,column=5,columnspan=3)

list1.insert(1,'Play Game')
list1.insert(2,'Quit')

list1.config(height=list1.size())



def submit():
    if list1.get(list1.curselection())=='Quit':
        if messagebox.askyesnocancel(title='EXIT',message='Are you sure that you want to quit the game?'):
            window.destroy()
        else:
            pass
    else:
        window_1=Toplevel()
        window_1.geometry('720x720')
        window_1.config(bg='Black')

        frame1=Frame(window_1,width=700,bg='black',highlightcolor='red',highlightthickness=5)
        frame1.grid(row=0,column=0,padx=10,pady=10)
        
        lb2=Label(frame1,text='Hi, Welcome to Hangman Game...',fg='Yellow',bg='Black',font=('Lucida Calligraphy',25),padx=50,pady=10)
        lb2.grid(row=0,column=0)
        
        lb3=Label(frame1,text='Enter your name:',fg='Yellow',bg='Black',font=('Times of Roman',20),width=20,pady=40)
        lb3.grid(row=1,column=0,sticky=W)

        entry1=Entry(frame1,fg='Blue',bg='light yellow',font=('Times of Roman',25))
        entry1.grid(row=1,column=0,sticky=W,padx=300)

        entry1.insert(0,'User')

        def submit1():
            if len(entry1.get())==0:
                messagebox.showerror(title='ERROR!',message='You haven\'t entered your name... Enter your name to proceed.')
            
            else:
                if messagebox.askyesno(title='Hangman Game',message=entry1.get()+', Are you ready ready to play the game?'):
                                   messagebox.showinfo(title='Wishes',message='All the best!!!')
                                   import Hangman_Project_CSE_1st_Year_Part_2
                                   
                                   
                else:
                    pass
               
        def backspace():
            entry1.delete(len(entry1.get())-1,END)
             
        def delete():
            entry1.delete(0,END)

        def quit1():
            if messagebox.askyesnocancel(title='EXIT',message='Are you sure that you want to quit the game?'):
                window.destroy()
            else:
                pass

        frame2=Frame(frame1,width=500,bg='black')
        frame2.grid(row=3,column=0,padx=10,pady=10)    

        

        button1 = Button(frame2,text='Clear',command=delete,padx=3,pady=3,font=('Times of Roman',18),bg='#03b6fc',activebackground='#03b6fc',relief=RAISED,bd=5)
        button1.grid(row=0,column=0,padx=10)

        button2 = Button(frame2,text='Submit ',command=submit1,padx=3,pady=3,font=('Times of Roman',18),bg='#03b6fc',activebackground='#03b6fc',relief=RAISED,bd=5)
        button2.grid(row=0,column=1,padx=10)

        button3= Button(frame2,text='Quit',command=quit1,padx=3,pady=3,font=('Times of Roman',18),bg='#03b6fc',activebackground='#03b6fc',relief=RAISED,bd=5)
        button3.grid(row=0,column=2,padx=10)




button = Button(frame,text='Submit ',command=submit,padx=3,pady=3,font=('Times of Roman',18),bg='#03b6fc',activebackground='#03b6fc',relief=RAISED,bd=5,image=y_image,compound='right')
button.grid(row=3,column=5,columnspan=3,rowspan=10,pady=30)


window.mainloop()
