from project.socketio_utils.base import BaseSocket

class ExtendedSocket(BaseSocket):
    def __init__(self):
        # Retreive everything from BaseSocket
        super().__init__()
        sio = self.sio

        # Extend the events
        #
        # Override the 'echo' event from BaseSocket
        @sio.event
        def echo(sid, data):
            print(f"Extended socket heard session id <{sid}> say: '{data}'")
