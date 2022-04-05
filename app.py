from flask import Flask
from scream.scream import scream as scream_fn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"

@app.route("/scream")
def scream():
    return f"<p>{scream_fn()}</p>"

if __name__ == "__main__":
    app.run(debug=False)
