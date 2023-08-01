#!/bin/bash
# This script is used by cloud flare.
# The name is a leftover from when we used Netlify to build the website.
python3 -m pip install .
python3 -m sdk html
