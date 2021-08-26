from .base import *
import datetime

DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ['*']
    
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'detail': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'info':{
            'level':'INFO',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'detail',
            'filename': os.path.join(LOG_BASE, 'info/boovoice-info-'+datetime.date.today().strftime('%Y%m%d')+'.log'),
            'when': 'D',
            'backupCount' : 3,
            'encoding':'utf8',
        },
        'err':{
            'level':'ERROR',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'detail',
            'filename': os.path.join(LOG_BASE, 'error/boovoice-error-'+datetime.date.today().strftime('%Y%m%d')+'.log'),
            'when': 'D',
            'backupCount' : 3,
            'encoding':'utf8',
        },
        'debug':{
            'level':'DEBUG',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'detail',
            'filename': os.path.join(LOG_BASE, 'debug/debug.log'),
            'when': 'D',
            'backupCount' : 3,
            'encoding':'utf8',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['err',],
            'level': 'ERROR',
            'propagate': False,
        },
        'info': {
            'handlers': ['info'],
            'level': 'INFO',
            'propagate': False,
        },
        'myAppDebug': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}