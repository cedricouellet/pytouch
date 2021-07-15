# pytouch
A Python tool similar to UNIX's touch.

To run the program, use `pytouch-runner.py`.
Since it is configured as a pip package, it is not possible to run files individually.
To install the dist version, use `pip install pytouch-cli`
Then, all you have to do is write `pytouch` into your terminal.

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
