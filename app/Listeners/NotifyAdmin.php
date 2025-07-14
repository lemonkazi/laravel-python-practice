<?php

namespace App\Listeners;

use App\Events\PostCreated;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Support\Facades\Log;
use App\Mail\UserMail;
use Illuminate\Support\Facades\Mail;

class NotifyAdmin implements ShouldQueue
{
    /**
     * Create the event listener.
     */
    public function __construct()
    {
        //
    }

    /**
     * Handle the event.
     */
    public function handle(PostCreated $event): void
    {
        //echo '<pre>';print_r($event);exit;
        Mail::to('lemonpstu09@gmail.com')->send(new \App\Mail\UserMail($event->post));
    }
}
