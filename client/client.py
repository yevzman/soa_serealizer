import sys
import socket

client_address = ("0.0.0.0", 2000)
server_addresses_mappings = {
    'native':           ("soa_serealizer-native-1", 5000),
    'json':             ("soa_serealizer-json-1", 5001),
    'yaml':             ("soa_serealizer-yaml-1", 5002),
    'xml':              ("soa_serealizer-xml-1", 5003),
    'message_pack':     ("soa_serealizer-message_pack-1", 5004),
    'avro':             ("soa_serealizer-avro-1", 5005)
}
formats = ['native', 'json', 'yaml', 'xml', 'message_pack', 'avro']

if __name__ == '__main__':    
    print('client start')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(client_address)
    print('start client on', client_address)
    while True:
        data, addr = client_socket.recvfrom(8192*7)
        data = data.decode().strip().split(' ')
        print('get connection from addr', addr, 'with data', data)
        if data[0] != '/get_result' or data[-1] not in formats:
            print('bad arguments')
            continue
        format = data[-1].strip()
        server_address =  server_addresses_mappings[format]
        print('send to', server_address)
        client_socket.sendto('data'.encode(), server_address)
        response, server_address = client_socket.recvfrom(1024)
        res_time = response.decode("utf-8")
        print(res_time)
        client_socket.sendto(res_time.encode(), addr)