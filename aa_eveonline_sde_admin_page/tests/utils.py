"""
Helper for our tests
"""

# Standard Library
import datetime as dt
import re
import secrets

# Django
from django.utils.timezone import now

# Alliance Auth
from allianceauth.authentication.models import User
from allianceauth.tests.auth_utils import AuthUtils

MESSAGE_DATETIME_HOURS_INTO_PAST = 240
MESSAGE_DATETIME_MINUTES_OFFSET = 2
NEW_MESSAGE_DATETIME = now() - dt.timedelta(hours=MESSAGE_DATETIME_HOURS_INTO_PAST)


def create_fake_user(
    character_id: int,
    character_name: str,
    corporation_id: int = None,
    corporation_name: str = None,
    corporation_ticker: str = None,
    permissions: list[str] = None,
    **kwargs,
) -> User:
    """
    Create a fake user with a given character name and id.

    :param character_id:
    :type character_id:
    :param character_name:
    :type character_name:
    :param corporation_id:
    :type corporation_id:
    :param corporation_name:
    :type corporation_name:
    :param corporation_ticker:
    :type corporation_ticker:
    :param permissions:
    :type permissions:
    :param kwargs:
    :type kwargs:
    :return:
    :rtype:
    """

    username = re.sub(pattern=r"[^\w\d@\.\+-]", repl="_", string=character_name)
    user = AuthUtils.create_user(username=username)

    if not corporation_id:
        corporation_id = 2001
        corporation_name = "Wayne Technologies Inc."
        corporation_ticker = "WTE"

    alliance_id = kwargs.get("alliance_id", 3001)
    alliance_name = (
        kwargs.get("alliance_name", "Wayne Enterprises")
        if alliance_id is not None
        else ""
    )

    AuthUtils.add_main_character_2(
        user=user,
        name=character_name,
        character_id=character_id,
        corp_id=corporation_id,
        corp_name=corporation_name,
        corp_ticker=corporation_ticker,
        alliance_id=alliance_id,
        alliance_name=alliance_name,
    )

    if permissions:
        perm_objs = [AuthUtils.get_permission_by_name(perm) for perm in permissions]
        user = AuthUtils.add_permissions_to_user(perms=perm_objs, user=user)

    return user


def random_id(n: int = 26) -> int:
    """
    Generate a random ID

    :param n: Length of the ID, optional (default=26 (8 digits in base36))
    :type n: int
    :return: A random ID
    :rtype: int
    """

    return secrets.randbits(n)
