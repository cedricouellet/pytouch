# pytouch
A Python tool similar to UNIX's touch.

For those unlucky enough Windows users that don't have WSL and don't want to use `echo > {filename}` to create files.

## Execution

### Source

Run `pytouch-runner.py`, it is a wrapper for running pytouch directly from root directory.

### Dist

1. In a terminal, call `pip install pytouch-cli` in order to download the build from PyPi.org

2. Call `pytouch` to execute the script 

For help, use `pytouch -h` or `pytouch --help`.

## Usage
```
usage: pytouch [-h] [-q | -v] [-t TXT] FILE [FILE ...]

A barebones Python equivalent of the touch command in UNIX
positional arguments:
  FILE                File to create
optional arguments:
  -h, --help          show this help message and exit
  -q, --quiet         Do not notify if the file already exists
  -v, --verbose       Notify upon file creation
  -t TXT, --text TXT  Text to store inside the created file
```
