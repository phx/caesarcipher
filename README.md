# Caesar Cipher
This is code that I modified from a couple of examples in a book to make it more useful.
It takes `STDIN` as input.  Except for the bruteforce method, it also allows for case-sensitivity.

In the case of bruteforce, you can usually see the shift used, then pipe the original message in with `echo [message] | ./caesar.py [shift] -d` in order to re-obtain the original case-sensitivity.

### Usage:

`./caesar.py <[# OF SHIFTS] [-e|-d]> | <[--brute]>`

### Examples

`echo 'stuff to encrypt' | ./caesar.py 11 -e`

`echo 'DEFQQ EZ PYNCJAE' | ./caesar.py 11 -d`

`cat decrypted_file.txt | ./caesar.py 3 -e`

`./caesar.py 3 -d < encrypted_file.txt`

`echo 'DEFQQ EZ PYNCJAE' | ./caesar.py --brute`

