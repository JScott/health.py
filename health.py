#!/usr/local/bin/python3
import time
import shelve
import click
import httplib2

def initialize_database(file_name):
    """Set up the database connection"""
    database = shelve.open(file_name)
    if 'index' not in database:
        database['index'] = 0
    return database

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

def store(data, database):
    """Store the results in the given database connection"""
    data_point = {'was_up': data[0], 'response_time': data[1]}
    index = database['index']
    database[str(index)] = data_point
    print(index, ':', data_point)
    database['index'] = index + 1

@click.command()
@click.option('--interval', default=1.0, help='Seconds between pings.')
@click.option('--url', default="http://localhost:12345/", help='URL to ping.')
@click.option('--caching_enabled', is_flag=True, help='Are responses cached?')
def daemon(interval, url, caching_enabled):
    """A loop for health checking"""
    database = initialize_database('data_points.db')
    while True:
        data = check(url, caching_enabled)
        store(data, database)
        time.sleep(interval)

if __name__ == '__main__':
    daemon()
