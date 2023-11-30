docker.up:
	docker-compose -f docker-compose.yaml up -d

docker.down:
	docker-compose -f docker-compose.yaml down -v

migrate.up:
	python manage.py migrate

run.local:
	python manage.py runserver 0.0.0.0:8000





