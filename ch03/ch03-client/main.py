
from app import create_app

app = create_app('../config_dev.toml')

if __name__ == "__main__":
    app.run(port=5001)
    