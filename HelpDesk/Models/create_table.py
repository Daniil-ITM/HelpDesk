from Models.Base import *
from Models.Category import Category
from Models.Task import Task
from Models.User import User

connect().create_tables(
    [
        User,
        Task,
        Category

    ]
)