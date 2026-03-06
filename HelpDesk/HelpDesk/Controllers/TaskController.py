from  Models.Task import Task

class TaskController:
    '''
    Класс для работы с задачами
     Реализация CRUD
    '''

    @classmethod
    def create(cls,topic,description,path,priority,status):
        try:
            Task.create(
                topic=topic,
                description=description,
                path=path,
                priority=priority,
                status=status
            )
            return  f'Задача добавлена'
        except:
            return 'Ошибка добавления задачи'

    @classmethod
    def get(cls):
        '''
                        Вывод списка задач из таблицы Task
                        :return:
                            список задач (объект)
                        '''
        return  Task.select()

    @classmethod
    def update(cls,id,topic):
        # Обновить запись по id
        Task.update({Task.topic:topic}).where(Task.id == id).execute()

    @classmethod
    def delete(cls,id):
        '''
         удалить задачу
        '''
        try:
            query = Task.delete().where(Task.id == id)
            delete_count = query.execute()

            if delete_count >0:
                return True, f"Задача с {id} удалена"
            else:
                return False, f"Задача с {id}не найдена"

        except:
            return  f"Ошибка при удалении"

if __name__ == "__main__":
    print(TaskController.create(
        topic='Не устанавливается red os',
        description='Ошибка при первоначальной установки red os',
        path='-',
        priority='Высокий',
        status='В работе'


    ))

# Вывод списка заявок
for row in TaskController.get():
        print(row.id, row.topic, row.description, row.path, row.priority, row.status,row.user_id,row.speciality_id,row.category_id)
# Обновить данные заявки
TaskController.update('','')