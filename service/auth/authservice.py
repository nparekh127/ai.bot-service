from flask import jsonify


class AuthService:

    def getName(self):
        tasks = [{'id': 1000, 'name': "Breakfastsss"}, {'id': 1001, 'name': "Lunch"}]

        return jsonify({'tasks': tasks})
