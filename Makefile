all:
	FLASK_DEBUG=1 FLASK_APP=run.py flask run

routes:
	FLASK_DEBUG=1 FLASK_APP=run.py flask routes

test:
	black .
