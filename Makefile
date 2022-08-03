
clean-all:
	cd apigateway && make clean
	cd nuts && make clean
	cd bolts && make clean
	cd db && make clean

build-all:
	cd apigateway && make build
	cd nuts && make build
	cd bolts && make build
	cd db && make build

clean-build-all:
	make clean-all
	make build-all
