import os

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from service_api import api_v1


class CustomFlaskApp(Flask):
    pass


app = CustomFlaskApp(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

api_v1.load_api(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = scoped_session(sessionmaker(bind=engine))
