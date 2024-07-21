#!/bin/bash
SCRIPT_NAME=$1
docker run --gpus all -it --rm \
    -v ~/projects:/workspace \
    nvcr.io/nvidia/isaac-sim:4.0.0 \
    python /workspace/${SCRIPT_NAME}