"""bootstrap.bootstrap: provides entry point main()."""

import sys
import click
import pika
from .stuff import Stuff

__version__ = "0.0.1"

@click.version_option(version=__version__)

@click.group()
def main():
    """Testor"""
    pass
#    print("Executing bootstrap version %s." % __version__)
#    print("List of argument strings: %s" % sys.argv[1:])
#    print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))

@click.command()
def hello():
    """Hello World command"""
    print("Hello World!")
    print("Executing bootstrap version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))


@click.command()
def run():
    """Run the command"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', type='fanout')
    #message = ' '.join(sys.argv[1:])
    message = "info: Hello World!"
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    connection.close()


main.add_command(hello)
main.add_command(run)


class Boo(Stuff):
    pass
