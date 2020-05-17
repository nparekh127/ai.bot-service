import logging as logger
from flask import jsonify
from service.model.modelservicehelper import ModelServiceHelper

logger.basicConfig(level="DEBUG")

class ModelService:

    def train_model(self, request):
        logger.log(1, "Initiating training", "", "")

        if request['model_id']:
            model_id = request['model_id']

            model_service_helper = ModelServiceHelper()
            return model_service_helper.prepare_model(model_id)

        return jsonify({'status': {'status': 404, 'desc': 'model id not found'}})