run:
	docker-compose up

permission:
	sudo chmod -R 777 ./pgadmin && sudo chmod -R 777 ./data/db

test:
	docker-compose run --rm web python manage.py test

migrate:
	docker-compose run --rm web python manage.py migrate

shell:
	docker-compose run --rm web python manage.py shell

req:
	pip freeze > requirements.txt