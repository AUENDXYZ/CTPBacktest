# --coding:utf-8--
from peewee import SqliteDatabase, Model, CharField, DateField, ForeignKeyField, IntegerField
from utils.paths import DB

db = SqliteDatabase(DB.joinpath("data.db"))


class Models(Model):
    name = CharField()
    kline_interval = IntegerField()
    direction = CharField()
    modules = CharField(max_length=4096)

    class Meta:
        database = db  # This model uses the "people.db" database.


db.connect()
db.create_tables([Models, ])
