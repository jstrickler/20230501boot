import re
import fileinput
from argparse import ArgumentParser

arg_parser = ArgumentParser(description="Faux Grep")

arg_parser.add_argument("-i", action="store_true", dest="ignore_case", help="Ignore case")
arg_parser.add_argument("-f", action="store_true", dest="show_filename", help="Show filenames")
arg_parser.add_argument("pattern", help="Pattern to find")
arg_parser.add_argument("filename", nargs="+", help="Files to search" )

args = arg_parser.parse_args()

# print(f"args: {args}")


pattern = re.compile(args.pattern, re.I if args.ignore_case else 0)

for raw_line in fileinput.input(args.filenames):
    if pattern.search(raw_line):
        line = raw_line.rstrip()
        if args.show_filename:
            print(fileinput.filename(), end=": ")
        print(line)