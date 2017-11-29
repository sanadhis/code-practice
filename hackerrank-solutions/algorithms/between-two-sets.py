#!/bin/python3

import sys

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def getTotalX(a, b):
    gcdB = min(b)
    lcmA = min(a)
    gcdA = min(a)
    
    for i in a:
        lcmA = lcm(lcmA,i)
    
    for i in b:
        gcdB = gcd(gcdB,i)
        
    for i in a:
        gcdA = gcd(gcdA,i)
    
    result = 0
    for i in range(lcmA,gcdB+1,gcdA):
        if i%lcmA == 0 and gcdB%i == 0:
            result += 1
    return result
        
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
