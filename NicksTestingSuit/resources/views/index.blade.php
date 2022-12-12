@extends('master')
@section("styling")
    <link rel="stylesheet" href="{{asset('css/dash.css')}}">
@endsection

@section("body")
    <h1>Dashboard</h1>
    <div id="connection">
        <p>Bakend status:</p>
        <p id="connectionStatus"></p>
        <button onclick="con(true)">Connect</button>
        <button onclick="con(false)">Disconnect</button>
    </div>
    <p>Server Status: </p>
    <div class="container">
        <div class="progress">
            <p id="barley-text">I</p>
            <p id="barley-full">1%</p>
            <progress min="0" value="75" max="35000" id="barley"></progress>
        </div>

        <div class="progress">
            <p id="hops-text">II</p>
            <p id="hops-full">1%</p>
            <progress min="0" value="75" max="35000" id="hops"></progress>
        </div>

        <div class="progress">
            <p id="malt-text">III</p>
            <p id="malt-full">1%</p>
            <progress min="0" value="75" max="35000" id="malt"></progress>
        </div>

        <div class="progress">
            <p id="wheat-text">IV</p>
            <p id="wheat-full">1%</p>
            <progress min="0" value="75" max="35000" id="wheat"></progress>
        </div>

        <div class="progress">
            <p id="yeast-text">V</p>
            <p id="yeast-full">1%</p>
            <progress min="0" value="75" max="35000" id="yeast"></progress>
        </div>
    </div>
    <div>
        <progress min="0" value="75" max="35000" id="Maintenance"></progress>
    </div>
@endsection
@section("script")
    <script>


        let connect = false
        let x = 1000;

        function con(x){
            if(x){
                document.getElementById("connectionStatus").innerText = "Connecting"
                document.getElementById("connectionStatus").style.color = "green"
                connect = true;
            }else if(!x){
                document.getElementById("connectionStatus").innerText = "Disconnected"
                document.getElementById("connectionStatus").style.color = "red"
                connect = false;
            }
        }

        con(false)

        setInterval(getData, x)
        async function getData(){
            if(!connect){
                return
            }

            fetch("{{route("inventory")}}", {
                method: "GET"
            })
                .then(response => {
                    return response.json();
                })
                .then(json => {
                    if(document.getElementById("connectionStatus").innerText === "Connecting"){
                        document.getElementById("connectionStatus").innerText = "Connected"
                    }
                    console.table(json)
                    for (const [key, value] of Object.entries(json)) {
                        const progress = document.getElementById(key);
                        const text = document.getElementById(key+"-text");
                        const full = document.getElementById(key+"-full");
                        if(progress !== null){
                            progress.value = value
                            text.innerText = key
                            full.innerText = ((value/35000)*100)+"%"
                        }
                    }
                }).catch(error =>{
                    con(false)
                    document.getElementById("connectionStatus").innerText += ": Server Connection Refused"
            });
        }
    </script>
@endsection
