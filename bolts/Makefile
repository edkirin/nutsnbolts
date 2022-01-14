IMAGE_NAME=bolts-service
CONTAINER_NAME=bolts-service
INTERNAL_PORT=5000
WORKERS=2

USER_ID?=$(shell id -u)
SERVICE_NAME=bolts


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
			-t $(CONTAINER_NAME)


clean-build:
	make clean
	make build


container:
	@make filesreadable
	@cd ../capps; \
		docker-compose stop $(SERVICE_NAME)
	@docker-compose run --rm $(SERVICE_NAME)
	@make filesreadable


# correct the file permissions post docker
filesreadable:
	@test "$$(find . -uid 0)" && \
		echo "Need to correct file permissions, active directory authentication required" && \
		sudo find . -uid 0 -exec chown "$(USER_ID)":"$(USER_ID)" {} \; || true


install:
ifneq ($(DOCKER_CONTAINER),)
	@pip install pip -U
	@pip install -r requirements.txt
else
	@echo "Command should be started inside container"
endif


run:
ifneq ($(DOCKER_CONTAINER),)
	@cd /app; \
	./run.sh
else
	@echo "Command should be started inside container"
endif
