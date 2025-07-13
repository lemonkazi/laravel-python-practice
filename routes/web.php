<?php

use Illuminate\Support\Facades\Route;
use App\Models\Post;
use App\Models\User;

Route::get('/', function () {
    return view('welcome');
    //Post::whereId(1)->delete();
    // $arr = [1, 2, 3, 4];
    // foreach ($arr as &$value) {
    //     echo $value = $value * 2;
    //     echo '<br>';
    //     //$value *= 2;
    // }
    // foreach ($arr as $value) {}
    echo '<pre>';print_r(['ss']);exit;
});
