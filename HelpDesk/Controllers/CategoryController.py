from unicodedata import category

from Models.Category import Category

class CategoryController:
    '''
        Класс для работы с категориями
        Реализация CRUD

        '''


    @classmethod
    def create(cls,name):
        try:
            Category.create(
                name=name
            )
            return f'Категория добавлена '
        except:
            return 'Ошибка добавления категории'

    @classmethod
    def get(cls):
        '''
                Вывод списка категорий из таблицы Category
                :return:
                    список категория (объект)
                '''
        return Category.select()



    @classmethod
    def update(cls,id,name):
         # Обновить запись по id
         Category.update({Category.name:name}).where(Category.id == id).execute()


    @classmethod
    def delete(cls,id):
        '''
        Удалить категорию
        '''
        try:
            query = Category.delete().where(Category.id == id)
            delete_count = query.execute()

            if delete_count >0:
                return True, f"Категория с  {id} удалена"
            else:
                return  False, f"Категория с {id} не найдена "

        except:
            return f"Ошибка при удалении "





if __name__ == "__main__":
    print(CategoryController.create(
        name='Вирусы на компьютере'
    ))
    # print(CategoryController.delete(3))
    # print(CategoryController.update(4,'Сломался цп'))
