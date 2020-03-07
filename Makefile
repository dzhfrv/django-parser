redis-docker:
	docker run -p 6379:6379 -d redis:alpine

worker:
	python manage.py rqworker default

clean:
	black -l 79 -S apps/
	isort -rc apps/