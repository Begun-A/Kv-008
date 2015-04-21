REST-tutorial
=============

fork from https://github.com/miguelgrinberg/REST-tutorial 

also you need install flask-sqlalchemy in your virtualenv
  `pip install flask-sqlalchemy`

create user in postgres:
    `CREATE USER username WITH password 'password';`

grant access for newly created user to create new DB
    `ALTER USER username CREATEDB;`

change db_user, db_password, db_name in `config.py`

guide to flask-sqlalchemy:
- [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/)
