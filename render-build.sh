#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Initialize migrations if not already done
if [ ! -d "migrations" ]; then
  flask db init
fi

# Create migration
flask db migrate -m "Initial migration"

# Run database migrations
flask db upgrade

# Seed the database
python seeds.py
