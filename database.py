from pony.orm.core import *

db = Database()


class Words(db.Entity):
    word = Required(str, unique=True)
    definition = Required(str)
    audio = Optional(str)
    details = Optional(str)


class Examples(db.Entity):
    word = Required(str)
    sentence = Required(str)


""" these lines has to be after entity classes """
db.bind(provider='sqlite', filename='db/database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
set_sql_debug(True)
