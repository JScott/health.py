#!/usr/local/bin/python3
import time
import click
import httplib2

def is_valid(utf8_content):
    """Was the request fulfilled as expected?"""
    return 'Magnificent!' in utf8_content.decode("utf-8")

def request(url, caching_enabled):
    """Send a GET request to the given URL"""
    http = httplib2.Http(".cache")
    headers = {} if caching_enabled else {'cache-control':'no-cache'}
    return http.request(url, "GET", headers=headers)

def check(url, caching_enabled):
    """Check the URL for server health"""
    start = time.time()
    response, content = request(url, caching_enabled)
    seconds_elapsed = time.time() - start
    return (is_valid(content), seconds_elapsed)

@click.command()
@click.option('--frequency', default=1.0, help='Seconds between pings.')
@click.option('--url', default="http://localhost:12345/", help='URL to ping.')
@click.option('--caching_enabled', is_flag=True, help='Are responses cached?')
def daemon(frequency, url, caching_enabled):
    """A loop for health checking"""
    while True:
        is_up, response_time = check(url, caching_enabled)
        print(is_up, response_time)
        time.sleep(frequency)

if __name__ == '__main__':
    daemon()
