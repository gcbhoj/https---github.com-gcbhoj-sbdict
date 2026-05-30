#!/bin/sh

gunicorn \
  --bind 0.0.0.0:5001 \
  --workers 2 \
  --timeout 120 \
  server:app