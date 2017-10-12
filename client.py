#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import sys


class Client(object):

    def __init__(self):
        self.args = sys.argv[1:]
        self.request = []
        if len(self.args) == 2:
            self.request = [self.args[0], self.args[1]]
        if len(self.args) == 3:
            self.addr = self.args[2]
        else:
            self.addr = "localhost"
        self.ctx = zmq.Context()
        self.s = self.ctx.socket(zmq.REQ)

    def main(self):
        #  Connect socket to master
        self.s.connect("tcp://{}:5555".format(self.addr))

        print("Sending request  …")
        self.s.send_pyobj(self.request)

        #  Get the reply.
        message = self.s.recv_pyobj()
        print("Received reply [ %s ]" % message)


c = Client()
c.main()
