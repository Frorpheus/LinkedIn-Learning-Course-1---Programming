from flask import Flask # Lets you quickly get things going on the web

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World"

app.run(debug=True)
