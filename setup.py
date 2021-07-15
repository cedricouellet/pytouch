"""setup.py: setuptools control."""


from re import search, M
from setuptools import setup


version = search(
    '^__version__\s*=\s*"(.*)"',
    open('pytouch/pytouch.py').read(),
    M
).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="pytouch-cli",
    packages=["pytouch"],
    entry_points={
        "console_scripts": ['pytouch = pytouch.pytouch:main']
    },
    version=version,
    description="A Python tool similar to UNIX's touch.",
    long_description=long_descr,
    author="cedricao",
    author_email="cedricao.noreply@gmail.com",
    url="https://github.com/cedricouellet/pytouch.git"
)
