<?php

namespace App\Contracts\Events;

use App\Models\Post;

interface EventInterface
{
    public function getPost(): Post;
}