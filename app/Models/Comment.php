<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Comment extends Model
{
    /** @use HasFactory<\Database\Factories\CommentFactory> */
    use HasFactory;
    protected $fillable = [
        'comment_body',
        'post_id',
        'user_id',
        'is_approved',
        'approved_at',
    ];
    public function post()
    {
        return $this->belongsTo(Post::class);
    }
    public function user()
    {
        return $this->belongsTo(User::class);
    }
    public function approve(): void
    {
        $this->is_approved = true;
        $this->approved_at = now();
        $this->save();
    }

    public function scopeApproved($query)
    {
        return $query->where('is_approved', true)
                     ->whereNotNull('approved_at');
    }
}
