from Models.Base import *

class Category(Base):
    id = PrimaryKeyField()
    name = CharField(unique=True,max_length=150)
