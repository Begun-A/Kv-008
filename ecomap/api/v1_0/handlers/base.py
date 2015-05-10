# coding: utf-8
import tornado.web
from api.v1_0.models.user import User


class BaseAPIHandler(tornado.web.RequestHandler):

    ACTIONS = ('create', 'delete', 'edit')

    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        return self.get_secure_cookie('user_name')

    @property
    def user_id(self):
        email = self.get_secure_cookie('email')
        uid = self.db.query(User.id)\
            .filter(User.email == email).one()
        if not uid.id:
            return None
        return int(uid.id)

        # return 3

    # permission id for user
    # @property
    # def permission_id(self):
    #     pass
