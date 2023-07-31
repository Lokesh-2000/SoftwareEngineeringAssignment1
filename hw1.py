# Title : Fermat's Last Theorem Near Misses
# Filename : hw1.py
# Necessary Files :
# Created Files : hw1.exe : executable file in windows platform
# Name : Lokesh Gupta
# Email : LokeshGupta@lewisu.edu
# Course and Sections : SU23-CPSC-60500-001
# Date : 28/07/2023
# Explanation : This program helps to search for near misses
# of the form (x, y, z, n, k) in the formula x^n + y^n = z^n, where x, y, z, n, k
# are positive integers, where 2< n <12, where 10 <= x <= k, and where 10 <= y <= k
# Language : Python 3.10.3

def calculate_miss(n, k):
    
    # Calculate near misses of the formula of Fermat's Last Theorem

    miss_min = -1 # value is -1 at first initialization
    for x in range(10, k): # Outer loop for first variable x
        for y in range(10, k): # loop for y variable
            xysum_pow = pow(x, n) + pow(y, n) # calculate (x^n + y^n)
            z = int(pow(xysum_pow, 1/n))
            z_pow = pow(z, n)
            z1_pow = pow(z+1, n)
            miss = min( xysum_pow - z_pow, z1_pow - xysum_pow) # get the miss which is minimum value
            relative_miss = miss / xysum_pow
            if miss_min==-1:
                miss_min = relative_miss # for the first iteration get the relative miss
                print("\nx : {}   |   y : {}   |   z : {}    |   Miss : {}   |   Relative Miss : {}%".format(x, y, z, miss, round(miss_min*100,2)))
            else:
                if relative_miss < miss_min: 
                    miss_min = relative_miss # get the minimum relative miss
                    print("x : {}   |   y : {}   |   z : {}    |   Miss : {}   |   Relative Miss : {}%".format(x, y, z, miss, round(miss_min*100,2)))
    print("Final Result")
    # show the final result
    print("x : {}   |   y : {}   |   z : {}    |   Miss : {}   |   Relative Miss : {}%".format(x, y, z, miss, round(miss_min*100, 2)))
    
        
if __name__ == "__main__":
    # take input and call the calculate function

    n = int(input("Exponent value : "))
    while(n>11 or n<3):
        # check if n is bigger than 2
        n = int(input("Exponent value is between 2 and 12 : "))
    k = int(input("Limit value : "))
    while(k<11):
        # check if k is bigger than 10
        k = int(input("Limit value bigger than 10 : "))
    calculate_miss(n,k)
    s = input("Enter for exit.")