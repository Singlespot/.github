#!/bin/bash

while getopts t:o: opts; do
   case ${opts} in
      t) IMAGE_TAG=${OPTARG} ;;
      o) OUTPUT_TAG=${OPTARG} ;;
      *) echo "Unknown option: $opts" ;;
   esac
done

if [ -z "${IMAGE_TAG}" ]; then
    echo "IMAGE_TAG is not set"
    exit 1
fi

if [ -z "${OUTPUT_TAG}" ]; then
    OUTPUT_TAG=${IMAGE_TAG}
fi

echo "Building with IMAGE_TAG=${IMAGE_TAG}, OUTPUT_TAG=${OUTPUT_TAG}"

kubuild --build-arg IMAGE_TAG="${IMAGE_TAG}" \
		268324876595.dkr.ecr.eu-west-1.amazonaws.com/spt-actions-runner:"${OUTPUT_TAG}" "$(dirname "$0")"
