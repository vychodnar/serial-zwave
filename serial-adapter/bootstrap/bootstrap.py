"""bootstrap.bootstrap: provides entry point main()."""

import sys
import click
from .stuff import Stuff

__version__ = "0.0.1"

@click.group()
def main():
    pass
#    print("Executing bootstrap version %s." % __version__)
#    print("List of argument strings: %s" % sys.argv[1:])
#    print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))

@click.command()
def hello():
    print("Hello World!")
    print("Executing bootstrap version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))

main.add_command(hello)

class Boo(Stuff):
    pass