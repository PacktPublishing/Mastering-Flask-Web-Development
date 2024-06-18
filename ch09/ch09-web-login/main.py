from modules import create_app
from modules.services.login_task import get_user_task_wrapper

app, login_auth, celery_app = create_app('../config_dev.toml')

@login_auth.user_loader
def load_user(id):
    task = get_user_task_wrapper.apply_async(args=[id])
    result = task.get()
    return result

# For pyTest, add the following line in TOML file
# LOGIN_DISABLED = False 
    
if __name__ == '__main__':
    app.run()
    