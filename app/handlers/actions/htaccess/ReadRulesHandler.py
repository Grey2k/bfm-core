from tornado import web
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch

from core import FM


class ReadRulesHandler(BaseHandler):
    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        path = self.get_post('path')
        session = self.get_post('session')

        if path is None:
            self.json({
                'error': True,
                'message': 'no path provided'
            })
            self.finish()
            return

        if session is None:
            self.json({
                'error': True,
                'message': 'no session provided'
            })
            self.finish()
            return

        action = self.get_action(name=FM.Actions.HTACCESS_READ_RULES, module=session.get('type'), path=path,
                                 session=session)
        answer = action.run()

        self.json(answer)
        self.finish()
