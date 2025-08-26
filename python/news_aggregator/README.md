docker-compose exec -T db mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS python_practice;" 

docker-compose exec -T db mysql -u root -p -e "GRANT ALL PRIVILEGES ON python_practice.* TO 'user'@'%';
FLUSH PRIVILEGES;"

docker-compose exec python alembic init migrations
 
docker-compose exec python alembic revision --autogenerate -m "add initial tables"

docker-compose exec python alembic upgrade head

