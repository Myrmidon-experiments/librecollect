import pytest
from librecollect.core import SocialNetworkUser


@pytest.fixture
def get_users():
    user_1 = SocialNetworkUser("Pepe")
    user_2 = SocialNetworkUser("Lalo")
    user_3 = SocialNetworkUser("Pepe")
    return [user_1, user_2, user_3]


def test_social_network_user_eq_operation(get_users):
    user_1, user_2, user_3 = get_users
    assert user_1 == user_3


def test_social_network_users_set_lenght(get_users):
    users_as_set = set(get_users)
    assert len(users_as_set) == 2
