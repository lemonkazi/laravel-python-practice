<?php

namespace App\Contracts\Listeners;

use App\Contracts\Events\EventInterface;

interface ListenerInterface
{
    public function handle(EventInterface $event): void;
}