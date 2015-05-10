# coding: utf-8
import tornado.web
import tornado.escape

from api.v1_0.handlers.base import BaseAPIHandler
from api.v1_0.handlers.permission import have_access


class UserAPIHandler(BaseAPIHandler):

    @have_access('create')
    @tornado.web.authenticated
    def get(self):
        email = self.get_secure_cookie('email')
        return self.write({'user_name': self.current_user, 'email': email})

    @tornado.web.authenticated
    def post(self):
        return self.write({'user': 'post'})

    @tornado.web.authenticated
    def delete(self):
        return self.write({'user': 'delete'})


    def put(self, user):
        return self.write({'user': 'put'})