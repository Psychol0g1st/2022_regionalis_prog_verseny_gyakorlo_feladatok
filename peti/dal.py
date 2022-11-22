#!/usr/bin/env python3
# encoding: utf-8

import sys


def main():
    for line in sys.stdin:
        s = list(line)

        alpha = False

        i = 0
        while i < len(s):
            if not alpha and s[i].isalpha():
                s.insert(i, '"')
                # i += 1
                alpha = True

            elif alpha and not s[i].isalpha():
                s.insert(i, '"')
                # i += 1
                alpha = False

            elif alpha and i == len(s) - 1:
                s.append('"')
                alpha = False
            i += 1

        print(eval("".join(s)))


if __name__ == "__main__":
    main()
