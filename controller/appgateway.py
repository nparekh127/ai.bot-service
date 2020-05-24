from flask import Flask, request
from flask.json import jsonify

from service.auth.authservice import AuthService
from service.file.fileservice import FileService
from service.model.modelservice import ModelService
from service.model.modelservicehelper import ModelServiceHelper

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
        files = FileService.list_files()

        return jsonify({'files': files})

    if request.method == 'POST':
        return file_service.file_meta(request.json['filename'])


@flaskAppInstance.route('/train', methods=['POST'])
def train_model():
    model_service = ModelService()

    if ModelServiceHelper.validate_req(request):
        return model_service.train_model(request.json)
    else:
        return "invalid request"


if __name__ == '__main__':
    flaskAppInstance.run(host="0.0.0.0", port=8181, debug=True)
