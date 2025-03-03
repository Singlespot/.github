ARG IMAGE_TAG=latest
FROM ghcr.io/actions/actions-runner:${IMAGE_TAG}

RUN sudo add-apt-repository ppa:deadsnakes/ppa && \
  sudo apt-get update && \
  sudo apt-get install -y python3.13 python3.13-dev python3.13-venv

RUN python3.13 -m ensurepip --upgrade && \
    python3.13 -m pip install --upgrade pip

RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.13 10
