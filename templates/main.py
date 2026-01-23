
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>olaaaaaaaaaaaaaaaaaaaaaaaa!</p>"

app = Flask(__name__)
@app.route("/")
def rotta_test():
    return "<p>olaaaaaaaaaaaaaaaaaaaaaaaa!</p>"

app.run(debug=True)