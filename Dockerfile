# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13.1
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /vpn_wireguard

# Install wireguard-tools, iptables, iproute2, openresolv, iputils-ping (ping)
# to work with network and wireguard (vpn)
RUN apt-get update && apt-get install -y --no-install-recommends \
    wireguard-tools \
    iptables \
    iproute2 \
    openresolv \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Download dependencies as a separate step to take advantage of Docker's caching.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Copy source code
COPY . .

# Specify the root for imports
ENV PYTHONPATH=/vpn_wireguard

COPY entrypoint.sh /entrypoint.sh

# Make it executable
RUN chmod +x /entrypoint.sh

# Set as the main entry point
ENTRYPOINT ["/entrypoint.sh"]

# Run the application.
CMD ["python3", "src/main.py"]
