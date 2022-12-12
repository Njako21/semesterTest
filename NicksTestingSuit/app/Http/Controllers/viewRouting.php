<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class viewRouting extends Controller
{
    function index(){
        return view("index")->with('selected', 'dashboard');
    }

    function brew(){
        return view("brew")->with('selected', 'brew');
    }

    function admin(){
        return view("admin")->with('selected', 'admin');
    }
}
