from flask import  Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/')
def home():
    return "running Allah ka shukar"
if __name__ == '__main__':
    app.run(debug=True)
