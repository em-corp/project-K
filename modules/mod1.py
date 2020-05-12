import sys
from lib.modules import BaseModule

class mod1(BaseModule):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def main(self, **kwargs):
        print(">>> proxy: {}".format(self.getProxyList()))
        print(">>> ua: {}".format(self.getUAList()))
        print(">>> thread: {}".format(self.getMaxAllowedThreads()))
        print(">>> verbosity: {}".format(self.getVerbosity()))
        print(">>> proxy: {}".format(self.getRandomProxy()))
        print(">>> ua: {}".format(self.getRandomUserAgent()))

