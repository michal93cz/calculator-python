from abc import abstractmethod


class Operation:
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_request(self, text):
        pass
