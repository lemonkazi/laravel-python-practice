<?php

namespace Database\Seeders;

use App\Models\User;
// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        // User::factory(10)->create();

        User::factory()->create([
            'name' => 'Test User',
            'email' => 'test@example.com',
        ]);
        // Post and comment create 10
        \App\Models\Post::factory(10)->create()->each(function ($post) {
            $post->comments()->saveMany(\App\Models\Comment::factory(3)->make());
        });

    }
}
