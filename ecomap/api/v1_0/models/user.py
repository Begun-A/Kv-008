# coding: utf-8
from sqlalchemy import Column, Integer, String, DateTime, Boolean, and_, exists, ForeignKey
from api.v1_0.models import Base


class UserStatus(Base):
    __tablename__ = 'user_statuses'
    STATUS_INITIAL = 1

    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(75), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
        return "<User('%s')>" % (self.username)

    # def has_permission(self, id):
    #     # permission = self.db.query.filter()
    #     permission = exists().where(RolePermission.user_)
    # def user_id(self, email):
    #     return self.db.query\
    #         .filter(User.email == ":email")\
    #         .params(email=email).first()


class RolePermission(Base):
    __tablename__ = 'rolepermission'

    id = Column(Integer, primary_key=True)
    permission_id = Column(Integer, ForeignKey('permissions.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))


class Roles(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    role = Column(String(100), unique=True)


class Permissions(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, nullable=False)
    permission = Column(String(100), nullable=False)

