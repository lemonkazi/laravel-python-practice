<?php

namespace App\Http\Controllers;

use App\Repositories\PostRepositoryInterface;
use Illuminate\Http\Request;

use App\Models\Post;
use App\Models\Comment;

use App\Events\PostCreated;

class PostController extends Controller
{
    protected $postRepository;

    public function __construct(PostRepositoryInterface $postRepository)
    {
        $this->postRepository = $postRepository;
    }
    /**
     * Approve a comment.
     */
    public function approveComment(Request $request, Comment $comment)
    {
        $this->commentRepository->approve($comment->id);
        return redirect()->back()->with('success', 'Comment approved successfully.');
    }
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $posts = $this->postRepository->paginate(10);
        return view('posts.index', compact('posts'));
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return view('posts.create');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'required|string',
            'is_published' => 'boolean',
        ]);

        $post = $this->postRepository->create([
            'title' => $request->title,
            'content' => $request->content,
            'is_published' => $request->has('is_published'),
            'user_id' => auth()->id(),
        ]);

        //PostCreated::dispatch($post);
        event(new PostCreated($post));

        return redirect()->route('posts.index')->with('success', 'Post created successfully.');
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Post $post)
    {
        return view('posts.edit', compact('post'));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Post $post)
    {
        $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'required|string',
            'is_published' => 'boolean',
        ]);

        $this->postRepository->update($post->id, [
            'title' => $request->title,
            'content' => $request->content,
            'is_published' => $request->has('is_published'),
        ]);

        return redirect()->route('posts.index')->with('success', 'Post updated successfully.');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Post $post)
    {
        $this->postRepository->delete($post->id);

        return redirect()->route('posts.index')->with('success', 'Post deleted successfully.');
    }
}
