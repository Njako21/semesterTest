def make_variable_dict():
    stop_reason = "ns=6;s=::Program:Cube.Admin.StopReason.ID"
    stop_reason2 = "ns=6;s=::Program:Cube.Admin.StopReason"
    current_Recipe = "ns=6;s=::Program:Cube.Admin.Parameter[0].Value"
    product_produced = "ns=6;s=::Program:Cube.Admin.ProdProcessedCount"
    product_failed = "ns=6;s=::Program:Cube.Admin.ProdDefectiveCount"


    # use the locals() function to access the local variables in the current scope
    local_vars = locals()

    # create a dictionary that maps the names of the local variables to their values
    variable_dict = {
        name: local_vars[name] for name in local_vars
        if not name.startswith("_")
    }

    # return the dictionary of local variables
    return variable_dict

ADMIN = make_variable_dict()

stop_reason = {
    10: 'Empty inventory',
    11: 'Maintenance',
    12: 'Manual stop',
    13: 'Motor power loss',
    14: 'Manual abort'
}