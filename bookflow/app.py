from flask import Flask
from flask_cors import CORS
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Enable CORS for all routes
db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to BookFlow!'




if __name__ == '__main__':
    app.run(debug=True)