<?php

namespace Tests\Unit;

use Tests\TestCase;
use App\Models\Post;
use App\Models\User;
use App\Repositories\PostRepository;
use Illuminate\Foundation\Testing\RefreshDatabase;

class PostRepositoryTest extends TestCase
{
    use RefreshDatabase;

    protected $postRepository;

    public function setUp(): void
    {
        parent::setUp();
        $this->postRepository = new PostRepository();
    }

    // public function test_all()
    // {
    //     Post::factory()->count(3)->create();

    //     $result = $this->postRepository->all();

    //     $this->assertCount(3, $result);
    // }

    public function test_find()
    {
        $post = Post::factory()->create();

        $result = $this->postRepository->find($post->id);

        $this->assertEquals($post->id, $result->id);
    }

    public function test_create()
    {
        $user = User::factory()->create();
        $data = [
            'title' => 'Test Post',
            'content' => 'This is a test post.',
            'user_id' => $user->id,
        ];

        $result = $this->postRepository->create($data);

        $this->assertDatabaseHas('posts', $data);
        $this->assertEquals($data['title'], $result->title);
    }

    public function test_update()
    {
        $post = Post::factory()->create();
        $data = [
            'title' => 'Updated Title',
            'content' => 'Updated content.',
        ];

        $result = $this->postRepository->update($post->id, $data);

        $this->assertDatabaseHas('posts', $data);
        $this->assertEquals($data['title'], $result->title);
    }

    public function test_delete()
    {
        $post = Post::factory()->create();

        $this->postRepository->delete($post->id);

        $this->assertDatabaseMissing('posts', ['id' => $post->id]);
    }
}
