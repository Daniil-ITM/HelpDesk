from Models.Base import *

class User(Base):
    id = PrimaryKeyField()
    login = CharField(unique=True,max_length=12)
    password = CharField(max_length=255)
    role = CharField(choices=[
        'Пользователь',
        'Администратор',
        'Специалист'
    ])
    is_active = BooleanField(default=True) # Альтернатива удаления
    fullname = CharField(null=True,max_length=150)
