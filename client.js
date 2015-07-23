/*

Create the js version of this setup so it can connect to the python server

class Client(object):

    def __init__(self):
        self.ctx = zmq.Context()
        self.socket = self.ctx.socket(zmq.REQ)

    def __call__(self, method, *args):
        self._send(method, *args)
        h, status, rtn = self._recv()
        return rtn[0]

    def _send(self, method, *args):
        header = {'message_id': 0, 'v': 3}
        self.socket.send(msgpack.packb((header, method, args)))

    def _recv(self):
        return msgpack.unpackb(self.socket.recv())

    def connect(self, *args):
        self.socket.connect(*args)*/
