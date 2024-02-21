from my_app.middlewares.config_secret import PORT
from my_app import app

app.run(host='0.0.0.0', port=PORT)