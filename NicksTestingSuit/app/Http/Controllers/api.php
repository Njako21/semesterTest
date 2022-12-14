<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class api extends Controller
{
    function get($id){
        $url = "http://localhost:5000/api/read/" . $id;
        return file_get_contents($url);
    }

    function post(Request $request){
        $data = $request->json();
    }
}
