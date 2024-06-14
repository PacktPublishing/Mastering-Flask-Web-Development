from modules import create_app

app, celery_app= create_app("../config_dev.toml")

if __name__ == "__main__":
     app.run(debug=False, host='0.0.0.0')
     
     
     
     
     

     
     


