#!/bin/bash
set -e
docker build -t keymon/inline-shell-resource .
docker push keymon/inline-shell-resource
