from peewee import *

# # Первый способ
# db = MySQLDatabase(
#     'MitnD31_HelpDesk',
#     user='MitnD31_HelpDesk',
#     password='111111',
#     host='10.11.13.118'
# )
# Второй способ
def connect():
    try: # удачная попытка
        database = MySQLDatabase(
            'MitnD31_HelpDesk',
            user='MitnD31_HelpDesk',
            password='111111',
            host='10.11.13.118'
        )
        return database
    except : # неудачная попытка
        print(f'Ошибка')
        return None

if __name__ ==  "__main__":
    print(connect().connect())