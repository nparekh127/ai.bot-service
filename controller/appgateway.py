from flask import Flask, request
from service.auth.authservice import AuthService
from service.file.fileservice import FileService
from service.model.modelservice import ModelService

flaskAppInstance = Flask(__name__)


@flaskAppInstance.route('/auth', methods=['POST'])
def validate_user():
    auth = AuthService()

    return auth.validateUser(request)


@flaskAppInstance.route('/token', methods=['POST'])
def get_token():
    auth = AuthService()

    return auth.generateToken(request)


@flaskAppInstance.route('/upload', methods=['POST'])
def upload_file():
    file_service = FileService()

    return file_service.upload(request.files['file'])


@flaskAppInstance.route('/file', methods=['GET', 'POST'])
def file():
    file_service = FileService()
    if request.method == 'GET':
        return file_service.list_files()

    if request.method == 'POST':
        return file_service.file_meta(request.json['filename'])


@flaskAppInstance.route('/train', methods=['POST'])
def train_model():
    model_service = ModelService()

    return model_service.train_model(request)


if __name__ == '__main__':
    flaskAppInstance.run(host="0.0.0.0", port=8181, debug=True)
