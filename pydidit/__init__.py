#!/usr/bin/env python

"""pydidit script to update idonethis topics

.. moduleauthor:: Valentine Gogichashvili <valgog@gmail.com>

"""

from __future__ import print_function, unicode_literals
import os
from textwrap import dedent
import click
import requests
import sys


class Config:
    """Config object represents the current configuration"""
    def __init__(self):
        # TODO: load all the needed envvars here and throw exception if they are not defined
        self.url = 'https://idonethis.com/api/v0.1'
        self.team = os.environ.get('DIDIT_TEAM')
        self.api_token = os.environ.get('DIDIT_API_TOKEN')


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
    message = message.strip()
    if message:
        click.echo("Sending to team ", nl=False)
        click.secho(config.team, nl=False, bold=True)
        click.echo(' ', nl=False)
        click.secho(message, fg='green')
        r = requests.post(
            config.url + '/dones/',
            json={'raw_text': message,
                  'team': config.team,
                  },
            headers={'Authorization': 'Token ' + config.api_token}
        )
        if r.status_code == requests.codes.created:
            click.secho('Done')
        else:
            click.secho('Could not post data {} {}'.format(r.status_code, r.text))


def get_user_for_api_token(config):
    r = requests.get(config.url + '/noop', headers={'Authorization': 'Token ' + config.api_token})
    if r.status_code == requests.codes.ok:
        result = r.json()
        return result['user']
    else:
        return None


@click.command()
@click.option('--team', type=str)
@click.option('--api-token', type=str)
@click.option('--test-api-token', is_flag=True)
@click.argument('done', nargs=-1)
@pass_config
def cli(config, team, api_token, test_api_token, done):
    config.team = team or config.team
    config.api_token = api_token or config.api_token
    if not config.team:
        click.secho('team should be defined', fg='red', err=True)
        sys.exit(1)
    if not config.api_token:
        click.secho('api token should be defined', fg='red', err=True)
        sys.exit(1)
    if test_api_token:
        user = get_user_for_api_token(config)
        if user:
            click.echo('Connected as user ', nl=False)
            click.secho(user, fg='green')
        else:
            click.secho('Could not connect using provided api token', fg='red', err=True)
    else:
        send(config, done)


if __name__ == '__main__':
    cli()

