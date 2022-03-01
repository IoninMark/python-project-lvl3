#!/usr/bin/env python3
import argparse
import os
from page_loader.html_loader import download


def main():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('--output',
                        dest='output',
                        default=os.getcwd(),
                        help='path to output directory')
    parser.add_argument('url_to_load')
    args = parser.parse_args()
    # default_path = os.path.abspath(__file__)
    print(download(args.url_to_load, args.output))

if __name__ == '__main__':
    main()
