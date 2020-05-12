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

parser.add_argument('-m', '--module', help='Run module[s] with[out] arguments. Each modules are called seperatly. e.g -m "mod1_name" "mod1_args" -m "mod2_name" "mod2_args" "mod2_more_args"', dest='modules', action='append', nargs='+', metavar='mod_args')
parser.add_argument('-L', '--list', help='List available modules', action='store_true', default=False)

parser.add_argument('-P', '--proxy', help='Add prox(y|ies) to use, Use "," to seperate multiple.', dest='proxies', type=str)
parser.add_argument('-U', '--useragent', help="Add useragents", dest='ua', type=str)
parser.add_argument('-p', '--parallel', help="Maximum number of parallel threads.", dest='threads', type=int)

parser.add_argument('-v', '--verbose', help='Be verbose, Add multiple time to increase verbosity.', action='count', dest='verbose')
parser.add_argument('-V', '--version', help='Show version and exit', action='version', version=__VERSION__)

args = parser.parse_args()

# >> Global Argument parse <<
proxy_list = []
if args.proxies:
    proxy_list = args.proxies.split(',')

ua_list = []
if args.ua:
    ua_list = args.ua.split(',')

max_threads = 1
if args.threads:
    max_threads = int(args.threads)

verbose_level = 0
if args.verbose:
    verbose_level = int(args.verbose)


kwargs = {
        'proxy_list': proxy_list,
        'ua_list' : ua_list,
        'max_threads': max_threads,
        'verbosity': verbose_level
        }

# >> Main <<


