#!/usr/bin/env python3.8

import logging
from argparse import ArgumentParser
from datetime import datetime

LOG_NAME = "lenses.log"
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
        '--used', '-u',
        action='store_true',
        help='option to specify that lenses were used',
    )
    parser.add_argument(
        '--missed', '-m',
        action='store_true',
        help='option to specify that lenses were unused',
    )

    return parser.parse_args()


def init_logger():
    logging.basicConfig(
        filename=LOG_NAME,
        level=logging.INFO,
        format='%(message)s',
    )

    return logging.getLogger()


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
        with open(LOG_NAME, 'w') as config:
            config.truncate(0)

    if msg := '1' if args.used else '0' if args.missed else '':
        logger.info(
            ':'.join([args.date or datetime.now().strftime(DATE_FORMAT), msg])
        )

    account()


if __name__ == '__main__':
    main()
