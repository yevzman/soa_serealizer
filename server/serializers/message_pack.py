import msgpack

from .serializer import Serializer
from overrides import override

class MessagePackSerializer(Serializer):
    format = 'MESSAGE_PACK'

    @override
    def serialize(self, data):
        return msgpack.packb(data)

    @override
    def deserialize(self, data):
        return msgpack.unpackb(data)
