import os, secret

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = (os.environ.get('MAIL_USE_TLS') is not None) or secret.MAIL_USE_TLS
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or secret.MAIL_USERNAME
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or secret.MAIL_PASSWORD
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'jarmeisterbot@gmail.com'
    ADMINS = ['jarmeisterbot@gmail.com']
    POSTS_PER_PAGE = 15
