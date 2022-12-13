@extends('master')
@section("styling")
    <link rel="stylesheet" href="{{asset('css/brew.css')}}">
@endsection
@section("body")
    <div id="content">
    <h1>Brew</h1>
    <div style="row-gap: 1vh; display: grid;">
        <select onchange="beertype()" id="beerType">
            <option value="0">Pilsner</option>
            <option value="1">Wheat</option>
            <option value="2">IPA</option>
            <option value="3">Stout</option>
            <option value="4">Ale</option>
            <option value="5">Alcohol Free</option>
        </select>
        <input type="number" id="quantity" placeholder="quantity" onkeyup="updateSpeed()">
        <p id="speed-display">Current speed:</p>
        <input type="number" id="speedC" value="50" onkeyup="changeSpeed()">
        <input type="range" id="speed" min="1" max="600" value="300" oninput="updateSpeed()">
        <div style="display: flex;">
            <input type="checkbox" id="checkbox" name="checkbox" on>
            <label for="checkbox">Run at optimal speed</label>
        </div>
        <p id="timerTakes">Est time: </p>
        <button onmouseup="costCalc()">Start production</button>
    </div>
    </div>
    <script>
        fetch('http://localhost:5000/api/brew/write/brew', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "set_speed": 200,
            })
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)
            })
            .catch(error => {
                console.log(error)
            });
    </script>
@endsection
@section("script")
    <script>
        updateSpeed()

        function beertype(){
            switch (document.getElementById("beerType").value) {
                case "0": //Pilsner
                    speed(600)
                    break
                case '1': //Wheat
                    speed(300)
                    break
                case '2': //IPA
                    speed(150)
                    break
                case '3': //Stout
                    speed(200)
                    break
                case '4': //Ale
                    speed(100)
                    break
                case '5': //Alcohol Free
                    speed(125)
                    break
            }
        }

        function speed(maxSpeed){
            formerMax = document.getElementById("speed").max
            value = document.getElementById("speed").value
            document.getElementById("speed").max = maxSpeed
            if(value > maxSpeed){
                document.getElementById("speed").value = maxSpeed
            }
            updateSpeed()
        }

        function changeSpeed(){
            document.getElementById("speed").value = document.getElementById("speedC").value
            updateSpeed()
        }

        function updateSpeed() {
            var speed = document.getElementById('speed').value;
            document.getElementById('speedC').value = speed;
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

        function costCalc(){
            switch (document.getElementById("beerType").value) {
                case "0": //Pilsner
                    trueCost(4,2,1,4,1)
                    break
                case '1': //Wheat
                    trueCost(1,4,1,3,6)
                    break
                case '2': //IPA
                    trueCost(4,1,5,1,4)
                    break
                case '3': //Stout
                    trueCost(3,4,6,2,1)
                    break
                case '4': //Ale
                    trueCost(4,6,2,8,2)
                    break
                case '5': //Alcohol Free
                    trueCost(1,1,4,0,5)
                    break
            }
        }

        function trueCost(barley, hops, malt, yeast, wheat){
            quantity = document.getElementById("quantity").value

            const ingredients = new Map();

            ingredients.set('barley', quantity * barley);
            ingredients.set('hops', quantity * hops);
            ingredients.set('malt', quantity * malt);
            ingredients.set('yeast', quantity * yeast);
            ingredients.set('wheat', quantity * wheat);
            console.log(ingredients.get('barley'))
            console.log(ingredients.get('hops'))
            console.log(ingredients.get('malt'))
            console.log(ingredients.get('yeast'))
            console.log(ingredients.get('wheat'))
        }
    </script>
@endsection
