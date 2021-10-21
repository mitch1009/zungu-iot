"""  
Services
"""
import os

from main.model import db, User, Package, Course


class Resolver:
    """
    Endpoint Resolver
    """

    def __init__(self):
        self.manager = ""
        self.db = db

    def create_database_tables(self) -> object:
        """

        Returns: object

        """
        self.db.create_all()
        self.db.session.commit()

        return {"message": "Tables initialized", "status": True}


class BaseService:
    """
    Service configurations. all data and all main configurations will be kept here.
    """

    def __init__(self):
        # :::::::::::::: MAIL CONFIG PARAMETERS :::::::::::::
        self.mail_user = os.environ["MAIL_USER"]
        self.mail_password = os.environ["MAIL_PASSWORD"]
        self.mail_server = os.environ["MAIL_SERVER"]
        self.mail_sender = os.environ["MAIL_USER"]

        # ::::::::::::::::::  END  :::::::::::::::::::::::::::

        # :::::::::::::::::: DATABASE CONFIG ::::::::::::::::::::::::
        self.database = db
        """User Table"""
        self.user = User
        """Package Table"""
        self.package = Package
        """Course Table"""
        self.courses = Course

    def sys_send_mail(self, message: str, mail_type: str, to: str) -> object:
        """

        Args:
            message: message to be sent to the user
            mail_type:  String value - possible values [CREATE, UPDATE, _2FA, DELETE, DEACTIVATE]
            to:
        """
        pass
