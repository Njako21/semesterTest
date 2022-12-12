<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\api;
use App\Http\Controllers\viewRouting;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', [viewRouting::class, 'index'])->name("home");
Route::get('/brew', [viewRouting::class, 'brew'])->name("brew");
Route::get('/admin', [viewRouting::class, 'admin'])->name("admin");


Route::get('/api/getInventory', [api::class, 'getInventory'])->name("inventory");
