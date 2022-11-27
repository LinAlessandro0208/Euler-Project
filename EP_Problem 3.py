"""
Problem 3 Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
import math
#test = 13195
test = 600851475143
test_2 = int(round(math.sqrt(test)))        #Round to the nearest integer

i=2
while i * i < test:
    while test%i == 0:
        test = test / i
    i = i + 1
print (test)
