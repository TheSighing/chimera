import zmq
import msgpack

class Server(object):

    def __init__(self, obj):
        self.methods = self._parse_methods(obj)
        self.ctx = zmq.Context()
        self.socket = self.ctx.socket(zmq.REP)

    def _parse_methods(self, obj):
        methods = {}
        for method in dir(obj):
            if not method.startswith('_'):
                methods[method] = getattr(obj, method)

        return methods

    def bind(self, *args):
        self.socket.bind(*args)

    def _recv(self):
        return msgpack.unpackb(self.socket.recv())

    def _send(self, msg):
        self.socket.send(msgpack.packb(msg))

    def _process(self, req):
        header, method, args = req
        rtn = self.methods[method](*args)
        h = {'response_to': 0, 'message_id':0, 'v': 3}
        return (h, 'OK', [rtn])

    def run(self):
        while True:
            req = self._recv()
            rep = self._process(req)
            self._send(rep)
