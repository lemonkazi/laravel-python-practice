<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Str;

class Post extends Model
{
    /** @use HasFactory<\\Database\\Factories\\PostFactory> */
    use HasFactory;
    protected $fillable = [
        'title',
        'content',
        'slug',
        'user_id',
        'is_published',
        'published_at',
    ];



    public function user()
    {
        return $this->belongsTo(User::class);
    }
    public function comments()
    {
        return $this->hasMany(Comment::class);
    }
    public function scopePublished($query)
    {
        return $query->where('is_published', true)
                     ->whereNotNull('published_at')
                     ->where('published_at', '<=', now());
    }
    public function scopeDraft($query)
    {
        return $query->where('is_published', false)
                     ->orWhereNull('published_at');
    }
    public function scopeWithSlug($query, $slug)
    {
        return $query->where('slug', $slug);
    }
    public function scopeByUser($query, $userId)
    {
        return $query->where('user_id', $userId);
    }
    public function scopeRecent($query, $limit = 10)
    {
        return $query->orderBy('created_at', 'desc')->take($limit);
    }
    public function scopeSearch($query, $searchTerm)
    {
        return $query->where('title', 'like', '%' . $searchTerm . '%')
                     ->orWhere('content', 'like', '%' . $searchTerm . '%');
    }
}
