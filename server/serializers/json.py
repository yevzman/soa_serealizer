import json
from overrides import override
from .serializer import Serializer


class JsonSerializer(Serializer):
    format = 'JSON'

    @override
    def serialize(self, data):
        return json.dumps(data)
    
    @override
    def deserialize(self, data):
        return json.loads(data)