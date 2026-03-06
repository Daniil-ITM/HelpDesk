# Информационная система «Техническая поддержка» #
## Наименование проекта ##
*Полное наименование: **Информационная система «Техническая поддержка»(HelpDesk).** *Краткое наименование:* __ИС «TechSupport».__
## **План**
1. Создать диаграмму [x]
2. ~~Создать Базу данных~~ 
3. Разработать структуру проекта[]
4. Написать код в соответствии со структурой [ ]
### Диаграммы ###
Созданы диаграммы Вариантов и классов

### База данных ###
Создана база данных из трех сущностей
+ User
    1. id(int:11)
    2. login(varchar:12)
    3. password
    4. role
    можно выбрать только из трёх вариантов:
       
       -'Пользователь',
       
       -'Администратор',
       
       -Специалист
+ Task
+ Category
### Структура проекта
```
HelpDesk/
|--Connection/
|   |--connect.py               # подключение к БД
|-- Controllers/
|   |-- UserController.py       # Контроллер для работы с пользователями
|   |-- TaskController.py       # Контроллер для работы с заявками 
|   |-- CategoryController.py   # Контроллер для работы с категориями заявок
```
 ### Технологии
- **Python** - основной язык программирования
- **Peewee** - ORM для работы с базой данных
- **MySQL** - СУБД
- **PyMySQL** - библиотека для подключения к СУБД

### Модели ###
### Task(Заявки) ###
- `id` - первичный ключ
- `topic` - тема заявки
- `description` - описание 
- `path` - путь к файлу
- `priority` - приоритет: 'Низкий','Средний','Высокий'
- `status` - Статус: 'Новая','В работе','Выполнена'
- `user_id` - внешний ключ
- `speciality_id` - внешний ключ
- `category_id` - внешний ключ
### Category(Категории) ###
- `id` - первичный ключ
- `name` - Название категории
### create_table ###
Создание таблицы
#### User(Пользователи)
- `id` - первичный ключ
- `login` - логин уникальный, максимум 12 символов
- `password` - хешированный пароль
- `role` -  роль пользователя: 'Пользователь','Администратор','Специалист'
- `is_active` - при создании True, Альтернатива удаления
- `full_name` - полное имя пользователя, максимум 150 символов

## Установка
1. Все библиотеки указаны в файле `requirements.txt`
2. Подключение к БД в `Connection/connect.py`
3. Создать таблицы в БД с помощью
  ```bash
  python Models/create_table.py
  ```

## Функционал кода ##
### Работа с пользователями ###
отвечает UserController
```python
# регистрация пользователя администратора
from Controllers.UserController import UserController
UserController.registration(
        login='admin2',
        password='102030',
        role='Специалист'
    )
# Вывод списка пользователей
for row in UserController.get():
        print(row.id, row.login, row.password, row.role, row.is_active, row.fullname)
# Обновить данные пользователей
UserController.update(2,login = "User")


```
### Работа с заявками ###
отвечает TaskController
```python
# Создание заявки
from  Controllers.TaskController import TaskController
TaskController.create(
        topic='Не устанавливается red os',
        description='Ошибка при первоначальной установки red os',
        path='-',
        priority='Высокий',
        status='В работе'


    )
# Вывод списка заявок
for row in TaskController.get():
        print(row.id, row.topic, row.description, row.path, row.priority, row.status,row.user_id,row.speciality_id,row.category_id)
# Обновить данные заявки
TaskController.update('','')
# Удалить заявку
TaskController.delete(7)
```
### Работа с Категориями ###
отвечает CategoryController
```python
# Создание категории
from  Controllers.CategoryController import CategoryController
CategoryController.create(
          name=''
)
# Вывод список категорий
for row in CategoryController.get():
        print(row.id, row.name)
# Обновить данные категорий
CategoryController.update(1,'')
# Удалить категорию
CategoryController.delete(7)

```
## Лицензия
Проект находится в разработке
