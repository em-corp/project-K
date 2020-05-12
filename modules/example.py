# * if needed to run seperately
if __name__ == "__main__":
    import sys
    # * insert lib's parent dir to sys.path at beginning
    sys.path.insert(0, "{}/../".format(sys.path[0]))

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
        self.getParser().add_argument("-d", "--def", help = "test arg1", dest='defin')
        self.getParser().add_argument("-e", "--exp", help = "test arg2", dest='exp')
        self.getParser().add_argument("-v", "--version", help='version', action='version', version='5.1')

    def main(self):
        # * main method to start custom calls
        # * retrive arguments by `self.getArgs()` call
        # * or, retrive arguments by `self.getArg('arg_name')` call

        print("============> {}".format(self.getVerbosity()))
        
        print("============> {}".format(self.getArgs().defin))
        print("============> {}".format(self.getArg('defin')))
        print("============> {}".format(self.getArgs().exp))
        print("============> {}".format(self.getArg('exp')))

# * if needed to run seperately
if __name__ == "__main__":
    kwargs = {
            'proxy_list': '',
            'ua_list' : '',
            'max_threads': 1,
            'verbosity': 5
        }
    mod_obj = example(**kwargs)
    #mod_obj = example()
    mod_obj.call(" ".join(sys.argv[1:]))

