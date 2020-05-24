from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from flask import jsonify
from sklearn.model_selection import train_test_split

from service.file.fileservice import FileService
import pandas as pd


MODEL_MAPPING = {'LR': LinearRegression(), 'RF': RandomForestRegressor()}
DEFAULT_DATASET_PATH = '../dataset/csv/'

class ModelServiceHelper:

    ######################################################################
    # model_config_dict:  dictionary object contains
    # key param for model training.
    #
    # model_config_dict.model_id        valid model id from MODEL_MAPPING
    # model_config_dict.filename        valid file name with extension
    # model_config_dict.target          valid column name from given file
    # model_config_dict.features        list of features from given file
    # model_config_dict.train_split     percentage of training data
    #######################################################################
    def prepare_model(self, model_config_dict):
        model_id = model_config_dict.get('model_id')
        model = MODEL_MAPPING.get(model_id)

        filename = model_config_dict.get('filename')
        df = pd.read_csv(DEFAULT_DATASET_PATH+filename)

        features = model_config_dict.get('features')
        target = model_config_dict.get('target')
        train_split = int(model_config_dict.get('train_split'))/100

        X_train, X_test, y_train, y_test = train_test_split(df[features], df[target],
                                                            train_size=train_split, random_state=10)

        model = model.fit(X_train, y_train)

        return jsonify({'auth': model.score(X_test, y_test)})

    ##################################################################################
    # check if "model_id" is present and valid
    # check if "filename" is present and valid
    # check if "target" is present and present "filename" columns
    # check if "train_split" is present and "train_split" < 100
    ##################################################################################
    @staticmethod
    def validate_req(request):
        request_body = request.json

        if not request_body['model_id'] and request_body['model_id'] not in MODEL_MAPPING.keys():
            return False
        elif not request_body['filename'] and request_body['filename'] not in FileService.list_files():
            return False
        elif not request_body['target']:
            df = pd.read_csv(request_body['filename'])
            if request_body['target'] not in df.columns.to_list():
                return False
        elif not request_body['train_split'] and (50 > request_body['train_split'] > 100):
            return False

        return True
