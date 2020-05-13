'''
project-K main file

'''

# >> Version <<
major_version = '0'
minor_version = '1'
extra_version = '(alpha)'
__VERSION__ = major_version + '.' + minor_version + ' ' + extra_version

# >> Banner <<
def banner():
    print("""
   .                 
  d8c           .o@8 
^*888%      .o@8888% 
  "8    .o@8888%"    
       8888R"        
   .   "*8888bu.     
 .@8c     ^"*8888bu. 
'%888"        ^%*888 
  ^*              ^% 
      Project K
    """)

banner()

# >> Arguments parse <<
import argparse

parser = argparse.ArgumentParser(prog='projekt')

parser.add_argument('-m', '--module', help='Run module[s] with[out] arguments. Each modules are called seperatly. For modules options; provide `-h` in `mod_args`. Note: Please provide extra leading space in module\'s argument to not to let it expand before it is needed.  (e.g -m "mod1_name" "mod1_args" or -m "mod2_name" "mod2_args" "mod2_more_args" or -m "mod_name"  " -h")', dest='modules', action='append', nargs='+', metavar='mod_args')
parser.add_argument('-L', '--list', help='List available modules', action='store_true', default=False, dest='mod_list')

parser.add_argument('-P', '--proxy', help='Add prox(y|ies) to use, Use "," to seperate multiple.', dest='proxies', type=str)
parser.add_argument('-U', '--useragent', help="Add useragents", dest='ua', type=str)
parser.add_argument('-p', '--parallel', help="Maximum number of parallel threads.", dest='threads', type=int)

parser.add_argument('-v', '--verbose', help='Be verbose, Add multiple time to increase verbosity.', action='count', dest='verbose')
parser.add_argument('-V', '--version', help='Show version and exit', action='version', version=__VERSION__)

args = parser.parse_args()

# >> Global Argument parse  & Build Conf<<
from lib.config import ConfigManager
import os

proj_path = os.path.dirname(os.path.realpath(__file__))
cfile = "{}/config/default.conf".format(proj_path)

cman = ConfigManager.load(cfile)

cman.set('project_path', proj_path)

if args.proxies:
    cman.set("proxy_list", args.proxies.split(','))

if args.ua:
    cman.set("ua_list", args.ua.split(','))

if args.threads:
    cman.set("max_threads", int(args.threads))

if args.verbose:
    cman.set("verbosity", int(args.verbose))

kwargs = {
        "conf": cman
        }

# >> Imports <<
from lib.modules import ModuleLoader as module
from lib.modules import ModuleMeta

# >> Main (Methods) <<
def list_modules():
    l = ModuleMeta.list(cman.get('project_path'))
    if len(l) > 0:
        print("Available Modules:")
        for i in l:
            print ("[*] {mod_name}".format(mod_name=i))
    else:
        print("No Modules available.")

def load_modules(mod_list):
    for mod in args.modules:
        if mod:
            mod_name = mod[0]
            mod_args = ''
            if len(mod) > 1:
                mod_args = " ".join(mod[1:])

            mod_obj = module.load(mod_name, **kwargs)
            mod_obj.call(mod_args)

# >> Main <<
if args.mod_list:
    list_modules()
    quit()

if args.modules:
    try:
        load_modules(args.modules)
    except Exception as e:
        print("[ERROR]: {}".format(e))

