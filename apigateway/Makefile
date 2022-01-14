IMAGE_NAME=apigateway-service
CONTAINER_NAME=apigateway-service
INTERNAL_PORT=5000
EXTERNAL_PORT=80
NUTS_HOST=http://nuts-n-bolts:5001
BOLTS_HOST=http://nuts-n-bolts:5002
WORKERS=2
NETWORK=nutsnbolts-net

all:
	make clean
	make build
	make run

clean:
	@echo "> Removing container $(CONTAINER_NAME)"
	- @docker rm $(CONTAINER_NAME)
	@echo "> Removing image $(CONTAINER_NAME)"
	- @docker image rm $(CONTAINER_NAME)

build:
	@docker \
		build . \
		--build-arg INTERNAL_PORT=$(INTERNAL_PORT) \
		--build-arg WORKERS=$(WORKERS) \
		--build-arg NUTS_HOST=$(NUTS_HOST) \
		--build-arg BOLTS_HOST=$(BOLTS_HOST) \
		-t $(CONTAINER_NAME)

clean-build:
	make clean
	make build

run:
	@docker network inspect $(NETWORK) >/dev/null 2>&1 || \
    	docker network create --driver bridge $(NETWORK)

	@docker \
		run \
		--network $(NETWORK) \
		-p $(EXTERNAL_PORT):$(INTERNAL_PORT) \
		--name=$(CONTAINER_NAME) \
		$(IMAGE_NAME) \
		-d

start:
	@docker start $(CONTAINER_NAME)

stop:
	@docker stop $(CONTAINER_NAME)
