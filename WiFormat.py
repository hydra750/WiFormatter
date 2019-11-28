import os, sys, argparse, ntpath

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-min', '--min-key-length', help='Define the minimum wireless key', default=8)
arg_parser.add_argument('-max', '--max-key-length', help='Define the maximum wireless key', default=63)
arg_parser.add_argument('-w', '--wordlist', help='Specify the wordlist')
arg_parser.add_argument('-f', '--focus', help='Focus output on the white list only', action='store_true', default=False)
arg_parser.add_argument('-v', '--overwrite', help='Overwrite wordlist', action='store_true', default=False)
arg_parser.add_argument('-d', '--diagnose', help='Diagnose wordlist', action='store_true', default=False)
args = arg_parser.parse_args()

if not len(sys.argv) > 1:
    print('\nTo get started, use the -h | --help switch')
    sys.exit()

if args.wordlist==None:
    print('ERROR: wordlist not specified')
    sys.exit()

if args.wordlist!=None:
    if not os.path.isfile(args.wordlist):
        print('ERROR: can not find wordlist')
        sys.exit

banner = '\n';
print(banner)

file = open(args.wordlist, 'r')
keys = file.read().split('\n')
file.close();

white_keys = []
black_keys = []

for key in keys:
    if len(key)>=args.min_key_length and len(key)<=args.max_key_length:
        white_keys.append(key)
    else:
        black_keys.append(key)

print('White keys: {}'.format(len(white_keys)))
print('Black keys: {}'.format(len(black_keys)))

if args.overwrite:
    white_output = ''
    for white in white_keys:
        white_output += white + '\n'
    white_output = white_output.rstrip()

    file = open(args.wordlist, 'w')
    file.write(white_output)
    file.close()
    print('\n[+] wordlist overwritten')
    sys.exit

if args.focus:
    white_output = ''
    for white in white_keys:
        white_output += white + '\n'
    white_output = white_output.rstrip()

    file = open('white_keys__'+ntpath.basename(args.wordlist), 'w')
    file.write(white_output)
    file.close()
    print('\n[+] white wordlist created')
    sys.exit

if args.diagnose:
    print('white keys: {}'.format(white_keys))
    print('black keys: {}'.format(black_keys))