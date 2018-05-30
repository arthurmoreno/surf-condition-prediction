from celery import Celery


app = Celery('surf_scrapers')

app.config_from_object('surf_scrapers.celeryconfig')

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(10.0, hello(), name='add every 10')


# @app.task
# def hello():
#     return print('hello world')
