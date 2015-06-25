#!/usr/local/bin/python3

import click
import httplib2

def is_healthy(utf8_content):
    """Was the request fulfilled as expected?"""
    return 'Magnificent!' in utf8_content.decode("utf-8")

def request(url):
    """Send a GET request to the given URL"""
    http = httplib2.Http(".cache")
    return http.request(url, "GET")

@click.command()
@click.option('--frequency', default=1, help='Seconds between pings.')
@click.option('--url', default="http://localhost:12345/", help='URL to ping.')
@click.option('--timeout', default=10, help='Seconds to wait for a response.')
def check(frequency, url, timeout):
    """Not a great health checker"""
    response, content = request(url)
    if is_healthy(content):
        print("good!")
    else:
        print("bad!")

if __name__ == '__main__':
    check()
