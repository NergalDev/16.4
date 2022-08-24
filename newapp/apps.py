from django.apps import AppConfig
import redis
import newapp.signals

class NewappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newapp'


    def ready(self):


red = redis.Redis(
    host='redis-10332.c273.us-east-1-2.ec2.cloud.redislabs.com',
    port=10332,
    password='3AhbR1HWfwmnKftX15RqkoPH7SzcLPmI'
)

