from opcua import Client, ua

protcol = "opc.tcp"
#ip = "192.168.0.122"
ip = "127.0.0.1"
port = "4840"

client = Client(protcol + "://" + ip + ":" + port)
connected = False


def connect():
    global connected
    print("trying to connect")
    try:
        print("connected")
        client.connect()
        changeCon(True)
    except:
        print("could not connect to opc ua server")


def disconnect():
    if is_connected():
        print("disconnected")
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


def write_node(nodeID, type, value):
    node = read_node(nodeID)

    if type == "int32":
        dv = ua.DataValue(ua.Variant(value, ua.VariantType.Int32))
    elif type == "float":
        dv = ua.DataValue(ua.Variant(value, ua.VariantType.Float))
    elif type == "bool":
        dv = ua.DataValue(ua.Variant(value, ua.VariantType.Boolean))
    elif type == "structure":
        dv = ua.DataValue(ua.Variant(value, ua.VariantType))

    dv.ServerTimestamp = None
    dv.SourceTimestamp = None
    node.set_value(dv)


def changeCon(var):
    global connected
    if var:
        connected = True
    elif not var:
        connected = False
