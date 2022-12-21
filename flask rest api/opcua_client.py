from opcua import Client, ua
from finished_Data import finished
from variables.all import ALL
import time

protcol = "opc.tcp"
ip = "127.0.0.1"
port = "4840"

client = Client(protcol + "://" + ip + ":" + port)
connected = False
sub = None
handle = None
handler = None

class subHandler(object):

    def datachange_notification(self, node, val, data):
        if val == 17:
            handleFinish()
        elif val == 6:
            brewStats()

def connect():
    global connected
    global handler
    print("trying to connect")
    try:
        client.connect()
        connected = True
        handler = subHandler()
        subBrew()
        print("connected")
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

def write_node(nodeID, value):
    node = read_node(nodeID)
    value = convertVal(nodeID, value)

    dv = ua.DataValue(ua.Variant(value, node.get_data_type_as_variant_type()))
    dv.ServerTimestamp = None
    dv.SourceTimestamp = None
    node.set_value(dv)

def convertVal(nodeID, value):
    node = read_node(nodeID)
    nodeVariant = node.get_data_type_as_variant_type()
    if isinstance(nodeVariant, ua.VariantType):
        if nodeVariant.name == 'Int32':
            value = int(value)
        elif nodeVariant.name == 'Boolean':
            value = bool(value)
        elif nodeVariant.name == 'Float':
            value = float(value)
        return value

def changeCon(var):
    global connected
    if var:
        connected = True
    elif not var:
        connected = False

def subBrew():
    global sub
    global handle
    sub = client.create_subscription(500, handler)
    node_id = ALL.get('current_state')
    node = read_node(node_id)
    handle = sub.subscribe_data_change(node)

start_time = 0
stop_time = 0
def reset():
    global start_time
    global stop_time
    start_time = 0
    stop_time = 0

def brewStats():
    reset()
    global start_time
    start_time = time.perf_counter()
    print("starting brew")

def handleFinish():
    global stop_time
    global start_time
    stop_time = time.perf_counter()
    timeSpent = stop_time-start_time
    finished(timeSpent)
    #do shit with code