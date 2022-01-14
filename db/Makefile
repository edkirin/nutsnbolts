IMAGE_NAME=nutsnbolts-db
CONTAINER_NAME=nutsnbolts-db
POSTGRES_USER=nutsnbolts
POSTGRES_PASSWORD=nutsnbolts
POSTGRES_DB=nutsnbolts
INTERNAL_PORT=5432
EXTERNAL_PORT=55432


clean:
	@echo "> Removing container $(CONTAINER_NAME)"
	- @docker rm $(CONTAINER_NAME)
	@echo "> Removing image $(CONTAINER_NAME)"
	- @docker image rm $(CONTAINER_NAME)

build:
	@docker \
		build . \
		--build-arg POSTGRES_DB=${POSTGRES_DB} \
		--build-arg POSTGRES_USER=${POSTGRES_USER} \
		--build-arg POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
		-t $(CONTAINER_NAME)

clean-build:
	make clean
	make build

run:
	@docker \
		run \
		-p $(EXTERNAL_PORT):$(INTERNAL_PORT) \
		-e PGDATA=/var/lib/postgresql/data/pgdata \
		-e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
		-e POSTGRES_DB=${POSTGRES_DB} \
		--name=$(CONTAINER_NAME) \
		$(IMAGE_NAME) \
		-d

start:
	@docker start $(CONTAINER_NAME)

stop:
	@docker stop $(CONTAINER_NAME)
