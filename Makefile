redis-docker:
	docker run -p 6379:6379 -d redis:alpine

worker:
	python manage.py rqworker default

