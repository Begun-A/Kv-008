import os

#SQLALCHEMY_DATABASE_URI = 'postgresql://rest:rest@localhost:5432/rest_tutorial'

db_host = 'localhost'
db_user = ''
db_pass = ''
db_name = ''
db_port = 5432
db_engine = 'postgresql'

SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'\
                        .format(db_engine, db_user, db_pass, db_host, db_port, db_name)
