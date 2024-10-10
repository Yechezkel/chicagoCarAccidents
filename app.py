from flask import Flask
from routes.accident_bp import accident_bp
app = Flask(__name__)


app.register_blueprint(accident_bp)





@app.route('/')
def home_page():
    return 'Wellcome to the home page!'


if __name__ == '__main__':
    app.run()
