from flask import Flask
from service.auth.authservice import AuthService


app = Flask(__name__)


@app.route('/')
def index():
    auth = AuthService()
    tasks = auth.getName()

    return tasks


if __name__ == '__main__':
    app.run(debug=True)
