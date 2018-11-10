from flask import flask,Blueprint
from .api.v1 import superv1
from db_config import create_tables,Destroy_tables

def create_app():
	app=flask(__name__)
	create_tables()

	app.register_Blueprint(superv1)
	app.register_Blueprint(superv2)

	return app