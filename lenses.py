#!/usr/bin/env python3.8

import logging
from argparse import ArgumentParser
from datetime import datetime, timedelta
from os import path

LOG_NAME = f"{path.dirname(path.abspath(__file__))}/lenses.log"
DATE_FORMAT = "%Y-%m-%d"


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        '--clear', '-c',
        action='store_true',
        help='clear lenses account log file',
    )
    parser.add_argument(
        '--date', '-d',
        help="date when lenses were used or unused (default: today)",
    )
    parser.add_argument(
        '--fill', '-f',
        action='store_true',
        help='option to set all unspecified dates between the first and the last dates as missed',
    )
    parser.add_argument(
        '--missed', '-m',
        action='store_true',
        help='option to specify that lenses were unused',
    )
    parser.add_argument(
        '--used', '-u',
        action='store_true',
        help='option to specify that lenses were used',
    )

    return parser.parse_args()


def init_logger():
    logging.basicConfig(
        filename=LOG_NAME,
        level=logging.INFO,
        format='%(message)s',
    )

    return logging.getLogger()


def clear_log():
    with open(LOG_NAME, 'w') as log:
        log.truncate(0)


def add_log_line(logger, date, msg):
    logger.info(f"{date}:{msg}")


def fill_log(logger):
    with open(LOG_NAME) as log:
        lines = [line.split(':') for line in log.read().splitlines()]
        lines.sort()

    item, count = 0, len(lines)

    while not item >= count - 1:
        if (datetime.strptime(lines[item + 1][0], DATE_FORMAT) - \
            (date := datetime.strptime(lines[item][0], DATE_FORMAT))
           ).total_seconds() > 60 * 60 * 24:
            lines.insert(item + 1, [(date + timedelta(1)).strftime(DATE_FORMAT), '0'])
        item += 1
        count = len(lines)

    clear_log()
    for date, result in lines:
        add_log_line(logger, date, result)


def account():
    total_used = 0
    with open(LOG_NAME) as log:
        for line in log.readlines():
            print(line, end="")
            total_used += int(line.split(':')[-1])

    if total_used:
        print('------------')
    print('USED:', total_used)


def main():
    args = parse_args()
    logger = init_logger()

    if args.clear:
        clear_log()

    if msg := '1' if args.used else '0' if args.missed else '':
        add_log_line(logger, args.date or datetime.now().strftime(DATE_FORMAT), msg)

    if args.fill:
        fill_log(logger)

    account()


if __name__ == '__main__':
    main()
