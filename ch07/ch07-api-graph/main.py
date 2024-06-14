
from flask import Flask
import toml
from neo4j_config import db_auth

app = Flask(__name__)   
app.config.from_file("config_dev.toml", toml.load)
graph = db_auth()

with app.app_context():
    import modules.api.neo4j_sample

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")