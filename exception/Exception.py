class NoLocationError(Exception):
    def __init__(self):
        self.messages = "Didn't receive location!"

    def __str__(self):
        return repr(self.messages)


class NoTaskTokenError(Exception):
    def __init__(self):
        self.messages = "Can't find taskToken"

    def __str__(self):
        return repr(self.messages)
