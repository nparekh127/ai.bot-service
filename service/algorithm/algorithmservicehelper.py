from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression

MODEL_MAPPING = {
    'RPLR': LinearRegression(),
    'RCLR': LogisticRegression(),
    'ETRF': RandomForestRegressor()
}

MODEL_PARAMS = {
    'RPLR': {'fit_intercept': True, 'normalize': False, 'copy_X': True, 'n_jobs': None},
    'RCLR': {},
    'ETRF': {}
}

MODEL_ATTRS = {
    'RPLR': {'coef_': None, 'rank_': None, 'singular_': None, 'intercept_': None},
    'RCLR': {},
    'ETRF': {}
}

class AlgorithmServiceHelper:

    def get_algorithm(self, id):
        """
        returns the algorithm instance for given id

        Parameters
        ----------
        id : valid algorithm id


        Returns
        -------
        Object : returns an instance of scikit-: Nonelearn algorithms.
        """
        if id in MODEL_MAPPING.keys():

            return MODEL_MAPPING.get(id)
        else:
            raise Exception("Sorry, no algorithm found for id: "+id)

    def get_params(self, algorithm_id):
        """
        returns the parameters dict for given algorithm.

        Parameters
        ----------
        algorithm_id : valid algorithm id


        Returns
        -------
        Object : returns an instance of scikit-: Nonelearn algorithms.
        """
        if id in MODEL_PARAMS.keys():

            return MODEL_PARAMS.get(algorithm_id)
        else:
            raise Exception("Sorry, no algorithm found for id: " + id)

    def get_attrs(self, algorithm_id):
        """
        returns the attribute dict for given algorithm.

        Parameters
        ----------
        algorithm_id : valid algorithm id


        Returns
        -------
        Object : returns an instance of scikit-: Nonelearn algorithms.
        """
        if id in MODEL_ATTRS.keys():

            return MODEL_ATTRS.get(algorithm_id)
        else:
            raise Exception("Sorry, no algorithm found for id: " + id)

    def validate_params(self, algorithm_id, params):
        """
        validate the parameters against given algorithm

        Parameters
        ----------
        algorithm_id : valid algorithm id
        params:        dictionary of parameters

        Returns
        -------
        Boolean : return True if provided params are valid.
        """
        actual_params = self.get_params(algorithm_id)
        if params.keys() in actual_params.keys():
            return True
        else:
            return False

    def validate_attrs(self, algorithm_id, attrs):
        """
        validate the parameters against given algorithm

        Parameters
        ----------
        algorithm_id : valid algorithm id
        attrs:        dictionary of attributes

        Returns
        -------
        Boolean : return True if provided attrs are valid.
        """
        actual_attrs = self.get_attrs(algorithm_id)
        if attrs.keys() in actual_attrs.keys():
            return True
        else:
            return False
