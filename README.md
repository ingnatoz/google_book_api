<p align="center"><img src="https://miro.medium.com/max/724/1*lAMsvtB6afHwTQYCNM1xvw.png" width="600"></p>

## Development Technologies Stack
- python https://www.python.org/downloads, https://hub.docker.com/_/python/
- Django  https://www.djangoproject.com
- Django Rest Framework https://www.django-rest-framework.org
- MySQL https://registry.hub.docker.com/_/mysql
## Architecture Execution with Docker
```shell
$ docker-compose build 
$ docker-compose up -d 
$ docker-compose exec backend python manage.py makemigrations
$ docker-compose exec backend python manage.py migrate
$ docker-compose restart backend
$ docker-compose exec backend python manage.py createsuperuser
```
## Pytest

```shell
$ docker-compose exec backend pytest
```
## API documentation

- https://documenter.getpostman.com/view/4638883/UzBsJjVo

