from flask import jsonify
import logging as logger
logger.basicConfig(level="DEBUG")


class AuthService:

    def validateUser(self, request):
        validationResult = {}
        logger.log(1, "Validating user", "", "")

        if request.json['uid'] == "admin" and request.json['pwd'] == "pass@123":
            logger.log(1, "User validation successful", "", "")
            validationResult["status"] = True
            userinfo = {"fname": "Nevile", "surname": "Parekh"}
            validationResult["userinfo"] = userinfo

        else:
            logger.log(1, "User validation un-successful", "", "")
            validationResult["status"] = False

        return  jsonify({'auth': validationResult})
