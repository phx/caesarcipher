# Caesar Cipher
This is code that I modified from a couple of examples in a book to make it more useful.
It takes `STDIN` as input.

### Usage:

`./caesar.py <[# OF SHIFTS] [-e|-d]> | <[--brute]>`

### Examples

`echo 'stuff to encrypt' | ./caesar.py 11 -e`

`echo 'DEFQQ EZ PYNCJAE' | ./caesar.py 11 -d`

`cat decrypted_file.txt | ./caesar.py 3 -e`

`./caesar.py 3 -d < encrypted_file.txt`

`echo 'DEFQQ EZ PYNCJAE' | ./caesar.py --brute`

