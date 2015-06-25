#!/usr/local/bin/python3
import time
from os import system
import shelve
import click
from prettytable import PrettyTable

DATABASE_FILE = 'data_points.db'

def write_row(table, data_point):
    row = [data_point['was_up'], data_point['response_time']]
    table.add_row(row)

@click.command()
@click.option('--refresh', default=1.0, help='Seconds between checking data.')
def daemon(refresh):
    """A loop for data display"""
    database = shelve.open(DATABASE_FILE, flag='r')
    while True:
        table = PrettyTable(["Was it up?", "Response time"])
        index = up_count = 0
        while index < database['sample_size']:
            if str(index) not in database:
                break
            data_point = database[str(index)]
            write_row(table, data_point)
            up_count += 1 if data_point['was_up'] else 0
            index += 1
        system('clear')
        print(table)
        print('Availability score:', (up_count/database['sample_size']))
        time.sleep(refresh)

if __name__ == '__main__':
    daemon()
