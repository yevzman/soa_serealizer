import fastavro
from io import BytesIO
from avro.schema import parse
from .serializer import Serializer
from overrides import override

avro_schema = {
  "type": "record",
  "name": "baggage",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "airports", "type": {"type": "array", "items": "string"}},
    {"name": "parametrs", "type": {"type": "map", "values": "int"}},
    {"name": "items", "type": "int"},
    {"name": "weight", "type": "float"}
  ]
}


class AvroSerializer(Serializer):
    format = 'AVRO'

    @override
    def serialize(self, data):
        writer = BytesIO()
        fastavro.schemaless_writer(writer, avro_schema, data)
        return writer.getvalue()

    @override
    def deserialize(self, data):
        writer = BytesIO()
        writer.write(data)
        writer.seek(0)
        return fastavro.schemaless_reader(writer, avro_schema)