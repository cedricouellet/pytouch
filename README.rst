***********
pytouch-cli
***********

A Python tool similar to UNIX's touch.
######################################

::

 usage: pytouch [-h] [-q | -v] [-t TXT] FILE [FILE ...]
    A barebones Python equivalent of the touch command in UNIX
    positional arguments:
      FILE                File to create
    optional arguments:
      -h, --help          show this help message and exit
      -q, --quiet         Do not notify if the file already exists
      -v, --verbose       Notify upon file creation
      -t TXT, --text TXT  Text to store inside the created file

