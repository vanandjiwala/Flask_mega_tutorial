from flask import Flask

app = Flask(__name__)

# import is at bottom to avoid circular import
from app import routes