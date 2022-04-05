from flask import Flask
from scream.scream import scream

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, World! and {scream()}</p>"

@app.route("/scream")
def scream():
    return f"<p>{scream()}</p>"

if __name__ == "__main__":
    app.run()
