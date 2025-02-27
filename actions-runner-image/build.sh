#!/bin/bash

while getopts t: opts; do
   case ${opts} in
      t) IMAGE_TAG=${OPTARG} ;;
      *) echo "Unknown option: $opts" ;;
   esac
done

if [ -z "${IMAGE_TAG}" ]; then
    echo "IMAGE_TAG is not set"
    exit 1
fi

echo "Building with IMAGE_TAG=${IMAGE_TAG}"

docker buildx build --push --builder kube --platform linux/amd64,linux/arm64 \
    --build-arg IMAGE_TAG="${IMAGE_TAG}" \
    --cache-from type=s3,region=eu-west-1,bucket=spt-docker-cache \
    --cache-to type=s3,region=eu-west-1,bucket=spt-docker-cache \
		-t 268324876595.dkr.ecr.eu-west-1.amazonaws.com/spt-actions-runner:"${IMAGE_TAG}" "$(dirname "$0")"
