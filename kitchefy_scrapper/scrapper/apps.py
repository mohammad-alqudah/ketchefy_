from django.apps import AppConfig

from .test_backgrounjob import runn

class ScrapperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scrapper'
    runn.backgroun_job()
    
