import logging as logger
from flask import jsonify
from service.model.modelservicehelper import ModelServiceHelper

logger.basicConfig(level="DEBUG")

class ModelService:

    def train_model(self, model_config_dict):
        logger.log(1, "Initiating training...", "", "")
        model_service_helper = ModelServiceHelper()

        return model_service_helper.prepare_model(model_config_dict)
