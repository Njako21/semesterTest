def make_variable_dict():
    #   machine data
    vibrations = "ns=6;s=::Program:Data.Value.Vibration"
    temperature = "ns=6;s=::Program:Data.Value.Temperature"
    current_state = "ns=6;s=::Program:Cube.Status.StateCurrent"

    #   maintenance
    maintenance = "ns=6;s=::Program:Maintenance.Counter"
    maintenance_status = "ns=6;s=::Program:Maintenance.State"
    maintenance_urgent = "ns=6;s=::Program:Maintenance.Trigger"


    # use the locals() function to access the local variables in the current scope
    local_vars = locals()

    # create a dictionary that maps the names of the local variables to their values
    variable_dict = {
        name: local_vars[name] for name in local_vars
        if not name.startswith("_")
    }

    # return the dictionary of local variables
    return variable_dict

MACHINE = make_variable_dict()

status = {
0   : 'Deactivated',
1   : 'Clearing',
2   : 'Stopped',
3   : 'Starting',
4   : 'Idle',
5   : 'Suspended',
6   : 'Execute',
7   : 'Stopping',
8   : 'Aborting',
9   : 'Aborted',
10  : 'Holding',
11  : 'Held',
15  : 'Resetting',
16  : 'Completing',
17  : 'Complete',
18  : 'Deactivating',
19  : 'Activating',
}