from peewee import *
import src.settings as settings

database = SqliteDatabase(settings.DB_NAME)
database.connect()

class BaseModel(Model):
    class Meta:
        database = database

class Category(BaseModel):
    id = IntegerField(primary_key=True)
    name = TextField(null=False) 
    level = IntegerField(null=False)
    bestOfferEnabled = BooleanField(default=False)
    parent = ForeignKeyField('self', null=True)