from Connection.connect import *

class Base(Model):
    class Meta:
        database = connect()