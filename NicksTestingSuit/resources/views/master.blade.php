<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="{{asset('css/main.css')}}">
        <link rel="stylesheet" href="{{asset('css/fonts.css')}}">
        @yield('styling')
    </head>
    <body>
        <nav>
            <div>
                <h1>Nicks Testing Suit</h1>
            </div>
            <ul>
                <li><a href="{{route('home')}}" id="dashboard">Dashboard</a></li>
                <li><a href="{{route('brew')}}" id="brew">Brew</a></li>
                <li><a href="{{route('admin')}}" id="admin">Admin</a></li>
                <li><a href="{{route('admin')}}" id="admin">Batches</a></li>
            </ul>
        </nav>
        <div id="content">
            @yield("body")
        </div>
    </body>
    <script>
        document.getElementById("{{$selected}}").classList.add("selected");
    </script>
    @yield('script')
</html>
