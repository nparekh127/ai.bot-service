import logging as logger
import pandas as pd
from flask import jsonify, request
from werkzeug import secure_filename
from os import listdir
from os.path import isfile, join
logger.basicConfig(level="DEBUG")

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


class FileService:

    # uploads file
    def upload(self, file):
        filename = secure_filename(file.filename)
        if filename and self.__allowed_file_types(filename):
            file.save('../dataset/csv/'+filename)
            return jsonify({'file': {'status': 200, 'desc': 'file saved'}})
        else:
            return jsonify({'file': {'status': 500, 'desc': 'file not saved'}})

    def list_files(self, extension=None, path='../dataset/csv/'):
        files = [f for f in listdir(path) if isfile(join(path, f))]

        return jsonify({'files': files})

    def file1(self, filename, path='../dataset/csv/'):
        extension = filename.rsplit('.', 1)[1].lower()

        if extension == 'csv':
            df = pd.read_csv(path+filename)

        metadata = self.__fetch_metadata(df)
        return jsonify({'metadata': metadata})


    # Private methods ###########################
    @staticmethod
    def __allowed_file_types(self, filename):

        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def __fetch_metadata(self, df):
        meta = {
            'columns': df.columns.to_list(),
            'shape': df.shape
        }

        return meta
