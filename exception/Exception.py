class NoLocationError(Exception):
    def __init__(self):
        self.messages = "Didn't receive location!"

    def __str__(self):
        return repr(self.messages)
