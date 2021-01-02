from flask import Flask, render_template, redirect
from blueprints.about_bp import about_bp

app = Flask(__name__)
app.register_blueprint(about_bp)

@app.route('/')
def index():
    return render_template('index.html')

app.run(host="127.0.0.1", port=5000,debug=True)