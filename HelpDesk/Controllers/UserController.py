from bcrypt import hashpw,gensalt,checkpw
from Models.User import User


class UserController:
    '''
    Класс для работы с пользователями
    Реализация CRUD

    '''
    @classmethod
    def get(cls):
        '''
        Вывод списка пользователей из таблицы User
        :return:
            список пользователей (объект)
        '''
        return User.select()
    @classmethod
    def registration(cls, login, password,role = 'Пользователь'):
        '''
        :param login:  логин пользователя не более 10 символов, должен быть уникален
        :param password: пароль в будущем должен быть в виде HASH пароль
        :param role: роль в системе, если не указана, то: "Пользователь"
        :return:
            если ошибка - возвращаем текст ошибки
            иначе - возвращаем сообщение о созданном пользователе
        '''
        try:
            password = bytes(password, 'utf-8')
            hashed = hashpw(password, gensalt())# введённый пароль кодирует
            User.create(
                login = login,
                password = hashed,
                role = role
            )
            return f'Пользователь {login} с ролью {role} добавлен'
        except:
            return 'Ошибка добавления пользователя'
        User.create(
            login=login,
            password=password,
            role=role
        )
    @classmethod
    def update(cls,id,**kwargs):
        '''

        :param id: по id пользователя будет происходить изменение занчений записи в таблицы
        :param kwargs: вводится название поля и его новое занчение (например: login = "новый_логин")
                за один вызов метода можно изменить несколько полей одной записи
        :return:
            возвращаем сообщение об изменениях пользователе
            если ошибка - возвращаем текст ошибки

        '''
        try:
            for key, value in kwargs.items():# key - название столбца/поля, value - новое значение,  kwargs.items() - аргументы в виде списка словарей
                User.update({key:value}).where(User.id == id).execute()
            return f'У Пользователя изменен {kwargs} на {kwargs[key]} '
        except :
            return 'Ошибка измениния пользователя'
    @classmethod
    def update_status(cls,id):
        '''
        меняет у порльзователя статус с True на False или с False на True
        :param id: id пользователя
        :return:
            новый статус пользователя

        '''
        status = User.get_by_id(id).is_active # получаем по id пользователя его значения поля is_active (True/False)
        User.update({User.is_active:not status}).where(User.id==id).execute()
        return f'Статус пользователя стал {status}'

    @classmethod
    def auth(cls,login,password):
        '''

        :param login:
        :param password:
        :return:
        '''
        # user = User.select().where(User.login == login)[0]
        user = User.get_or_none(User.login==login)
        if user:
            print(type(user.password))
            if checkpw(bytes(password,'utf-8'),bytes(user.password,'utf-8')):
                return "Есть такой пользователь"

        return 'Неверный логин или пароль'


    @classmethod
    def test_hesh(cls,password):
        # Хешируем пароль password
        print(password)
        password = bytes(password,'utf-8')
        hashed = hashpw(password,gensalt())
        print(hashed)
        if checkpw(password,hashed):
            print('Работает')









if __name__ == "__main__":
    # print(UserController.registration(
    #     login='admin2',
    #     password='102030',
    #     role='Специалист'
    # ))
    # UserController.test_hesh('1234')
    # print(UserController.update(2,login = "User"))
    # print(UserController.update_status(2))
    # print(UserController.auth('User1','User'))
    for row in UserController.get():
        print(row.id, row.login, row.password, row.role, row.is_active, row.fullname)

    print(UserController.auth('admin2','102030'))