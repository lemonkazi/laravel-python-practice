<?php

namespace App\Repositories;

use App\Models\Post;

class PostRepository implements PostRepositoryInterface
{
    public function all()
    {
        return Post::all();
    }

    public function find($id)
    {
        return Post::find($id);
    }

    public function create(array $data)
    {
        return Post::create($data);
    }

    public function update($id, array $data)
    {
        $post = Post::find($id);
        $post->update($data);
        return $post;
    }

    public function delete($id)
    {
        $post = Post::find($id);
        return $post->delete();
    }
}
