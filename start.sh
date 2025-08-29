#!/bin/bash

source .venv/bin/activate

echo "===========| RUNNING MIGRATIONS |==========="
alembic upgrade head

echo "===========| STARTING APPLICATION |==========="
python -m app
