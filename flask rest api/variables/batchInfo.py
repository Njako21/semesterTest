def make_variable_dict():
    batch_id = "ns=6;s=::Program:Cube.Status.Parameter[0].Value"
    batch_quantity = "ns=6;s=::Program:Cube.Status.Parameter[1].Value"
    batch_humidity = "ns=6;s=::Program:Cube.Status.Parameter[2].Value"
    production_speed = "ns=6;s=::Program:Cube.Status.MachSpeed"
    batch_temperature = "ns=6;s=::Program:Cube.Status.Parameter[3].Value"
    current_production_speed = "ns=6;s=::Program:Cube.Status.CurMachSpeed"


    # use the locals() function to access the local variables in the current scope
    local_vars = locals()

    # create a dictionary that maps the names of the local variables to their values
    variable_dict = {
        name: local_vars[name] for name in local_vars
        if not name.startswith("_")
    }

    # return the dictionary of local variables
    return variable_dict

BATCH = make_variable_dict()