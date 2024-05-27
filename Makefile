LOCAL ?= docker/local.yml


bup:
	 docker-compose -f $(ENV) build && \
	 docker-compose -f $(ENV) stop && \
	 docker-compose -f $(ENV) rm -f && \
	 docker-compose -f $(ENV) up -d && \
	 docker system prune --force && \
	 docker exec -it backend python3 manage.py migrate && \
	 docker exec -it backend python3 manage.py load_offline_days


bup_lite:
	 docker-compose -f $(ENV) build && \
	 docker-compose -f $(ENV) stop && \
	 docker-compose -f $(ENV) rm -f && \
	 docker-compose -f $(ENV) up -d && \
	 docker system prune --force


bup_local:
	 docker-compose -f $(ENV) build && \
	 docker-compose -f $(ENV) stop && \
	 docker-compose -f $(ENV) rm -f && \
	 docker-compose -f $(ENV) up -d

pro: ENV:=$(PRODUCTION)
pro: bup

lite: ENV:=$(PRODUCTION)
lite: bup_lite

dev: ENV:=$(DEVELOPMENT)
dev: bup

local: ENV:=$(LOCAL)
local: bup_local


banned:
	docker exec -it nginx fail2ban-client status nginx-unauthorized

unban: # The properly way for type this command is: make IP=<ip_to_unban> unban
	docker exec -it nginx fail2ban-client set nginx-unauthorized unbanip $(IP)

up:
	docker-compose -f $(LOCAL) up

migrate:
	docker-compose -f $(ENV) exec backend python3 manage.py migrate

migratepro: ENV:=$(PRODUCTION)
migratepro: migrate

migratedev: ENV:=$(DEVELOPMENT)
migratedev: migrate


collectstatic:
	docker-compose -f $(ENV) exec backend /venv/bin/python3 manage.py collectstatic

collectpro: ENV:=$(PRODUCTION)
collectpro: collectstatic

collectdev: ENV:=$(DEVELOPMENT)
collectdev: collectstatic

preparelocal:
	docker exec -it backend python3 manage.py collectstatic
	docker exec -it backend python3 manage.py makemigrations
	docker exec -it backend python3 manage.py migrate
	docker exec -it backend python3 manage.py createsuperuser

superuser:
	docker-compose -f $(ENV) exec backend /venv/bin/python3 manage.py createsuperuser

superuserpro: ENV:=$(PRODUCTION)
superuserpro: superuser

superuserdev: ENV:=$(DEVELOPMENT)
superuserdev: superuser

superuserlocal: ENV:=$(LOCAL)
superuserlocal: superuser

mm:
	(cd sources && python3 manage.py makemigrations)

mu:
	docker-compose exec backend python3 manage.py migrate