"""pytouch.pytouch: provides entry point main()."""

__version__ = "0.1.1"

import sys
import os
import argparse
from typing import NoReturn
import colorama
from colorama import Fore


def main() -> None:
    """The main function ofs the script"""
    colorama.init()
    args = parse_args()

    for file in args.file:
        if os.path.exists(file):
            if not args.quiet:
                log_obj('The file already exists', file)
        else:
            try:
                write_into = args.text is not None

                with open(file, 'w') as f:
                    if write_into:
                        f.write(args.text)

                if args.verbose:
                    log_obj('File created', file)
                    if write_into:
                        log_obj(f'Contents written into {file}', args.text)

            except OSError as ex:
                ex_exit(ex, 1)


def log_obj(msg: str, obj: any) -> None:
    """Logs a message and an object to stdout."""
    sys.stdout.write(Fore.YELLOW + f'{msg}: ' +
                     Fore.CYAN + str(obj) + "\n")


def ex_exit(ex: BaseException, status_code: int = 1) -> NoReturn:
    """Logs an error on stderr the exits the program."""
    sys.stderr.write(Fore.YELLOW, "\n[CO] ",
                     Fore.RED, ex.__class__.__name__,
                     Fore.YELLOW, ": ", ex,
                     file=sys.stderr, sep='')
    sys.exit(1)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=Fore.YELLOW + "A barebones Python equivalent of the touch command in UNIX")

    parser.add_argument('file',
                        metavar='FILE',
                        type=str,
                        nargs='+',
                        help="File to create")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet',
                       action='store_true',
                       help='Do not notify if the file already exists')

    group.add_argument('-v', '--verbose',
                       action='store_true',
                       help='Notify upon successful file creation')

    parser.add_argument('-t', '--text',
                        metavar='TXT',
                        type=str,
                        help='Text to write into the created file',
                        required=False)

    return parser.parse_args()
