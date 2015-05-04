# coding: utf-8
import tornado.web


class BaseAPIHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie('user_name')
