# Use the official PHP 8.3 FPM image as the base image
FROM php:8.3-fpm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
    git \
    curl \
    unzip

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql \
    && pecl install pcov \
    && docker-php-ext-enable pcov

RUN pecl install xdebug \
    && docker-php-ext-enable xdebug


# Configure Xdebug for coverage
RUN echo "xdebug.mode=coverage" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

# Install Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

# Set the working directory
WORKDIR /var/www

# Copy application files
COPY . .

# Set permissions for Laravel storage and cache directories
RUN chown -R www-data:www-data /var/www/storage /var/www/bootstrap/cache

# Install Laravel dependencies
RUN composer install --optimize-autoloader

# Expose port 9000 for PHP-FPM
EXPOSE 9000

# Start PHP-FPM
CMD ["php-fpm"]