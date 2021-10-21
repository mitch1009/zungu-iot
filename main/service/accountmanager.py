import json
from pprint import pprint

from pymysql import IntegrityError

from main.model import User, db
from main.service import BaseService


# ::::::::::::::::::::::::::::::::: ACCOUNT MANAGER CLASS :::::::::::::::::::::::::::::::::::
class AccountManager(BaseService):
    """ """

    def __init__(self, method: str):
        super().__init__()

    """
     Manage account creation, deletions and transactions on user accounts.

    """

    def create_account(self, params: dict, account_method: str) -> dict:
        """

        Args: params: a dictionary of values required for account creation. the base data required on initial
        registration as email, phone, and full name.

        {
            - email: String required
            - phone: String Required
            - full_name: String required
            - option: enum value - [START, UPDATE, 2FA, FINISH]
        }

        """
        option = params["option"]
        pprint(account_method)
        if option == "START":
            # add account creation functionality here
            try:
                user_data = self.user(
                    name=params["name"], email=params["email"], phone=params["phone"]
                )
                self.database.session.add(user_data)
                self.database.session.commit()
                payload = {
                    "message": f"User added to database {user_data}",
                    "data": json.dumps(user_data),
                }
            except IntegrityError as e:
                payload = {'error': [e], 'status': False, 'message': e}
        elif option == "UPATE":
            payload = {}
        elif option == "2FA":
            payload = {}
        elif option == "FINISH":
            payload = {}
        else:
            payload = {
                "message": "Unknown request please try again",
                "status": False,
                "data": "",
            }

        return payload

    def register_child_user(self, params: dict) -> dict:
        pass
    def register_a_sibling(self, params)-> dict:
        pass


