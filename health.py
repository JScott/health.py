#!/usr/local/bin/python3

import click

@click.command()
@click.option('--frequency', default=1, help='Seconds between pings.')
@click.option('--url', default="localhost:12345", help='URL to ping.')

def check(frequency, url):
    """The worst health checker"""
    print(frequency)
    print(url)

if __name__ == '__main__':
    check()
