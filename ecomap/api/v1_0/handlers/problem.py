import tornado.web
from api.v1_0.handlers.base import BaseAPIHandler
from api.v1_0.models.user import User
from api.v1_0.handlers.permission import PermissionHandler

permission = PermissionHandler()

class ProblemApiHandler(BaseAPIHandler):

    @tornado.web.authenticated
    def get(self):
        pass

    def post(self):
        pass

    @tornado.web.authenticated
    def put(self):
        pass




class ProblemOfUserAPiHandler(BaseAPIHandler):

    @tornado.web.authenticated
    def get(self):
        pass
        # self.db.query.(self.current_user).get(user_id)