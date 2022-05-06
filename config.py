import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key=5e54ded54dd3a867c2d020ff50a5d40d'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://carolmaina:ethan2017@localhost/watchlist'

    #SECRET_KEY = os.environ.get('SECRET_KEY')
   

    @staticmethod
    def init_app(app):
        pass


# SECRET_KEY = os.urandom(32)
#app.config['SECRET_KEY'] = SECRET_KEY

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
