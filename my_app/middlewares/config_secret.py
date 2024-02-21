from decouple import config

SECRET_KEY = config("SECRET_KEY")
PORT = config("PORT", default=5000, cast=int) 