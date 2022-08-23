#!/bin/bash

# Start the FastAPI backend in the development environment
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


# Group all processes
setsid bash -s <<EOF &
source .venv/bin/activate
export FASTAPI_CONFIG=development

redis-server &
python3 -m celery -A main.celery worker --loglevel=info | tee celery.log &
python3 -m uvicorn main:app --host localhost --port 8000 --reload | tee uvicorn.log &
wait
EOF


pgid=$!


echo $pgid > .pgid
