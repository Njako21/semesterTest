@extends('master')
@section("body")
    <h1>Admin</h1>
    <p>Recipe:</p>
    <p id="current_Recipe">1</p>

    <p>product produced:</p>
    <p id="product_produced">1</p>

    <p>product failed:</p>
    <p id="product_failed">1</p>
@endsection
@section("script")
    <script>
        async function f(){
            fetch('/api/read/product_produced:current_Recipe:product_failed', {
                method: 'GET'
            })
                .then(async response => await response.json())
                .then(data => {
                    for (const [key, value] of Object.entries(data)) {
                        document.getElementById(key).innerText = value
                    }
                });
        }

        setInterval(f, 1000);
    </script>
@endsection
