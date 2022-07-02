import socketio
from project.config import settings

class BaseSocket:
    def __init__(self):
        # Socket setup based on settings
        self.sio = socketio.AsyncServer(
            async_mode=settings.SIO_MODE,
            cors_allowed_origins=settings.SIO_CORS,
        )

        # For ease of use and referencing
        sio = self.sio

        # Need to call this in FastAPI
        self.socket_app = socketio.ASGIApp(socketio_server=sio)

        # Basic events
        @sio.event
        async def connect(sid, env):
            print(f"on connect: {sid}")

        @sio.event
        async def disconnect(sid):
            print(f"on disconnect: {sid}")

        @sio.event
        async def echo(sid, data):
            print(f"BaseSocket heard session id <{sid}> say: '{data}'")
