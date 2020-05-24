import logging as logger
import pandas as pd
from flask import jsonify, request
from werkzeug import secure_filename
from os import listdir
from os.path import isfile, join
logger.basicConfig(level="DEBUG")

ALLOWED_EXTENSIONS = set(['csv', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


class FileService:

    ####################
    # uploads file
    ####################
    def upload(self, file):
        filename = secure_filename(file.filename)
        if filename and self.allowed_file_types(filename):
            file.save('../dataset/csv/'+filename)
            return jsonify({'file': {'status': 200, 'desc': 'file saved'}})
        else:
            return jsonify({'file': {'status': 500, 'desc': 'file not saved'}})

    ####################
    # uploads file
    ####################
    def list_files(self, extension=None, path='../dataset/csv/'):
        files = [f for f in listdir(path) if isfile(join(path, f))]

        return jsonify({'files': files})

    ####################
    # uploads file
    ####################
    def file_meta(self, filename, path='../dataset/csv/'):
        extension = filename.rsplit('.', 1)[1].lower()

        if extension == 'csv':
            df = pd.read_csv(path+filename)

        metadata = self.__fetch_metadata(df)
        return jsonify({'metadata': metadata})

    ############################################################
    # Private methods
    ############################################################

    ##############################
    # method to check if file is
    # allowed or not
    ##############################
    def allowed_file_types(self, filename):

        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    #########################
    # fetch the metadata
    # from a pandas data-frame
    #########################
    def __fetch_metadata(self, df):
        meta = {
            'shape': {
                'row': df.shape[0],
                'cols': df.shape[1]
            },
            'desc': self.__desc_dataframe(df.describe())
        }

        return meta

    def __desc_dataframe(self, desc_df):
        col_list = desc_df.columns.to_list()
        desc = {}
        for col in col_list:
            desc[col] = desc_df[col].to_dict()

        return desc