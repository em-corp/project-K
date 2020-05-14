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

parser.add_argument('-m', '--module', help='Run module[s] with[out] arguments. Each modules are called seperatly. For modules options; provide `-h` in `mod_args`. Note: Please provide extra leading space in module\'s argument to not to let it expand before it is needed.  (e.g -m "mod1_name" "mod1_args" or -m "mod2_name" "mod2_args" "mod2_more_args" or -m "mod_name"  " -h")', dest='modules', action='append', nargs='+', metavar=('mod_name', 'mod_args'))
parser.add_argument('-L', '--list', help='List available modules', action='store_true', default=False, dest='mod_list')

proxy_group = parser.add_mutually_exclusive_group()
proxy_group.add_argument('-P', '--proxy', help='Add proxy to use.', dest='proxy', type=str, metavar='proxy_url')
proxy_group.add_argument('--proxy-file', help='Add file containing list of proxies. File should contain 1 proxy per line.', dest='proxyfile', type=str, metavar='proxy_file')

ua_group = parser.add_mutually_exclusive_group()
ua_group.add_argument('-U', '--useragent', help="Add useragent", dest='ua', type=str, metavar='useragent')
ua_group.add_argument('--ua-file', help='Add file containing list of useragents. File should contain 1 useragent per line.', dest='uafile', type=str, metavar='ua_file')

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

def FiletoList(lfile, emsg):
    lst = []
    if os.path.exists(lfile) and os.path.isfile(lfile):
        with open(lfile, 'r') as f:
            for l in f:
                lst.append(l)
        return lst
    else:
        raise Exception(emsg)

if args.proxy:
    cman.set("proxy_list", [args.proxy])
elif args.proxyfile:
    pf = args.proxyfile
    cman.set("proxy_list", FiletoList(pf, "Incorrect proxy file `{}`"\
            .format(pf)))
elif cman.get('proxy'):
    # More specific, more preferred
    cman.set("proxy_list", [cman.get('proxy')])
elif cman.get('proxy_file'):
    pf = cman.get('proxy_file')
    cman.set("proxy_list", FiletoList(pf, "Incorrect proxy file `{}`"\
            .format(pf)))
else:
    # If nothing then empty
    cman.set("proxy_list", [])

if args.ua:
    cman.set("ua_list", [args.ua])
elif args.uafile:
    uaf = args.uafile
    cman.set("ua_list", FiletoList(uaf, "Incorrect useragent file `{}`"\
            .format(uaf)))
elif cman.get('useragents_file'):
    uaf = cman.get('useragents_file')
    cman.set("ua_list", FiletoList(uaf, "Incorrect useragent file `{}`"\
            .format(uaf)))
else:
    cman.set("ua_list", ["Project K/{version} (Linux; Python3 urllib)"\
            .format(version=__VERSION__)])

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

