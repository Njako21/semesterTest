def make_variable_dict():
    set_command = "ns=6;s=::Program:Cube.Command.CntrlCmd"
    set_speed = "ns=6;s=::Program:Cube.Command.MachSpeed"  # set eppsed
    exec_command = "ns=6;s=::Program:Cube.Command.CmdChangeRequest"  # true / false
    set_batch_id = "ns=6;s=::Program:Cube.Command.Parameter[0].Value"  # id 0 ≤ value ≤ 65535
    set_recipe = "ns=6;s=::Program:Cube.Command.Parameter[1].Value"  # type of beer 0 ≤ value ≤ 5
    set_quantity = "ns=6;s=::Program:Cube.Command.Parameter[2].Value"  # quantity 0 ≤ value ≤ 65535

    # use the locals() function to access the local variables in the current scope
    local_vars = locals()

    # create a dictionary that maps the names of the local variables to their values
    variable_dict = {
        name: local_vars[name] for name in local_vars
        if not name.startswith("_")
    }

    # return the dictionary of local variables
    return variable_dict

BREW = make_variable_dict()

machine_speed = {
    0: 600,
    1: 300,
    2: 150,
    3: 200,
    4: 100,
    5: 125,
}

control_cmd = {
    1: "Reset",
    2: "start",
    3: "Stop",
    4: "abort",
    5: "clear",
}

product_id = {
    0: "Pilsner",
    1: "Wheat",
    2: "IPA",
    3: "Stout",
    4: "Ale",
    5: "Alcohol Free",

}