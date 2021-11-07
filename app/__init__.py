from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# import is at bottom to avoid circular import
from app import routes