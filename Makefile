build:
	docker build -t ml-flask .
run:
	docker run -it  --rm -p 5566:80 --name ml-flask ml-flask
