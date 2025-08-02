<?php

namespace App\Repositories;

use App\Models\Comment;

class CommentRepository implements CommentRepositoryInterface
{
    public function create(array $data)
    {
        return Comment::create($data);
    }
    public function approve($id)
    {
        $comment = Comment::find($id);
        if ($comment) {
            $comment->is_approved = true;
            $comment->approved_at = now();
            $comment->save();
        }
    }
}
