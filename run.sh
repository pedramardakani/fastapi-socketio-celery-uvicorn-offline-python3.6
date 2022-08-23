#!/bin/bash

# Start the FastAPI backend on production environment
#
# Original author:
#   Pedram Ashofteh Ardakani <pedramardakani@pm.me>
# Contributing author(s):
# Copyright(c) 2022
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# version 3 or later as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.LIB.  If not, write
# to the Free Software Foundation, Inc., 51 Franklin Street, Fifth
# Floor, Boston, MA 02110-1301, USA.


# Group all the processes
setsid bash -s <<EOF &
source .venv/bin/activate
export FASTAPI_CONFIG=production

python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 | tee uvicorn.log &
python3 -m celery -A main.celery worker --loglevel=INFO | tee celery.log &
wait
EOF

# Take a note of the process group id (pgid)
pgid=$!

# Write it down to the .pgid file so we can kill the process group by id
echo $pgid > .pgid
