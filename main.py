"""
A template backend with FastAPI [1], SocketIO [2] and Celery [3] for air-gapped
servers running python 3.6.5+.

Original author:
    Pedram Ashofteh Ardakani <pedramardakani@pm.me>
Contributing author(s):

Copyright(c) 2022

The main structure is heavily inspired from Michael Yin's [4] article
"The Definitive Guide to Celery and FastAPI" [5]. However, I've
integrated SocketIO and prepared this template for air-gapped servers.
It is worthy of note that the FastAPI docs are served in the /static
directory as instructed by Sebastián Ramírez (aka tiangolo) [6].


[1] https://github.com/tiangolo/fastapi
[2] https://github.com/miguelgrinberg/python-socketio
[3] https://github.com/celery/celery
[4] https://testdriven.io/authors/yin/
[5] https://testdriven.io/courses/fastapi-celery/app-factory/
[6] https://fastapi.tiangolo.com/advanced/extending-openapi/#self-hosting-javascript-and-css-for-docs


This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
version 3 or later as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; see the file COPYING.LIB.  If not, write
to the Free Software Foundation, Inc., 51 Franklin Street, Fifth
Floor, Boston, MA 02110-1301, USA.
"""

from project import create_app

app = create_app()
celery = app.celery_app
