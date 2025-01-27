"""阿拉伯数字转中文数字"""

import argparse

from .core import Mode, convert


def main():
    parser = argparse.ArgumentParser(prog=__package__, description=__doc__)
    parser.add_argument("number", type=str, help="阿拉伯数字")
    parser.add_argument("-m", "--mode", type=str, default="low")

    args = parser.parse_args()
    # print(args)
    # return

    number: str = args.number
    mode: Mode = args.mode
    try:
        ret = convert(number, mode)
        print(f"MODE: {mode}")
        print(f"{number} --> {ret}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
