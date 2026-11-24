from utilities.jsonUtilities import JsonUtilities

class LoginDataUtilities:

    @staticmethod
    def get_user(username=None):
        users = []
        data = JsonUtilities.read_json("login_data.json")
        for user in data["login_users"]:
            if username is None or user["username"] == username:
                users.append((user["username"], user["password"]))
        return users