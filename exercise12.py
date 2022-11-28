#  Python coding challenge **12A "Perfect Number" is a number in which the sum of its factors 
# (excluding itself) are equal to itself.

'''Write a function that can verify if the given integer n is a perfect number, 
and return True if it is, or return False if not.

Example
n = 28 has the following factors: 1, 2, 4, 7, 14

1 + 2 + 4 + 7 + 14 = 28 therefore n = 28 is a perfect number, so you should return True.

n = 25 has the following factors: 1, 5, 25

1 + 5 = 6 therefore n = 25 is not a perfect number, so you should return False.'''
def perfect_number(n):
    k =0
    for num in range(1,int(n/2+1)):
        if n % num ==0:
            k += num      
    return k == n
print(perfect_number(28))
print(perfect_number(25))








