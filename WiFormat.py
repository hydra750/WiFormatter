import os, sys, argparse, locale

locale.setlocale(locale.LC_ALL, '')

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-min', '--min-key-length', help='Define the minimum wireless key', default=8)
arg_parser.add_argument('-max', '--max-key-length', help='Define the maximum wireless key', default=63)
arg_parser.add_argument('-i', '--input', help='Specify the input wordlist')
arg_parser.add_argument('-o', '--output', help='Specify the output wordlist')
arg_parser.add_argument('-v', '--overwrite', help='Overwrite wordlist', action='store_true', default=False)
arg_parser.add_argument('-d', '--diagnose', help='Diagnose wordlist', action='store_true', default=False)
args = arg_parser.parse_args()

if not len(sys.argv) > 1:
    print('\nTo get started, use the -h | --help switch')
    sys.exit()

if args.input==None:
    print('ERROR: input wordlist not specified')
    sys.exit()

if args.input!=None:
    if not os.path.isfile(args.input):
        print('ERROR: can not find input wordlist')
        sys.exit

banner = '';
print(banner)

file = open(args.input, 'r')
keys = file.read().split('\n')
file.close();

white_keys = []
black_keys = []

for key in keys:
    if len(key)>=args.min_key_length and len(key)<=args.max_key_length:
        white_keys.append(key)
    else:
        black_keys.append(key)

if args.diagnose:
    print('Total keys: {:n}'.format(len(white_keys)+len(black_keys)))
    print('White keys: {:n}'.format(len(white_keys)))
    print('Black keys: {:n}'.format(len(black_keys)))

if args.overwrite:
    white_output = ''
    for white in white_keys:
        white_output += white + '\n'
    white_output = white_output.rstrip()

    file = open(args.input, 'w')
    file.write(white_output)
    file.close()
    print('\n[+] wordlist overwritten')
    sys.exit

if args.input and args.output:
    white_output = ''
    for white in white_keys:
        white_output += white + '\n'
    white_output = white_output.rstrip()

    file = open(args.output, 'w')
    file.write(white_output)
    file.close()
    print('\n[+] wordlist created: {}'.format(args.output))
    sys.exit
