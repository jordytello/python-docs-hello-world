from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><!--Synack Responsible Disclosure- Jordy--></body></html>"
