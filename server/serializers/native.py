import pickle
from .serializer import Serializer
from overrides import override


class NativeSerializer(Serializer):
    format = 'NATIVE'

    @override
    def serialize(self, data):
        return pickle.dumps(data)

    @override
    def deserialize(self, data):
        return pickle.loads(data)