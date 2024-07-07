"""阿拉伯数字转中文数字"""

import argparse

from .core import Mode, convert


def main():
    parser = argparse.ArgumentParser(prog=__package__, description=__doc__)
    parser.add_argument('number')
    parser.add_argument('-m', '--mode', type=Mode, choices=Mode, default=Mode.LOW)

    args = parser.parse_args()
    print(args)
    # return

    number: str = args.number
    mode: Mode = args.mode
    ret = convert(number, mode)
    print(f'MODE: {mode}')
    print(f'{number} --> {ret}')
