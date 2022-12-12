def make_variable_dict():
    hops = "ns=6;s=::Program:Inventory.Hops"
    malt = "ns=6;s=::Program:Inventory.Malt"
    wheat = "ns=6;s=::Program:Inventory.Wheat"
    yeast = "ns=6;s=::Program:Inventory.Yeast"
    barley = "ns=6;s=::Program:Inventory.Barley"
    fullInv = "ns=6;s=::Program:FillingInventory"

    # use the locals() function to access the local variables in the current scope
    local_vars = locals()

    # create a dictionary that maps the names of the local variables to their values
    variable_dict = {
        name: local_vars[name] for name in local_vars
        if not name.startswith("_")
    }

    # return the dictionary of local variables
    return variable_dict

INGREDIENTS = make_variable_dict()