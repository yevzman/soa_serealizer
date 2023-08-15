from serializers import xml, json, yaml, native
import socket
import threading
import sys, timeit, os
from test import data

mapping = {
    'xml': xml.XmlSerializer(),
    'json': json.JsonSerializer(),
    'yaml': yaml.YamlSerializer(),
    'native': native.NativeSerializer()
}

def make_observation(data, serializer):
    serialize_time = timeit.timeit(lambda: serializer.serialize(data), number=100)
    serialized_data = serializer.serialize(data)
    deserialize_time = timeit.timeit(lambda: serializer.deserialize(serialized_data), number=100)

    ans = f'{serializer.format} - {len(serialized_data)}  - {serialize_time*1000}ms - {deserialize_time*1000}ms'
    print(f'Answer: {ans}')
    return ans


# host port format
if __name__ == '__main__':
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    format = os.getenv('FORMAT')
    if not host or not port or not format:
        print('bad args')
        exit(0)
    if format not in mapping:
        print('bad format')
        exit(1)
    serializer = mapping[format]
    print(f'serializer for {serializer.format}')
    server_address = (host, int(port))
    print(server_address)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)
    print('server configure on', server_address[0], server_address[1])
    while True:
        _, addr = server_socket.recvfrom(8192*7)
        print('get info from addr:', addr)
        print('ser data:', data)
        ans = make_observation(data, serializer)
        server_socket.sendto(ans.encode(), addr)
