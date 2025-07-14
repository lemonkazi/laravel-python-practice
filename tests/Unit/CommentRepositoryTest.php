<?php

namespace Tests\Unit;

use Tests\TestCase;
use App\Models\Comment;
use App\Models\Post;
use App\Models\User;
use App\Repositories\CommentRepository;
use Illuminate\Foundation\Testing\RefreshDatabase;

class CommentRepositoryTest extends TestCase
{
    use RefreshDatabase;

    protected $commentRepository;

    public function setUp(): void
    {
        parent::setUp();
        $this->commentRepository = new CommentRepository();
    }

    public function test_create()
    {
        $user = User::factory()->create();
        $post = Post::factory()->create();
        $data = [
            'comment_body' => 'This is a test comment.',
            'user_id' => $user->id,
            'post_id' => $post->id,
        ];

        $result = $this->commentRepository->create($data);

        $this->assertDatabaseHas('comments', $data);
        $this->assertEquals($data['comment_body'], $result->comment_body);
    }
}
