from flask import jsonify, request
import logging as logger
from werkzeug import secure_filename
logger.basicConfig(level="DEBUG")

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


class FileService:

    def upload(self, file):
        filename = secure_filename(file.filename)
        if filename and self.allowed_file_types(filename):
            file.save('../dataset/csv/'+filename)
            return jsonify({'file': {'status': 200, 'desc': 'file saved'}})
        else:
            return jsonify({'file': {'status': 500, 'desc': 'file not saved'}})

    # Private methods ###########################
    @staticmethod
    def allowed_file_types(filename):

        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
