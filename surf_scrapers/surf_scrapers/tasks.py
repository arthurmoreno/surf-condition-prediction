import celery

@celery.task(name='hello')
def hello():
    return print('hello world')