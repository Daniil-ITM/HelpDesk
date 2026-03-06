import tkinter
from tkinter import *
from tkinter import ttk,messagebox
from Controllers.UserController import *
from peewee import text_type

class regView(Tk):
    def __init__(self):
        super().__init__()

        #Атрибуты окна
        self.title("Регистрация")
        self.geometry("1280x800")
        # Фрейм регистрации
        self.reg_user = ttk.Frame(
            self,
            relief=SOLID,
            borderwidth=1,
            padding=[18]
        )
        self.reg_user.pack(anchor=CENTER,
                           fill=X,
                           pady=10,
                           padx=10)
        self.title_reg = ttk.Frame(self.reg_user,
                                     relief=SOLID,
                                     borderwidth=0,
                                     padding=[8,10])
        self.title_reg.pack(anchor=CENTER,
                              fill=X,
                              padx=10,
                              pady=10)



        self.reg_title = ttk.Label(self.reg_user,text="Help Desk")
        self.reg_title.pack()
        # Фрейм в input
        self.input_get_user = ttk.Frame(self.reg_user,
                                        relief=SOLID,
                                        borderwidth=1,
                                        padding=[8, 10])
        self.input_get_user.pack(fill=X,
                                 padx=10,
                                 pady=10)
        # Окна ввода данных пользователя
        self.log = ttk.Label(self.input_get_user,text='Логин')
        self.log.pack()
        self.login = ttk.Entry(self.input_get_user)
        self.login.pack()
        self.pas = ttk.Label(self.input_get_user,text='Пароль')
        self.pas.pack()
        self.password = ttk.Entry(self.input_get_user,show='*')
        self.password.pack()
        self.rol = ttk.Label(self.input_get_user,text='Выберите свою роль')
        self.rol.pack()
        roles = ['Пользователь','Администратор','Специалист']
        self.role = ttk.Combobox(self.input_get_user,values=roles)
        self.role.pack()
        self.reg = ttk.Button(self.input_get_user,text='Зарегистрироваться',command=self.add_reg)
        self.reg.pack()
        self.pere =Button(self.input_get_user, text='Уже есть аккаунт?',fg="blue",cursor="hand2",command=self.move,borderwidth=0)
        self.pere.pack()

    def move(self):
        from View.auth import authView
        window_auth = authView()
        self.destroy()

    def add_reg(self):
        self.login = self.login.get()
        self.password = self.password.get()
        self.role = self.role.get()
        UserController.registration(
            self.login,
            self.password,
            self.role
        )
#     # Очистить поля ввода
#         self.clear()
#
#     def clear(self):
#         '''
#         Метод очистит окна TreeView
#         '''
#         self.login.delete(0,END)
#         self.password.delete(0,END)
# if __name__ == "__main__":
#     window = regView()
#     window.mainloop()