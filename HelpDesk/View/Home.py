import tkinter
from tkinter import *
from  tkinter import ttk,messagebox

class HomeView(Tk):
    def __init__(self):
        super().__init__()

        #Атрибуты окна
        self.title("Главная")
        self.geometry("1280x800")
        # Главный фрейм
        self.home = ttk.Frame(
            self,
            relief=SOLID,
            borderwidth=1,
            padding=[18]
        )
        self.home.pack(
                       fill=X,
                       pady=10,
                       padx=10)

        self.Home_title = ttk.Frame(self.home,
                                   relief=SOLID,
                                   borderwidth=0,
                                   padding=[8,10])
        self.Home_title.pack(anchor=CENTER,
                             fill=X,
                             padx=10,
                             pady=10)



        self.buttos_frame = ttk.Frame(self.home)
        self.buttos_frame.pack()

        self.title_Home = ttk.Label(self.home,text="Статьи")
        self.title_Home.pack()
        self.reg = Button(self.buttos_frame,text='Зарегистрироваться',command=self.move)
        self.reg.grid(row=0,column=6,sticky='e',padx=5,pady=5)
        self.enter = Button(self.buttos_frame, text='Вход', command=self.move_enter )
        self.enter.grid(row=0,column=8,sticky='w',padx=5,pady=5)
        self.statie1 = ttk.Label(self.home, text='gehhrfnnrnrnrnrnr')
        self.statie1.pack(anchor="sw")
        self.statie2 = ttk.Label(self.home, text='gegegebbfbfbfb')
        self.statie2.pack()
        self.statie3 = ttk.Label(self.home, text='ettegerrbrbrbrbrbr')
        self.statie3.pack(anchor="ne")




    def move(self):
        from View.registration import regView
        window_auth = regView()
        self.destroy()

    def move_enter(self):
        from View.auth import authView
        window_auth = authView()
        self.destroy()




