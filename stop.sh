#!/bin/sh

# Stop the process group in .pgid
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


# Stop the previous process group if applicable
if [ -f .pgid ]; then

   # Execute a warm shutdown
   kill -TERM -$(cat .pgid)

   # Save kill exit status for later inspection
   status=$?

else

   # Prompt
   echo "Error: did not find the '.pgid' file"

   # Failed
   exit 1

fi


# Check if the process was shut down completely
if [ $status -eq 0 ]; then

   # Prompt
   echo ">>> SUCCESS: stopped the process group: <$(cat .pgid)>"

   # Remove the .pgid file to prevent stopping a similar process later
   rm .pgid

   # Done
   exit 0

else

   # Prompt
   echo ">>> FAIL: kill returned exit code <$status>"

   # Failed
   exit 1

fi
