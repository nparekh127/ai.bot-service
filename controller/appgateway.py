from flask import Flask, request
from service.auth.authservice import AuthService


flaskAppInstance = Flask(__name__)


@flaskAppInstance.route('/auth', methods=['POST'])
def validateUser():
    auth = AuthService()

    return auth.validateUser(request)


if __name__ == '__main__':
    flaskAppInstance.run(host="0.0.0.0", port=8181, debug=True)
