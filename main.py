from flask import Flask, render_template
from flask import template_rendered
from contextlib import contextmanager

app = Flask(__name__,static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    