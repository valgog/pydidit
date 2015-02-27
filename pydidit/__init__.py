#!/usr/bin/env python

"""pydidit script to update idonethis topics

.. moduleauthor:: Valentine Gogichashvili <valgog@gmail.com>

"""

from __future__ import print_function, unicode_literals
from textwrap import dedent
import click


class Config:
    def __init__(self):
        self.team = None
        self.app_key = None


pass_config = click.make_pass_decorator(Config, ensure=True)


def get_message_from_editor():
    marker = dedent('''
        #
        # Enter the thing you just did.
        #
        # You can use '#' to hash some topics.
        #
        # Prefix your text with [] to send a goal.
        #
        ''')
    message = click.edit('\n\n' + marker)
    if message is not None:
        return message.split(marker, 1)[0].rstrip('\n')


def send(config, done):
    """Send your progress to idonethis.com"""
    if done:
        message = ' '.join(done).strip()
    else:
        message = get_message_from_editor()
    if message:
        click.echo("Sending to team {}: {}".format(config.team, message.strip()))


@click.command()
@click.option('--team', type=str, envvar='DIDIT_TEAM')
@click.argument('done', nargs=-1)
@pass_config
def cli(config, team, done):
    config.team = team
    send(config, done)

if __name__ == '__main__':
    cli()

