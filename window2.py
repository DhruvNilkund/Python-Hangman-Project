if __name__=='__main__':
    pass
else:
    from tkinter import *
    from tkinter import messagebox


    window_2=Toplevel()
    window_2.config(bg='#03b1fc')
    window_2.geometry('730x720')

    frame2=Frame(window_2,width=680,highlightcolor='red',highlightthickness=5)
    frame2.pack(padx=20,pady=20)

    frame3=Frame(window_2,width=680,highlightcolor='red',highlightthickness=5)
    frame3.pack(padx=20,pady=20)

    h1_image=PhotoImage(file='C:\\Users\\chitt\\Downloads\\Hangman Figures.png')
    h2_image=PhotoImage(file='C:\\Users\\chitt\\Downloads\\Hangman Figures (1).png')
    h3_image=PhotoImage(file='C:\\Users\\chitt\\Downloads\\Hangman Figures (2).png')
    h4_image=PhotoImage(file='C:\\Users\\chitt\\Downloads\\Hangman Figures (3).png')
    h5_image=PhotoImage(file='C:\\Users\\chitt\\Downloads\\Hangman Figures (4).png')
    h6_image=PhotoImage(file='C:\\Users\\chitt\\Downloads\\Hangman Figures (5).png')
    h7_image=PhotoImage(file='C:\\Users\\chitt\\Downloads\\Hangman Figures (6).png')

    figures=[h1_image,h2_image,h3_image,h4_image,h5_image,h6_image,h7_image]

    lb6=Label(window_2,text='Figure',font=('Times of Roman',15),padx=10,pady=10,bg='light yellow',image=figures[0],compound='bottom')
    lb6.image=figures[0]
    lb6.place(x=10,y=100)


    for i in range(65,91):
        if i<78:
            x=chr(i)
            Button(frame2,text=x,padx=14,pady=10,bg='#03e3fc',activebackground='#03e3fc',font=('Times of Roman',15),relief=RAISED,command=lambda x=x: guess_letter(x)).pack(side=LEFT)
            frame2.place(x=0,y=580)
        else:
            y=chr(i)
            Button(frame3,text=y,padx=13.45,pady=10,bg='#03e3fc',activebackground='#03e3fc',font=('Times of Roman',15),relief=RAISED,command=lambda y=y: guess_letter(y)).pack(side=LEFT)
            frame3.place(x=0,y=650)

    
    def guessed_word():
        messagebox.showinfo(title='Hangman Game',message='Let\'s start the game!!')

        global chances
        chances=0
        import random
        Word_to_be_guessed=["PORBANDAR","HIRAKUD","DECIBEL","CRYOMETER","VOLTA","XYLEM","SONAR","CRYOMETER","PACIFIC","THAILAND","CRYOMETER","TOKYO","FEMUR","NORWAY","ROE","CANBERRA"]
        global a
        a=random.choice(Word_to_be_guessed)
        guessed_letter=''
        
        global lb
        if a=='DECIBEL':
            lb=Label(window_2,text='Hint: SI unit of sound',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='XYLEM':
            lb=Label(window_2,text='Hint: Tissue of plant that transports water',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='SONAR':            
            lb=Label(window_2,text='Hint: Instrument to calculate distance of underwater objects',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='PACIFIC':            
            lb=Label(window_2,text='Hint: Deepest ocean in the world',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='THAILAND': 
            lb=Label(window_2,text='Hint: A place where we found white elephants',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='TOKYO':
            lb=Label(window_2,text='Hint: Largest population city in the world',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='FEMUR':
            lb=Label(window_2,text='Hint: Largest bone in human body',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='CANBERRA':
            lb=Label(window_2,text='Hint: Capital of Australia',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='PORBANDAR':
            lb=Label(window_2,text='Hint: Birth Place of Mahatma Gandhiji',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='HIRAKUD': 
            lb=Label(window_2,text='Hint: Longest Dam in the world',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='ROE':
            lb=Label(window_2,text='Hint: The narrowest river in the world',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='CRYOMETER':            
            lb=Label(window_2,text='Hint: Device to measure very low temperature of objects',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='VOLTA':            
            lb=Label(window_2,text='Hint: Who invented the battery?',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)
            
        elif a=='NORWAY': 
            lb=Label(window_2,text='Hint: Which place is known as "Land of the Midnight Sun" in the world',padx=10,pady=10,bg='orange',font=('Times of Roman',20))
            lb.place(x=125,y=20)

        global word1
        word1=' '.join(a)

        global b
        b=StringVar()
        global lb1
        lb1=Label(window_2,textvariable=b,font=('Times of Roman',24))
        lb1.place(x=500,y=200)
        
        b.set(' '.join('_'*len(a)))


    guessed_word()



    def guess_letter(letter):
        global chances
        if chances<6:
            text1=list(word1)
            guessed_word=list(b.get())
         
            if word1.count(letter)>0:
                for i in range(len(text1)):
                    if text1[i]==letter:
                        guessed_word[i]=letter
                    b.set(''.join(guessed_word))

                    if b.get()==word1:
                        messagebox.showinfo(title='Hurrah! ,You won the game',message='Congratulations!, You have guessed the word')
                        Label(window_2,text='Hint: ',padx=10,pady=10,bg='orange',font=('Times of Roman',20)).place(x=125,y=20)
                        continue_game()
                

            else:
                chances+=1
                if chances<5:
                    Label(window_2,text='Figure',font=('Times of Roman',15),padx=10,pady=10,image=figures[chances],compound='bottom').place(x=10,y=100)

                elif chances==5:
                    Label(window_2,text='Figure',font=('Times of Roman',15),padx=10,pady=10,image=figures[chances],compound='bottom').place(x=10,y=100)
                    messagebox.showwarning(title='WARNING!',message='You have last chance to guess the word')

        elif chances==6:
            Label(window_2,text='Figure',font=('Times of Roman',15),padx=10,pady=10,image=figures[chances],compound='bottom').place(x=10,y=100)
            messagebox.showerror(title='Hangman Game',message='GAME OVER! , Better luck next time...')
            Label(window_2,text='Hint: ',padx=10,pady=10,bg='orange',font=('Times of Roman',20)).place(x=125,y=20)
            continue_game()
    
                
    
    

    def continue_game():
        if messagebox.askyesno(title='Hangman Game',message='Do you want to continue this game?'):
            lb.destroy()
            
            lb1.destroy()
            guessed_word()
            lb6=Label(window_2,text='Figure',font=('Times of Roman',15),padx=10,pady=10,bg='light yellow',image=figures[0],compound='bottom')
            lb6.place(x=10,y=100)

        else:
            window_2.destroy()



    window_2.mainloop()
