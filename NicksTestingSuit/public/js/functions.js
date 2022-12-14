async function getData(var1){

    fetch("/api/read/"+var1, {
        method: "GET"
    })
        .then(async response => {
            return response.json();
        })
        .then(json => {
            for (const [key, value] of Object.entries(json)) {

                let progress = document.getElementById(key);
                const text = document.getElementById(key+"-text");
                const full = document.getElementById(key+"-full");
                if(progress !== null){
                    if(key != "current_state"){
                        progress.value = value
                        text.innerText = key
                        full.innerText = ((value/35000)*100).toFixed(2)+"%"
                    }else {
                        progress.innerText = serverStatus[value]
                    }
                }
            }
        }).catch(error =>{
        console.log(error)
    });
}

const serverStatus = {
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
