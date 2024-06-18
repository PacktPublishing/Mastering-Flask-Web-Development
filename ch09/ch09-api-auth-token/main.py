from modules import create_app
from jwt import decode

app, celery_app, auth = create_app('../config_dev.toml')

@auth.verify_token
def verify_token(token):
    try:
        data = decode(token, app.config['SECRET_KEY'],
                          algorithms=['HS256'])
    except:  
        return False
    if 'username' in data:
        return data['username']
   
   
if __name__ == '__main__':
    app.run()
    