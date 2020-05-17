from sklearn.linear_model import LinearRegression
from flask import jsonify

MODEL_MAPPING = {'LR': LinearRegression()}


class ModelServiceHelper:

    def prepare_model(self, model_id):
        model = MODEL_MAPPING.get(model_id)

        return jsonify({'auth': model})
