#!/usr/bin/env python3
"""
Author : amedeiros <amedeiros@localhost>
Date   : 2023-02-04
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        help='name to greet',
                        metavar='name',
                        type=str,
                        default='World')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    name = args.name
    print(f'Hello, {name}!')
# --------------------------------------------------
if __name__ == '__main__':

    main()
    