# Caesar Cipher
This is code that I modified from an example in a book to make it more useful.

Takes STDIN as input.

###Usage:
`./caesar.py [NUMBER OF SHIFTS] [-e|-d]`

###Examples
`echo 'stuff to encrypt' | ./caesar.py 11 -e`

`echo 'DEFQQ EZ PYNCJAE' | ./caesar.py 11 -d`

`cat decrypted_file.txt | ./caesar.py 3 -e`

`./caesar.py 3 -d < encrypted_file.txt`

