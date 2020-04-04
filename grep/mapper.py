#!/usr/bin/env python
"""mapper.py"""

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--start_with", default='k', type = str)
parser.add_argument("--end_with", default='e', type = str)
parser.add_argument("--contains", default='oo', type = str)
args = parser.parse_args()

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if word.startswith(args.start_with):
            print '%s\t%s' % (word, 1)
        elif word.endswith(args.end_with):
            print '%s\t%s' % (word, 1)
        elif args.contains in word:
            print '%s\t%s' % (word, 1)
        else:
            print '%s\t%s' % (word, 0)
