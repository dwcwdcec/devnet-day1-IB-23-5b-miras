import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    token_hash8 = os.getenv("TOKEN_HASH8", "missing")
    return render_template("index.html", token_hash8=token_hash8)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
