from opcua import Client

protcol = "opc.tcp"
ip = "127.0.0.1"
port = "4840"

client = Client(protcol+"://"+ip+":"+port)

def connect():
    client.connect()

def disconnect():
    client.disconnect()

def changeIp(ip, port):
    client = Client("opc.tcp://"+ip+":"+port)

def read_node(node_id):
    return client.get_node(node_id)

def read_node_val(node_id):
    return float(read_node(node_id).get_value())