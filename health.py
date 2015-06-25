#!/usr/local/bin/python3
import time
import click
import httplib2

def is_valid(utf8_content):
    """Was the request fulfilled as expected?"""
    return 'Magnificent!' in utf8_content.decode("utf-8")

def request(url):
    """Send a GET request to the given URL"""
    http = httplib2.Http(".cache")
    return http.request(url, "GET")

def check(url):
    """Check the URL for server health"""
    response, content = request(url)
    return is_valid(content)

@click.command()
@click.option('--frequency', default=1.0, help='Seconds between pings.')
@click.option('--url', default="http://localhost:12345/", help='URL to ping.')
def daemon(frequency, url):
    """A loop for health checking"""
    while True:
        start = time.time()
        is_up = check(url)
        seconds_elapsed = time.time() - start
        print(is_up, seconds_elapsed)
        time.sleep(frequency)

if __name__ == '__main__':
    daemon()
