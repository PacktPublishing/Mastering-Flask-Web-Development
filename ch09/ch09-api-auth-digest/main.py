from modules import create_app
from modules.services.login_task import get_user_task_wrapper
from modules.models.db import Login
from werkzeug.security import check_password_hash
from flask import abort, make_response, jsonify, session
from cryptography.fernet import Fernet
from werkzeug.datastructures.auth import Authorization

app, celery_app, auth = create_app('../config_dev.toml')

# These values are open for change
server_nonce = "H9OVSzjcB57StMQFPInmX22uZ0Kwu_4JptsWrj0oPpU"
server_opaque = "XJIXDX615CMGXXL0COHQQ0IJRG33OFTNGNFYT72VJ8XF5U3RYZ"

# These HTTP Auth methods are open for change
@auth.generate_nonce
def gen_nonce():
    return server_nonce


@auth.generate_opaque
def gen_opaque():
    return server_opaque

@auth.verify_nonce
def verify_the_nonce(nonce):
    if nonce == server_nonce:
        return True
    else:
        return False

@auth.verify_opaque
def verify_opaque(opaque):
    if opaque == server_opaque:
        return True
    else:
        return False

@auth.get_password
def get_passwd(username):
    print(username)
    task = get_user_task_wrapper.apply_async(args=[username])
    login:Login = task.get()
    with open("enc_key.txt", mode="r") as file:
         enc_key = bytes(file.read(), "utf-8")
    fernet = Fernet(enc_key)
    print(login.password)
    password = fernet.decrypt(login.password).decode('utf-8')
    if login == None:
        return None
    else:
        return password

@auth.get_user_roles
def get_scope(user:Authorization):
    print(type(user), user.username)
    task = get_user_task_wrapper.apply_async(args=[user.username])
    login:Login = task.get()
    return str(login.role)

   
if __name__ == '__main__':
    app.run(host="0.0.0.0")
    