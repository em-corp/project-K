# * if needed to run seperately
if __name__ == "__main__":
    import sys
    import os

    proj_path = os.path.realpath("{}/../".format(os.path.dirname(os.path\
            .realpath(__file__))))
    sys.path.insert(0, proj_path)

    from lib.config import ConfigManager
    cman = ConfigManager.load("{}/config/default.conf".format(proj_path))
    cman.set('project_path', proj_path)

from lib.modules import BaseModule
import argparse

# * Module class name must be the same as of file name
class example (BaseModule):
    """
    * An example class for defining module
    *
    * only 3 methods are necessary to define.
    * `__init__(**kwargs)` with call to super with passing the `**kwargs`
    * `defineArgs()` to define modules related arguments
    * `main()` to be able to call from parent class
    """

    def __init__(self, **kwargs):
        # * to pass global arguments to BaseModule
        super().__init__(**kwargs)
    
    def defineArgs(self):
        # * define only arguments here
        # * do not define parser
        # * Always get parser with `self.getParser()` call
        self.getParser().add_argument("-d", "--def", help = "test arg1", \
                dest='defin')
        self.getParser().add_argument("-e", "--exp", help = "test arg2", \
                dest='exp')
        self.getParser().add_argument("-v", "--version", help='version', \
                action='version', version='5.1')

    def main(self):
        # * main method to start custom calls
        # * retrive arguments by `self.getArgs()` call
        # * or, retrive arguments by `self.getArg('arg_name')` call

        print("verbosity: {}".format(self.getVerbosity()))
        print("verbosity: {}".format(self.getConfig().get('verbosity')))
        print("User Agent: {}".format(self.getRandomUserAgent()))
        
        print("def: {}".format(self.getArgs().defin))
        print("def: {}".format(self.getArg('defin')))
        print("exp: {}".format(self.getArgs().exp))
        print("exp: {}".format(self.getArg('exp')))

# * if needed to run seperately
if __name__ == "__main__":
    kwargs = {
            'conf': cman
        }
    # * If needed to pass more arg, use cman to set them
    # cman.set('key', 'value')
    mod_obj = example(**kwargs)
    #mod_obj = example()
    mod_obj.call(" ".join(sys.argv[1:]))
