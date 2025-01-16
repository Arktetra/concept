#!/usr/bin/env bash

find . -type f -name "*.DS_Store" -ls -delete
find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
rm -rf .coverage*
