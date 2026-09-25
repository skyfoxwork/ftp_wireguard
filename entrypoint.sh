#!/bin/sh

# Create TUN device if it doesn't exist
if [ ! -c /dev/net/tun ]; then
    mkdir -p /dev/net
    mknod /dev/net/tun c 10 200
    chmod 666 /dev/net/tun
fi

# Pass control to the original container command
# Execute the main container command
exec "$@"
