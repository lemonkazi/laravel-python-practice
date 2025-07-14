<?php

use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;
use App\Models\Post;

Route::get('/', function () {
    Post::whereId(2)->delete();
    echo '<pre>';print_r(['sss']);exit;
    //return view('welcome');

});

Route::get('/dashboard', [App\Http\Controllers\PostController::class, 'index'])->middleware(['auth', 'verified'])->name('dashboard');

Route::resource('posts', App\Http\Controllers\PostController::class)->middleware(['auth', 'verified']);

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});

require __DIR__.'/auth.php';
