"""bootstrap.bootstrap: provides entry point main()."""

import sys
from .stuff import Stuff

__version__ = "0.0.1"

def main():
    print("Executing bootstrap version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))


class Boo(Stuff):
    pass