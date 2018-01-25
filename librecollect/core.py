class SocialNetworkUser:

    def __init__(self, username, **data):
        self.username = username
        self.data = data

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.username == other.username
        return False

    def __hash__(self):
        return hash(self.username)


class SocialNetworkPost:

    def __init__(self, main_text, **data):
        self.main_text = main_text
        self.data = data


class EventHandler:
    pass


class CollectorRule:
    """Return a set of"""
    pass
