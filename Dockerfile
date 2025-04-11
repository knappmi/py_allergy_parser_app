# Dockerfile
FROM python:3.10-slim

# Install dependencies
RUN apt update && apt install -y \
    openjdk-17-jdk \
    unzip \
    git \
    zip \
    libncurses5 \
    libffi-dev \
    libssl-dev \
    build-essential \
    python3-pip \
    python3-dev \
    libsqlite3-dev \
    zlib1g-dev \
    wget \
    libjpeg-dev \
    && pip install --no-cache-dir buildozer cython

WORKDIR /app
