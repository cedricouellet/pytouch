# pytouch
A Python tool similar to UNIX's touch.
For those unlucky enough Windows users that don't have WSL and don't want to use `echo < <filename>` to create files.

## Execution
- Source
  
  Run `pytouch-runner.py`, it is a wrapper for running pytouch directly from source tree.

- Dist
  1. `pip install pytouch-cli`
  2. `pytouch`

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
