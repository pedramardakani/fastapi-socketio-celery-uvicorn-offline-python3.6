from project.socketio_utils.extended import ExtendedSocket

socketio_object = ExtendedSocket()
sio = socketio_object.sio
socket_app = socketio_object.socket_app

def create_socketio():
    return socket_app