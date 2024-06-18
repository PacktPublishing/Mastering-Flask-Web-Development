
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from tornado.wsgi import WSGIContainer
from tornado.web import FallbackHandler, Application
from tornado.platform.asyncio import AsyncIOMainLoop
from modules_tornado.handlers.home import MainHandler
import asyncio

from a2wsgi import ASGIMiddleware
from main_fastapi import fast_app

from main_sub_flask import flask_sub_app

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modules_django.modules_django.settings') #attributeerror: module 'modules django.modules django.settings' has no attribute 'logging_config'
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true" #django.core.exceptions.SynchronousOnlyOperation: You cannot call this from an async context - use a thread or sync_to_async.

from modules.models.config import database
from modules import create_app
app = create_app('../config_dev.toml')

django_app = StaticFilesHandler(get_wsgi_application()) #ModuleNotFoundError: No module named 'modules_django.settings'

@app.before_request
def db_connect():
    database.connect()
    
@app.teardown_request
def db_close(exc):
    if not database.is_closed():
        database.close()

final_app = DispatcherMiddleware(app, {
    '/fastapi': ASGIMiddleware(fast_app),
    '/django': django_app,
    '/flask': flask_sub_app
})

main_flask = WSGIContainer(final_app)  # intended for Flask
application = Application([
       (r"/ch12/tornado", MainHandler),
       (r".*", FallbackHandler, dict(fallback=main_flask)),
])
   
if __name__ == "__main__":
    #app.run(host="0.0.0.0")
    #http_server = HTTPServer(WSGIContainer(app))
    #http_server.listen(5000)
    #AsyncIOMainLoop().install()
    #asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    application.listen(5000, address="0.0.0.0")
    #IOLoop.instance().start()
    loop.run_forever()
    
    
