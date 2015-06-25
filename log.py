#!/usr/local/bin/python3
import time
import shelve
import click

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
        index = 0
        previous_data_points = {}
        while index < database['sample_size']:
            if str(index) not in database:
                break
            data_point = database[str(index)]
            
            index += 1
        system('clear')
        print(previous_data_points)
        time.sleep(refresh)

if __name__ == '__main__':
    daemon()
