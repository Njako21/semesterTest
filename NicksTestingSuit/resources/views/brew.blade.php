@extends('master')
@section("body")
    <h1>Brew</h1>
    <div>
        <input type="number" value="1" id="quantity">
        <p id="speed-display">Current speed: 50</p>
        <input type="range" id="speed" min="1" max="600" value="50" oninput="updateSpeed()">
        <p id="timerTakes">Est time: </p>
    </div>
    <script>
        fetch('http://localhost:5000/api/brew/set_command/write', {
            method: 'POST',
            body: JSON.stringify({
                set_command: 300
            }),
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Alslow-Origin': '*'
            }
        })
            .then(response => response.json())
            .then(data => console.log(data));
    </script>
    <script>
        function updateSpeed() {
            var speed = document.getElementById('speed').value;
            document.getElementById('speed-display').innerHTML = 'Current speed: ' + speed;
            estTime()
        }

        function estTime(){
            var quantity = document.getElementById("quantity").value
            var speed = document.getElementById('speed').value

            seconds = (quantity/speed)*60
            var minutes = Math.floor(seconds / 60);
            var hours = Math.floor(minutes / 60);

            // Calculate the remaining seconds
            var remainingSeconds = Math.floor(seconds % 60);
            minutes %= 60

            document.getElementById("timerTakes").innerText = "Est time: H:"+hours+" M:"+minutes+" S:"+remainingSeconds
        }
    </script>
@endsection
