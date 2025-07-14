<?php

namespace App\Repositories;

use App\Models\Comment;

class CommentRepository implements CommentRepositoryInterface
{
    public function create(array $data)
    {
        return Comment::create($data);
    }
}
