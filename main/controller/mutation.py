from ariadne import ObjectType

from main.service import Resolver
from main.service.accountmanager import AccountManager

mutation = ObjectType("Mutation")


@mutation.field("create_tables")
def create_tables(_, info) -> object:
    """

    Args:
        _:
        info:
    """

    return Resolver().create_database_tables()


@mutation.field("account_manager")
def account_manager(_, info, params: dict, account_method: str) -> object:
    """

    Args:
        account_method: the main endpoint to be called values includes [CREATE, LOGIN, UPDATE, RESET, WITHDRAW, PAY, ADD_USER]
        _: - builtin parameter
        info: builtin parameter
        params: Oject of user data

    Returns:

    """
    return AccountManager(method="Mutation").create_account(
        params=params, account_method=account_method
    )
