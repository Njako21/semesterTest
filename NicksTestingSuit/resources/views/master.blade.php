<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="{{asset('css/main.css')}}">
        <link rel="stylesheet" href="{{asset('css/fonts.css')}}">
        <script src="{{asset('js/functions.js')}}"></script>
        <script src="{{asset('js/post.js')}}"></script>
        @yield('styling')
    </head>
    <body>
        <nav>
            <p>User: Name</p>
            <div>
                <h1>BEER MACHINE</h1>
            </div>
            <ul>
                <li><a href="{{route('home')}}" id="dashboard">Dashboard</a></li>
                <li><a href="{{route('brew')}}" id="brew">Brew</a></li>
                <li><a href="{{route('admin')}}" id="admin">Admin</a></li>
                <li><a href="{{route('batches')}}" id="batches">Batches</a></li>
            </ul>
        </nav>
        <div id="content">
            @yield("body")
        </div>
        <div style="display:flex; justify-content: center; column-gap: 1vw; padding: 1vh">
            <button onclick="setCommnad(1)">Reset</button>
            <button onclick="setCommnad(2)">Start</button>
            <button onclick="setCommnad(3)">Stop</button>
            <button onclick="setCommnad(4)">abort</button>
            <button onclick="setCommnad(5)">clear</button>
        </div>
        <footer style="display:flex; column-gap: 1vw; justify-content: center; position: fixed; bottom: 1vh; width: 100vw;">
            <p>Server Status: </p>
            <p id="current_state">....</p>
        </footer>
    </body>
    <script>


        function setCommnad(var1){
            fetch('http://localhost:5000/api/write/set_command', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    value: var1,
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

        let x = 1000
        getData("current_state")
        setInterval(getData("current_state"), x)
        document.getElementById("{{$selected}}").classList.add("selected");
    </script>
    @yield('script')
</html>
