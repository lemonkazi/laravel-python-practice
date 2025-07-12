#!/bin/sh

# Run artisan commands once the container is up and DB is reachable
php artisan config:clear
php artisan route:clear
php artisan cache:clear

# Start PHP-FPM
exec php-fpm
