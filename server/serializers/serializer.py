from abc import abstractmethod

class Serializer:
    format = None

    @abstractmethod
    def serialize(self, data):
        return None

    @abstractmethod
    def deserialize(self, data):
        return None
    