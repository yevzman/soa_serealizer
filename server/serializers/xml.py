from xml_marshaller import xml_marshaller
from overrides import override
from .serializer import Serializer


class XmlSerializer(Serializer):
    format = 'XML'

    @override
    def serialize(self, data):
        return xml_marshaller.dumps(data)
    
    @override
    def deserialize(self, data):
        return xml_marshaller.loads(data)