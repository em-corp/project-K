from lib.modules import BaseModule
import argparse

class example (BaseModule):
    """
    * An example class for defining module
    * only 3 methods are necessary to define.
    * `__init__(**kwargs)` with call to super with
        passing the `**kwargs`
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
        self.getParser().add_argument("-d", "--def", help = "default rgs", dest='defin')
        self.getParser().add_argument("-e", "--exp", help = "inew val ", dest='exp')
        self.getParser().add_argument("-v", "--version", help='version', action='version', version='5.1')

    def main(self):
        # * main method to start custom calls
        # * retrive arguments by `self.getArgs()` call

        print("============> {}".format(self.getVerbosity()))
        
        print("============> {}".format(self.args.defin))
        print("============> {}".format(self.args.exp))
