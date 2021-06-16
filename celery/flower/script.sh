#!/bin/bash

echo "running celery with tmux..."
tmux new-session -d -s bgtask "celery -A hello worker --loglevel=INFO"

echo "runing flower..."
celery -A hello flower
