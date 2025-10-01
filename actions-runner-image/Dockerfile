ARG IMAGE_TAG=latest
FROM ghcr.io/actions/actions-runner:${IMAGE_TAG}
ARG TARGETARCH

ENV PATH=/home/runner/.cargo/bin/:$PATH

RUN sudo add-apt-repository ppa:deadsnakes/ppa && \
  sudo apt-get update && \
  sudo apt-get install -y curl unzip \
    python3.13 python3.13-dev python3.13-venv \
    python3.12 python3.12-dev python3.12-venv \
    python3.11 python3.11-dev python3.11-venv && \
  sudo apt-get clean

RUN python3.13 -m ensurepip --upgrade && \
    python3.13 -m pip install --upgrade pip

RUN python3.12 -m ensurepip --upgrade && \
    python3.12 -m pip install --upgrade pip

RUN python3.11 -m ensurepip --upgrade && \
    python3.11 -m pip install --upgrade pip

RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.13 10 && \
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 10

RUN case ${TARGETARCH} in \
         "amd64")  ARCH=x86_64  ;; \
         "arm64")  ARCH=aarch64  ;; \
    esac && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-${ARCH}.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    sudo ./aws/install && \
    rm -rf awscliv2.zip

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
