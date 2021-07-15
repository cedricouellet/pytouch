"""pytouch.helpers: Helper functions and classes for the main pytouch program."""


from os import path


def create_and_write_into(file: str, text: str) -> None:
    """Creates a file then writes text into it"""
    f = open(file, 'w')
    if text:
        f.write(text)
    f.close()


def file_exists(file: str) -> bool:
    """Determines if a file exists or not"""
    return path.exists(file)
