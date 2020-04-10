import os
from bottle import Bottle, request, route, run
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration  

SERVER_URL = "https://still-escarpment-90121.herokuapp.com"

sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[BottleIntegration()])  
  
app = Bottle()  

@app.route("/")
def index():
    return "<h1> site works. try:http://localhost:8080/success   or   http://localhost:8080/fail</h1>"

@app.route("/success") 
def success():
    return "<h1> /success works </h1>"

@app.route("/fail") 
def fail():    
    raise RuntimeError("There is an error!")
    return



if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)