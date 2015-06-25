#!/usr/local/bin/python3
import time
import click
import httplib2

def is_healthy(utf8_content):
    """Was the request fulfilled as expected?"""
    return 'Magnificent!' in utf8_content.decode("utf-8")

def request(url):
    """Send a GET request to the given URL"""
    http = httplib2.Http(".cache")
    return http.request(url, "GET")

def check(url, timeout):
    """Check the URL for server health"""
    response, content = request(url)
    if is_healthy(content):
        print("good!")
    else:
        print("bad!")

@click.command()
@click.option('--frequency', default=1.0, help='Seconds between pings.')
@click.option('--url', default="http://localhost:12345/", help='URL to ping.')
@click.option('--timeout', default=1.0, help='Seconds to wait for a response.')
def daemon(frequency, url, timeout):
    """A loop for health checking"""
    while True:
        check(url, timeout)
        time.sleep(frequency)

if __name__ == '__main__':
    daemon()
