import functools

import tornado.web
import tornado.gen

from sqlalchemy.sql import exists, bindparam, select
from sqlalchemy import and_

from api.v1_0.handlers.base import BaseAPIHandler

from api.v1_0.models.user import User, RolePermission, Roles, Permissions

# just for testing
class PermissionHandler(BaseAPIHandler):

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def delete_permission(self, method):
        @functools.wraps(method)
        def wrap(*args, **kw):
            access = True
            if access:
                return method(self, *args, **kw)
            raise tornado.web.HTTPError(403, 'Permission violation')
        return wrap

    def edit_permission(self, method):
        pass

    def create_permission(self, method):
        pass

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def show_permission(self, method):
        @functools.wraps(method)
        def wrap(*args, **kw):
            access = True
            if access:
                return method(self, *args, **kw)
            raise tornado.web.HTTPError(403, 'Permission violation')
        return wrap


def have_access(permission):
    def access(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kw):
            stmt = exists().where(
                and_(
                    RolePermission.role_id == Roles.id,
                    Roles.id == User.role_id,
                    Permissions.id == RolePermission.permission_id,
                    User.id == self.user_id,
                    Permissions.permission == permission,
                    ))

            if self.db.query(RolePermission).filter(stmt).count():
                return method(self, *args, **kw)
            raise tornado.web.HTTPError(403, 'Permission violation')
        return wrapper
    return access
