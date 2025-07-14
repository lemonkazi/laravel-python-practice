<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use App\Events\PostCreated;
use App\Listeners\NotifyUser;
use App\Listeners\NotifyAdmin;
use App\Models\Post;

class EventServiceProvider extends ServiceProvider
{
    /**
     * The event to listener mappings for the application.
     *
     * @var array<class-string, array<int, class-string>>
     */
    protected $listen = [
        PostCreated::class => [
            //NotifyUser::class,
            NotifyAdmin::class,
        ],
    ];

    /**
     * Register any events for your application.
     */
    public function boot(): void
    {
        Post::observe(\App\Observers\PostObserver::class);
    }

    /**
     * Determine if events and listeners should be automatically discovered.
     */
    public function shouldDiscoverEvents(): bool
    {
        return false;
    }
}
