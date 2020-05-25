from service.algorithm.algorithmservicehelper import AlgorithmServiceHelper


class AlgorithmService:

    def init_algorithm(self, algorithm_id, params, attrs):
        algorithm_helper = AlgorithmServiceHelper()

        if not algorithm_helper.validate_params(algorithm_id, params):
            raise Exception("Sorry", "Invalid parameters for given algorithm id")

        if not algorithm_helper.validate_attrs(algorithm_id, attrs):
            raise Exception("Sorry", "Invalid attributes for given algorithm id")

        model = algorithm_helper.get_algorithm(algorithm_id)

        return model
