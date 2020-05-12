import random

class BaseModule:
    def __init__(self, proxy_list=[], ua_list=[], max_threads=1, verbosity=0):
        self.proxy_list = proxy_list
        self.ua_list = ua_list
        self.max_threads = max_threads
        self.verbosity = verbosity

    def call(self, **kwargs):
        self.main(**kwargs)

    def getProxyList(self):
        return self.proxy_list

    def getUAList(self):
        return self.ua_list

    def getRandomProxy(self):
        try:
            return random.choice(self.proxy_list)
        except IndexError:
            return ''

    def getRandomUserAgent(self):
        try:
            return random.choice(self.ua_list)
        except IndexError:
            return ''

    def getVerbosity(self):
        return self.verbosity

    def getMaxAllowedThreads(self):
        return self.max_threads

    def setProxyList(self, l=[]):
        self.proxy_list.append(l)

    def setUAList(self, ual=[]):
        self.ua_list.append(ual)

    def setMaxAllowedThreads(self, c):
        self.max_threads = c
    
    def serVerbosity(self, v):
        self.verbosity = v

    def addProxy(self, p=''):
        self.proxy_list.append(p)
    
    def addUserAgent(self, ua=''):
        self.ua_list.append(ua)

