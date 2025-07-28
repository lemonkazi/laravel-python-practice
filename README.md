<p align="center">
  <a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400" alt="Laravel Logo">
  </a>
</p>

<p align="center">
  <a href="https://github.com/laravel/framework/actions">
    <img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Build Status">
  </a>
  <a href="https://packagist.org/packages/laravel/framework">
    <img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads">
  </a>
  <a href="https://packagist.org/packages/laravel/framework">
    <img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version">
  </a>
  <a href="https://packagist.org/packages/laravel/framework">
    <img src="https://img.shields.io/packagist/l/laravel/framework" alt="License">
  </a>
</p>

# Laravel 12 with - Docker Setup

This guide walks you through setting up your Laravel 12 application using Docker & Docker Compose.

## Prerequisites
Ensure you have the following installed on your system:
- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (https://docs.docker.com/compose/install/)

## Step 1: Clone the Repository

```bash
git clone https://github.com/lemonkazi/laravel-12-practice.git
cd laravel-12-practice
```

## Step 2: Set Up Environment Variables
Create a .env file from .env.example and configure database settings:

```bash
cp .env.example .env
```

Update the .env file:

```env
APP_NAME=Laravel
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost

DB_CONNECTION=mysql
DB_HOST=db
DB_PORT=3306
DB_DATABASE=laravel_test
DB_USERNAME=user
DB_PASSWORD=secret

```

## Step 3: Build and Start Containers
Run the following command to build and start the containers:

```bash
docker-compose up -d --build
```

This will spin up the following containers:
- Laravel App (app)
- MySQL Database (db)

## Step 4: Install Dependencies
Run Laravel's dependency installation inside the container:

```bash
docker-compose exec -it app composer install
```

```bash
npm install
npm run build
```

```bash
sudo chmod -R a+rw storage bootstrap/cache
```

Generate an application key:

```bash
docker-compose run --rm app php artisan key:generate
```

Run database migrations:

```bash
docker-compose exec -it app php artisan migrate --seed
```

## Step 5: Access the Application
- Laravel API: http://localhost:5000
- MySQL Database: localhost:3306 (Username: user, Password: secret)

To check running containers:

```bash
docker ps
```

## Step 6: Stopping and Restarting Containers
To stop the containers:

```bash
docker-compose down
```

To restart them:

```bash
docker-compose up -d
```

## Step 7: Running Tests
You can run Laravel tests inside the container:

```bash
docker-compose exec -it app php artisan test
```

## Troubleshooting
- If containers fail to start, check logs:
  
```bash
  docker-compose logs app
```
- If database issues arise, try:
  
```bash
  docker-compose exec -it app php artisan migrate:fresh --seed
```
```bash
docker-compose exec app bash -c 'echo "xdebug.mode=coverage" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini'
```
# Restart container
```bash
docker-compose restart app
```

```bash
docker-compose exec app ./vendor/bin/phpunit --coverage-html coverage
```


You're all set! Start building your Laravel App!

# codecov
[![codecov](https://codecov.io/gh/lemonkazi/practice/branch/master/graph/badge.svg)](https://codecov.io/gh/lemonkazi/practice)

## About Laravel

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel takes the pain out of development by easing common tasks used in many web projects, such as:

- [Simple, fast routing engine](https://laravel.com/docs/routing).
- [Powerful dependency injection container](https://laravel.com/docs/container).
- Multiple back-ends for [session](https://laravel.com/docs/session) and [cache](https://laravel.com/docs/cache) storage.
- Expressive, intuitive [database ORM](https://laravel.com/docs/eloquent).
- Database agnostic [schema migrations](https://laravel.com/docs/migrations).
- [Robust background job processing](https://laravel.com/docs/queues).
- [Real-time event broadcasting](https://laravel.com/docs/broadcasting).

Laravel is accessible, powerful, and provides tools required for large, robust applications.

## Learning Laravel

Laravel has the most extensive and thorough [documentation](https://laravel.com/docs) and video tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.

You may also try the [Laravel Bootcamp](https://bootcamp.laravel.com), where you will be guided through building a modern Laravel application from scratch.

If you don't feel like reading, [Laracasts](https://laracasts.com) can help. Laracasts contains thousands of video tutorials on a range of topics including Laravel, modern PHP, unit testing, and JavaScript. Boost your skills by digging into our comprehensive video library.

## Laravel Sponsors

We would like to extend our thanks to the following sponsors for funding Laravel development. If you are interested in becoming a sponsor, please visit the [Laravel Partners program](https://partners.laravel.com).

### Premium Partners

- **[Vehikl](https://vehikl.com/)**
- **[Tighten Co.](https://tighten.co)**
- **[WebReinvent](https://webreinvent.com/)**
- **[Kirschbaum Development Group](https://kirschbaumdevelopment.com)**
- **[64 Robots](https://64robots.com)**
- **[Curotec](https://www.curotec.com/services/technologies/laravel/)**
- **[Cyber-Duck](https://cyber-duck.co.uk)**
- **[DevSquad](https://devsquad.com/hire-laravel-developers)**
- **[Jump24](https://jump24.co.uk)**
- **[Redberry](https://redberry.international/laravel/)**
- **[Active Logic](https://activelogic.com)**
- **[byte5](https://byte5.de)**
- **[OP.GG](https://op.gg)**

## Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the [Laravel documentation](https://laravel.com/docs/contributions).

## Code of Conduct

In order to ensure that the Laravel community is welcoming to all, please review and abide by the [Code of Conduct](https://laravel.com/docs/contributions#code-of-conduct).

## Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via [taylor@laravel.com](mailto:taylor@laravel.com). All security vulnerabilities will be promptly addressed.

## License

The Laravel framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
