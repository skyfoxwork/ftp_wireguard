# indent must be a tab not a space

# Specify that commands do not require reprocessing of the file
.PHONY: build run

# Build image
build:
	docker build -t ftp_wireguard .

# Start container and remove it after execution
run:
	docker run --rm -it --cap-add=NET_ADMIN --cap-add=MKNOD --env-file .env ftp_wireguard
