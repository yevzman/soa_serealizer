import yaml
from overrides import override
from .serializer import Serializer


class YamlSerializer(Serializer):
    format = 'YAML'

    @override
    def serialize(self, data):
        return yaml.dump(data)
    
    @override
    def deserialize(self, data):
        return yaml.load(data, Loader=yaml.Loader)
