#!/usr/bin/env python3
# encoding: utf-8

import sys


def main():
    while True:
        data_in = input()

        if(data_in == '' or data_in == None):
            break

        data_in = data_in.split(' ')
        x = float(data_in[0])
        repeat = int(data_in[1])
        dot_old_index = str(x).find('.')
        dot_new_index = str(x).find('.')

        if len(str(x).split('.')[1]) != repeat:
            li = list(str(x).replace('.', ''))
            li.insert(len(li)-repeat, '.')
            x = ''.join(li)
            x = float(x)
            dot_new_index = str(x).find('.')

        x = float(str(x).split('.')[0]+ '.' + str(x).split('.')[1]*10)

        #print(dot_old_index, dot_new_index)

        #sys.exit(0)

        old_repeat = repeat
        repeat = 10 ** float(old_repeat)
        big_x = x * repeat

        big_x -= x
        repeat = round(repeat-1)

        big_x = round(big_x)

        #print(f'{big_x}/{repeat}')

        if dot_new_index - dot_old_index != 0:
            repeat *= 10 ** (dot_new_index - dot_old_index)

        smaller = 0
        if big_x < repeat:
            smaller = big_x
        else:
            smaller = repeat

        irreducible = ''

        #print(repeat)

        for i in range(1,smaller+1):
            if big_x % i == 0 and repeat % i == 0:
                irreducible = str(round(big_x/i)) + '/' + str(round(repeat/i))

        print(irreducible)

###################################

if __name__ == "__main__":
    main()