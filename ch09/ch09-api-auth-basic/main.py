from modules import create_app
from modules.services.login_task import get_user_task_wrapper
from modules.models.db import Login
from werkzeug.security import check_password_hash
from flask import abort

app, celery_app, auth = create_app('../config_dev.toml')

@auth.verify_password
def check_password(username, password):
    task = get_user_task_wrapper.apply_async(args=[username])
    login:Login = task.get()
    if login == None:
        abort(403)
    if check_password_hash(login.password, password) == True:
        return login.username
    else:
        abort(403)

   
if __name__ == '__main__':
    app.run()
    