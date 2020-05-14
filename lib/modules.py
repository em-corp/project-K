__all__ = []

import random
import importlib
import argparse
import os

class BaseModule:
    def __init__(self, **kwargs):
        if 'conf' in kwargs.keys():
            self.conf = kwargs['conf']
        else:
            self.conf = {}  # This should never happens, but keep it

    def call(self, args):
        self.getParser()
        self.defineArgs()
        self.parseArgs(args)
        self.main()

    def main(self):
        # * This method needs to be overridden in every module
        pass

    def getConfig(self):
        return self.conf

    def getParser(self):
        if not hasattr(self, 'parser'): 
            self.parser = argparse.ArgumentParser(prog='projekt -m {}'\
                    .format(self.__class__.__name__))
        return self.parser 

    def defineArgs(self):
        # * This method needs to be overridden in every module
        pass

    def parseArgs(self, args):
        self.args = self.getParser().parse_args(args.split())

    def getArgs(self):
        return self.args
       
    def getArg(self, key):
        return vars(self.getArgs())[key]

    def getVerbosity(self):
        return self.getConfig().get('verbosity')

    def getMaxAllowedThreads(self):
        return self.getConfig().get('max_threads')

    def setMaxAllowedThreads(self, m):
        self.getConfig().set('max_threads', m)
    
    def setVerbosity(self, v):
        self.getConfig().set('verbosity', v)

    def getProxyList(self):
        return self.getConfig().get('proxy_list')

    def getRandomProxy(self):
        try:
            return random.choice(self.getProxyList())
        except IndexError:
            return ''

    def getUAList(self):
        return self.getConfig().get('ua_list')

    def getRandomUserAgent(self):
        try:
            return random.choice(self.getUAList())
        except IndexError:
            return ''

class ModuleLoader:
    def load(mod_name, **def_args):
        try:
            module = importlib.import_module('modules.{}'.format(mod_name))
        except ModuleNotFoundError:
            pass
        else:    
            if hasattr(module, mod_name):
                mod_class = getattr(module, mod_name)
                if issubclass(mod_class, BaseModule):
                    mod_obj = mod_class(**def_args)
                    return mod_obj
        raise Exception('Module "{}" not found or is incorrect.'\
                .format(mod_name))


class ModuleMeta:
    def list(p_path):
        mod_list = []
        mod_dir = "{}/modules".format(p_path)
        
        if os.path.exists(mod_dir) and os.path.isdir(mod_dir):
            for f in os.listdir(mod_dir):
                if not f.startswith('_'):
                    mod_list.append(f.replace('.py', ''))

        return mod_list
