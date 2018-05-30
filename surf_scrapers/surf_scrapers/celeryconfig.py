from celery.schedules import crontab

## Broker settings.
broker_url = 'amqp://guest:guest@rabbitmq:5672/guest'

# List of modules to import when the Celery worker starts.
imports = ('surf_scrapers.tasks',)

timezone = 'America/Recife'

beat_schedule = {
    'add-every-30-seconds': {
        'task': 'waves-crawler',
        'schedule': crontab(minute='*/15')
    },
}
