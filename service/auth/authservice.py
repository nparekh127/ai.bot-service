from flask import jsonify
import logging as logger
logger.basicConfig(level="DEBUG")


class AuthService:

    # Method to validate user
    def validateUser(self, request):
        logger.log(1, "Validating user", "", "")

        if request.json['uid'] == "admin" and request.json['pwd'] == "pass@123":
            logger.log(1, "User validation successful", "", "")

            return self.prepareSuccessResponse()

        else:
            logger.log(1, "User validation un-successful", "", "")

            return self.prepareDeclineResponse()

    # Method to generate token for given user
    def generateToken(self, request):

        return "This is dummy token"

    ################ Private methods ###########################
    def prepareSuccessResponse(self):
        validationResult = {}
        validationResult["status"] = True
        userinfo = {"fname": "Nevile", "surname": "Parekh"}
        validationResult["userinfo"] = userinfo

        return jsonify({'auth': validationResult})


    def prepareDeclineResponse(self):
        validationResult = {}
        validationResult["status"] = False

        return jsonify({'auth': validationResult})
