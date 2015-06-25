#!/usr/local/bin/python3
import time
import shelve
import click

DATABASE_FILE = 'data_points.db'
LOG_FILE = 'data_points.csv'

def write_entry(data_point, log):
    log.write('http://localhost:12345,' + str(data_point['was_up']) + ',' + str(data_point['response_time']) + '\n')

@click.command()
@click.option('--refresh', default=1.0, help='Seconds between checking data.')
def daemon(refresh):
    """A loop for data display"""
    database = shelve.open(DATABASE_FILE, flag='r')
    log = open(LOG_FILE, 'w')
    while True:
        index = 0
        previous_data_points = []
        while index < database['sample_size']:
            if str(index) not in database:
                break
            data_point = database[str(index)]
            if data_point not in previous_data_points:
                write_entry(data_point, log)
                previous_data_points.append(data_point)
            index += 1
        time.sleep(refresh)

if __name__ == '__main__':
    daemon()
