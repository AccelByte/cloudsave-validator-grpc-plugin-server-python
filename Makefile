# Copyright (c) 2022 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

BUILDER := grpc-plugin-server-builder
IMAGE_NAME := $(shell basename "$$(pwd)")-app

clean:
	rm -rf $(SOURCE_DIR)/$(PROTO_DIR)/*_grpc.py
	rm -rf $(SOURCE_DIR)/$(PROTO_DIR)/*_pb2.py
	rm -rf $(SOURCE_DIR)/$(PROTO_DIR)/*_pb2.pyi
	rm -rf $(SOURCE_DIR)/$(PROTO_DIR)/*_pb2_grpc.py

proto: clean
proto:
	docker run --rm --tty -u $$(id -u):$$(id -g) \
		--volume $$(pwd):/data \
		--workdir /data \
		rvolosatovs/protoc:4.1.0 \
			--proto_path=app/proto=src/app/proto \
			--python_out=src \
			--grpc-python_out=src \
			src/app/proto/*.proto

build: proto

beautify:
	docker run --rm --tty --user $$(id -u):$$(id -g) \
		--volume $$(pwd):/data \
		--workdir /data \
		cytopia/black:22-py3.9 \
		src

lint:
	rm -f lint.err
	docker run --rm --tty --user $$(id -u):$$(id -g) \
		--volume $$(pwd):/data \
		--workdir /data \
		--entrypoint /bin/sh \
		cytopia/pylint \
			-c 'pylint -j 4 --ignore=src/app/proto src || exit $$(( $$? & (1+2+32) ))' || touch lint.err
	[ ! -f lint.err ]

install:
	pip install .

run:
	python -m app

image:
	docker buildx build -t ${IMAGE_NAME} --load .

imagex:
	docker buildx inspect $(BUILDER) || docker buildx create --name $(BUILDER) --use
	docker buildx build -t ${IMAGE_NAME} --platform linux/arm64/v8,linux/amd64 .
	docker buildx build -t ${IMAGE_NAME} --load .
	docker buildx rm --keep-state $(BUILDER)

imagex_push:
	@test -n "$(IMAGE_TAG)" || (echo "IMAGE_TAG is not set (e.g. 'v0.1.0', 'latest')"; exit 1)
	@test -n "$(REPO_URL)" || (echo "REPO_URL is not set"; exit 1)
	docker buildx inspect $(BUILDER) || docker buildx create --name $(BUILDER) --use
	docker buildx build -t ${REPO_URL}:${IMAGE_TAG} --platform linux/arm64/v8,linux/amd64 --push .
	docker buildx rm --keep-state $(BUILDER)

ngrok:
	@test -n "$(NGROK_AUTHTOKEN)" || (echo "NGROK_AUTHTOKEN is not set" ; exit 1)
	docker run --rm -it --net=host -e NGROK_AUTHTOKEN=$(NGROK_AUTHTOKEN) ngrok/ngrok:3-alpine \
			tcp 6565	# gRPC server port
