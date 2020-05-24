# Lenses account

## How to use

```
usage: lenses.py [-h] [--clear] [--date DATE] [--fill] [--missed] [--used]

optional arguments:
  -h, --help            show this help message and exit
  --clear, -c           clear lenses account log file
  --date DATE, -d DATE  date when lenses were used or unused (default: today)
  --fill, -f            option to set all unspecified dates between the first
                        and the last dates as missed
  --missed, -m          option to specify that lenses were unused
  --used, -u            option to specify that lenses were used
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
