from flask import flask,blueprint
from .api.v1 import superv1
from db_config import create_tables

def create_app():
	app=flask(__name__)
	create_tables()

	app.register_blueprint()

	return app