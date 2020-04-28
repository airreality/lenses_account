# Lenses account

## How to use

```
usage: lenses.py [-h] [--clear] [--date DATE] [--used] [--missed]

optional arguments:
  -h, --help            show this help message and exit
  --clear, -c           clear lenses account log file
  --date DATE, -d DATE  date when lenses were used or unused (default: today)
  --used, -u            option to specify that lenses were used
  --missed, -m          option to specify that lenses were unused
```

## Example of log file:
```
$ lenses
2020-04-20:1
2020-04-21:1
2020-04-22:1
2020-04-23:0
2020-04-24:1
2020-04-25:1
2020-04-26:0
2020-04-27:0
2020-04-28:1
2020-04-29:1
------------
USED: 7

```
