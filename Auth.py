import json

class Auth:

    @staticmethod
    def check_auth(auth_json):
        auth = json.loads(auth_json)

        assert (("username" in auth) or ("password" in auth)), "auth_json does not contain required keys" #make sure json file has the data we want
        username = auth["username"]
        password = auth["password"]




