up:
	# bring up the services
	docker-compose up -d



build:
	docker-compose up -d --build --remove-orphans


sync:
	# set up the database tablea
	docker-compose run server python manage.py makemigrations --noinput
	# docker-compose exec server python manage.py migrate account --noinput
	docker-compose run server python manage.py migrate --noinput

superuser:
		docker-compose exec server python manage.py createsuperuser

wait:
	sleep 5

logs:
	docker-compose logs --follow

down:
	docker-compose down

test:
	docker-compose run server python manage.py test

reset: down up wait sync

hardreset: pull build reset
