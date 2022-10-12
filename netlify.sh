#!/bin/bash

# This script is used by netlify

sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
./bin/task sdk -- html
