#!/bin/bash
SCRIPT_NAME=$1
docker run --gpus all -it --rm \
    -v ~/projects:/workspace \
    nvcr.io/nvidia/isaac-sim:2023.1.1 \
    python /workspace/${SCRIPT_NAME}