from flask import Flask, render_template
from distance.distance import distance
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(distance, url_prefix="/distance")

@app.route('/', methods=['POST','GET'])
def index():
    # return "Hello, World!"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)