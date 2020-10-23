'''
Read two integer values (A and B). After, the program should print the message "Sao Multiplos"
(are multiples) or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

Input
The input has two integer numbers.

Output
Print the relative message to the input as stated above.
-----------
Input sample:
6 24

Output Sample:
Sao Multiplos
'''

a, b = input().split()

a = int(a)
b = int(b)

numbers = [a, b]
numbers.sort()

if numbers[1] % numbers[0] == 0:
    print ("Sao Multiplos")
else:
    print("Nao sao Multiplos")
