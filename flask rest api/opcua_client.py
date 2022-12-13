from opcua import Client

protcol = "opc.tcp"
ip = "127.0.0.1"
port = "4840"

client = Client(protcol + "://" + ip + ":" + port)
connected = False


def connect():
    global connected
    print("trying to connect")
    try:
        client.connect()
        connected = True
    except:
        print("could not connect to opc ua server")


def disconnect():
    if is_connected():
        client.disconnect()
        changeCon(False)


def read_node(node_id):
    if is_connected():
        return client.get_node(node_id)


def is_connected():
    global client
    if connected:
        return True
    else:
        return False


def read_node_val(node_id):
    if is_connected():
        return float(read_node(node_id).get_value())


def write_node():
    if is_connected():
        client.get_node("ns=6;s=::Program:Cube.Command.MachSpeed").set_value(200)


def changeCon(var):
    global connected
    if var:
        connected = True
    elif not var:
        connected = False
