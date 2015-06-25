#!/usr/local/bin/python3
import time
import sys
import shelve
import click
from prettytable import PrettyTable

DATABASE_FILE = 'data_points.db'

def write(database, table):
    index = 0
    while index < database['sample_size']:
        if str(index) not in database:
            break
        data_point = database[str(index)]
        row = [data_point['was_up'], data_point['response_time']]
        table.add_row(row)
        index += 1

@click.command()
@click.option('--refresh', default=1.0, help='Seconds between checking data.')
def daemon(refresh):
    """A loop for data display"""
    database = shelve.open(DATABASE_FILE, flag='r')
    while True:
        table = PrettyTable(["Was it up?", "Response time"])
        write(database, table)
        sys.stdout.flush()
        print(table)

if __name__ == '__main__':
    daemon()
