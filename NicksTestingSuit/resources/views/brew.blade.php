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
        <input type="number" id="quantity" placeholder="quantity" value="300" onkeyup="updateSpeed()">
        <p id="speed-display">Current speed:</p>
        <input type="number" id="speedC" value="50" onkeyup="changeSpeed()">
        <input type="range" id="speed" min="1" max="600" value="300" oninput="updateSpeed()">
        <div style="display: flex;">
            <input type="checkbox" id="checkbox" name="checkbox" on>
            <label for="checkbox">Run at optimal speed</label>
        </div>
        <p id="timerTakes">Est time: </p>
        <button onmouseup="prompt()">Start production</button>
    </div>
    </div>
@endsection
@section("script")
    <script>

        function write(variable, type){
            fetch('http://localhost:5000/api/write/'+type, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    value: variable,
                })
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error(error);
                });
        }


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

            answer = "Est time: H:"+hours+" M:"+minutes+" S:"+remainingSeconds

            document.getElementById("timerTakes").innerText = answer
            return answer
        }

        function prompt(){
            write(2, "set_batch_id")
            write(parseFloat(document.getElementById("beerType").value), "set_recipe")
            write(parseFloat(document.getElementById("quantity").value), "set_quantity")
            write(parseFloat(document.getElementById("speed").value), "set_speed")
            write(2, "set_command")
            write(true, "ExecuteCmd")
            estTimeVar = ""
            switch (document.getElementById("beerType").value) {
                case "0": //Pilsner
                    estTimeVar = trueCost(4,2,1,4,1)
                    break
                case '1': //Wheat
                    estTimeVar = trueCost(1,4,1,3,6)
                    break
                case '2': //IPA
                    estTimeVar = trueCost(4,1,5,1,4)
                    break
                case '3': //Stout
                    estTimeVar = trueCost(3,4,6,2,1)
                    break
                case '4': //Ale
                    estTimeVar = trueCost(4,6,2,8,2)
                    break
                case '5': //Alcohol Free
                    estTimeVar = trueCost(1,1,4,0,5)
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
            func("barley", ingredients)
            func("hops", ingredients)
            func("malt", ingredients)
            func("yeast", ingredients)
            func("wheat", ingredients)
        }

        function func(var1, ingredients){
            document.getElementById(var1).innerText = var1+": "+ ingredients.get(var1)
        }
    </script>
@endsection
