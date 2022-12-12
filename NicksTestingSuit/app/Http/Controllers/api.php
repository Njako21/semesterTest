<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class api extends Controller
{
    function getInventory(){
        $api_url = 'http://localhost:5000/api/inventory/all';
        return file_get_contents($api_url);
    }
}
