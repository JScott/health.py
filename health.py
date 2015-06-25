#!/usr/local/bin/python3
import time
import shelve
import click
import httplib2

URL = 'http://localhost:12345/'
DATABASE_FILE = 'data_points.db'

def initialize_database(file_name, sample_size):
    """Set up the database connection"""
    database = shelve.open(file_name, flag='w')
    if 'index' not in database:
        database['index'] = 0
    database['sample_size'] = sample_size
    return database

def increment_index(database, sample_size):
    database['index'] += 1
    if database['index'] >= sample_size:
        database['index'] = 0

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

def store(data, database, sample_size):
    """Store the results in the given database connection"""
    data_point = {'was_up': data[0], 'response_time': data[1]}
    current_index = database['index']
    database[str(current_index)] = data_point
    print(current_index, ':', data_point)
    increment_index(database, sample_size)

@click.command()
@click.option('--interval', default=1.0, help='Seconds between pings.')
@click.option('--caching_enabled', is_flag=True, help='Are responses cached?')
@click.option('--sample_size', default=10, help='The max data point count.')
def daemon(interval, caching_enabled, sample_size):
    """A loop for health checking"""
    database = initialize_database(DATABASE_FILE, sample_size)
    while True:
        data = check(URL, caching_enabled)
        store(data, database, sample_size)
        time.sleep(interval)

if __name__ == '__main__':
    daemon()
