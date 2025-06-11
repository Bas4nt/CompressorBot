#!/bin/bash
apt-get update && apt-get install -y ffmpeg mediainfo
python3 start.py
