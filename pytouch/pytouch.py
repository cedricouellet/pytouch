"""pytouch.pytouch: provides entry point main()."""

__version__ = "0.3.0"

from .helpers import create_and_write_into, file_exists
from sys import stderr, exit
from typing import NoReturn
from argparse import Namespace, ArgumentParser

import colorama
from colorama import Fore

colorama.init()


def main() -> None:
    """The main function of the script"""
    args = parse_args()

    for file in args.file:
        if file_exists(file):
            if not args.quiet:
                warn_file('The file already exists', file)
        else:
            try:
                create_and_write_into(file, args.text)
                if args.verbose:
                    print(Fore.RESET + 'File created: ' + Fore.CYAN + file)
            except OSError as ex:
                ex_exit(ex, 1)


def warn_file(msg: str, file: str) -> None:
    """Logs a message containing information about a file interaction, and the file itself."""
    print(Fore.YELLOW + msg + ': ' + Fore.CYAN + file)


def ex_exit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Logs an error to the console and ends the program."""
    print(Fore.YELLOW, "\n[CO] ", Fore.RED, ex.__class__.__name__, Fore.YELLOW, ": ", ex, file=stderr, sep='')
    exit(exit_code)


def parse_args() -> Namespace:
    """Parse command line arguments."""
    parser = ArgumentParser(
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
