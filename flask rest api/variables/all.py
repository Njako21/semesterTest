def make_variable_dict():
    #   machine data
    vibrations = "ns=6;s=::Program:Data.Value.Vibration"
    temperature = "ns=6;s=::Program:Data.Value.Temperature"
    current_state = "ns=6;s=::Program:Cube.Status.StateCurrent"

    #   maintenance
    maintenance = "ns=6;s=::Program:Maintenance.Counter"
    maintenance_status = "ns=6;s=::Program:Maintenance.State"
    maintenance_urgent = "ns=6;s=::Program:Maintenance.Trigger"

    hops = "ns=6;s=::Program:Inventory.Hops"
    malt = "ns=6;s=::Program:Inventory.Malt"
    wheat = "ns=6;s=::Program:Inventory.Wheat"
    yeast = "ns=6;s=::Program:Inventory.Yeast"
    barley = "ns=6;s=::Program:Inventory.Barley"
    fullInv = "ns=6;s=::Program:FillingInventory"

    batch_id = "ns=6;s=::Program:Cube.Status.Parameter[0].Value"
    batch_quantity = "ns=6;s=::Program:Cube.Status.Parameter[1].Value"
    batch_humidity = "ns=6;s=::Program:Cube.Status.Parameter[2].Value"
    production_speed = "ns=6;s=::Program:Cube.Status.MachSpeed"
    batch_temperature = "ns=6;s=::Program:Cube.Status.Parameter[3].Value"
    current_production_speed = "ns=6;s=::Program:Cube.Status.CurMachSpeed"

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

ALL = make_variable_dict()