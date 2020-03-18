from Valentines import app
from flask_debug import Debug
import os
from flask import Flask
from flask_sslify import SSLify


if __name__ == '__main__':

  port = int(os.environ.get("PORT", 5000))
  
  # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  # sslify = SSLify(app)
  app.run(host='0.0.0.0', port=port, debug=False)
  # Debug(app)
  # app.run(debug=True)