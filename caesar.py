#!/usr/bin/env python3
####################################################################
# Copyright (C) 2020 phx <https://github.com/phx>
# This is an updated version of the original Caesar Cipher code from
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# All code changes made by phx.
# This is currently under development to be cleaned up.
####################################################################
import sys

mode = None

# The encryption/decryption key:
if len(sys.argv) < 1:
    key = 0
    # print('shift:' + str(key) + '\n')
    mode = 'decrypt'
elif '--brute' in sys.argv:
    mode = 'bruteforce'
else:
    key = int(sys.argv[1])
    # print('shift: ' + str(key) + '\n')

# Whether the program encrypts or decrypts:
if len(sys.argv) > 2:
    if '-d' in sys.argv[2]:
        mode = 'decrypt'
    elif '-e' in sys.argv[2]:
        mode = 'encrypt'
    elif '--brute' not in sys.argv:
        print("Must include either '-e' or '-d' flags")
        raise SystemExit
    else:
        key = int(sys.argv[1])
        mode = 'decrypt'

# Every possible symbol that can be encrypted:
SPECIAL = '.,;:\'"<>[]{}|\\/+-=()*&^%$#@!?`~_ 	\n\t\r'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The string to be encrypted/decrypted:
# input = [x.replace('\n', ' ') for x in sys.stdin.readlines()]
if len(sys.argv) >= 4:
    print('This program only takes input from STDIN.')
    raise SystemExit
else:
    input = [x for x in sys.stdin.readlines()]


def docipher():
    output = []
    # Stores the encrypted/decrypted form of the message:
    global translatedIndex
    translated = ''
    for i, _ in enumerate(input):
        message = list(input[i])
        for symbol in message:
            symbol = symbol.upper()
            # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
            if SPECIAL.find(symbol) == True:
                output.append(symbol)
            elif symbol in SYMBOLS:
                # Perform encryption/decryption:
                symbolIndex = SYMBOLS.find(symbol)
                if mode == 'encrypt':
                    translatedIndex = symbolIndex + key
                elif mode == 'decrypt':
                    translatedIndex = symbolIndex - key
                elif mode == 'bruteforce':
                    translatedIndex = symbolIndex - key

                # Handle wrap-around, if needed:
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                output.append(translated)
                translated = translated + SYMBOLS[translatedIndex]
            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol
                output.append(translated)
        if mode == 'bruteforce':
            # Output the translated string:
            output = output[len(output) - 1].strip()
            # Display every possible decryption:
            print('Shift ' + str(key).zfill(2) + ':', output)
            output = []
            translated = ''
        else:
            # Output the translated string:
            output = output[len(output) - 1].strip()
            output_list = []
            for c, _ in enumerate(output):
                if message[c].isupper():
                    output_list.append(output[c].upper())
                else:
                    output_list.append(output[c].lower())
            #print(output_list)
            #print(output)
            print(''.join(output_list))


if __name__ == '__main__':
    if mode == 'bruteforce':
        for key in range(len(SYMBOLS)):
            docipher()
    else:
        docipher()
