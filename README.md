# django-weather-api
with Django, DRF, Celery + Redis, BeautifulSoap4, Postgres, Docker, PEP 8

# How to run a project on your local machine?
1. Install Docker https://docs.docker.com/engine/install/
1.1. Please check and specify docker-compose.yml environment variables.
2. Run `docker-compose up --build pgadmin`
3. If you have [Errno 13] Permission denied: '/var/lib/pgadmin/sessions'
use command to give permissions `make permission`
4. Open http://localhost:5050/browser/ add connect to server with:
`DB_HOST: postgres`
`POSTGRES_DB: weather_api_dev`
`POSTGRES_USER: weather_api_dev`
`POSTGRES_PASSWORD: pass`
5. Run `docker-compose up --build`
6. If you have error /data/db: permission denied failed to solve run: `make permission`
7. Run migrations by `docker exec -it weather_api_web python manage.py migrate`
8. Run to create admin user `docker exec -it weather_api_web python manage.py createsuperuser` 
9. Open http://localhost:8080/admin/ in browser and auth with user created at step 8
10. Open http://localhost:8080/api/v1/forecast/ in browser to see weather forecast data
11. Open http://localhost:8080/api/v1/forecast/run-task/ in browser to run celery task manually
12. Open http://localhost:8080/api/v1/forecast/schedule-task/ in browser to schedule celery task on time for everyday execute

