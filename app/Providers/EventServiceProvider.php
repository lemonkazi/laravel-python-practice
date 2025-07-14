<?php

namespace App\Providers;

use App\Contracts\Events\EventInterface;
use App\Contracts\Listeners\ListenerInterface;
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

    public function register()
    {
        $this->app->bind(
            EventInterface::class,
            PostCreated::class
        );

        $this->app->bind(
            ListenerInterface::class,
            NotifyAdmin::class
        );
    }

    /**
     * Determine if events and listeners should be automatically discovered.
     */
    public function shouldDiscoverEvents(): bool
    {
        return false;
    }
}
