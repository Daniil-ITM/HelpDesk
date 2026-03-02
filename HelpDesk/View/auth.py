import tkinter
from  tkinter import *
from tkinter import ttk,messagebox
from Controllers.UserController import *

class authView(Tk):
    def __init__(self):
        super().__init__()

        #Атрибуты окна
        self.title("Авторизация")
        self.geometry("1280x800")
        # Фрейм авторизации
        self.auth_user = ttk.Frame(
            self,
            relief=SOLID,
            borderwidth=1,
            padding=[18]
        )
        self.auth_user.pack(anchor=CENTER,
                            fill=X,
                            pady=10,
                            padx=10)
        self.auth_title_frame = ttk.Frame(self.auth_user,
                                          relief=SOLID,
                                          borderwidth=0,
                                          padding=[8,10])
        self.auth_title_frame.pack(anchor=CENTER,
                                   fill=X,
                                   padx=10,
                                   pady=10)
        self.auth_title = ttk.Label(self.auth_title_frame, text="HelpDesk")
        self.auth_title.pack()
        # Фрейм в input
        self.input_get_user = ttk.Frame(self.auth_user,
                                        relief=SOLID,
                                        borderwidth=1,
                                        padding=[8,10])
        self.input_get_user.pack(fill=X,
                                 padx=10,
                                 pady=10)
        # Окна ввода данных пользователя для добавления в таблицу БД
        self.log = ttk.Label(self.input_get_user,text='Логин')
        self.log.pack()
        self.login = ttk.Entry(self.input_get_user)
        self.login.pack()
        self.pas = ttk.Label(self.input_get_user, text='Пароль')
        self.pas.pack()
        self.password = ttk.Entry(self.input_get_user)
        self.password.pack()
        self.vxod = ttk.Button(self.input_get_user,text='Войти')
        self.vxod.pack()
        self.reg = ttk.Label(self.input_get_user, text='Нет аккаунта?')
        self.reg.pack()


if __name__ == "__main__":
    window = authView()
    window.mainloop()