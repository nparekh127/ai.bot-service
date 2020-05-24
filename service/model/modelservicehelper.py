from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from flask import jsonify

MODEL_MAPPING = {'LR': LinearRegression(), 'RF': RandomForestRegressor()}


class ModelServiceHelper:

    def prepare_model(self, model_id):
        model = MODEL_MAPPING.get(model_id)

        return jsonify({'auth': model})
