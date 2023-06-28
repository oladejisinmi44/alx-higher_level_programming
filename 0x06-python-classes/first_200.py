#!/usr/bin/python3

def _isprime(n):
    j = n // 2
    if n == 2 or n == 3 or n == 5:
        return True
    if n == 4:
        return False
    for i in range(2, j):
        if n % i == 0:
            return False
    return True



def main():
    n = 2
    count = 0
    while True:
        if _isprime(n):
            print(n, end="")
            count += 1
            if count == 200:
                break
            else:
                print(", ", end="")
        n += 1

main()
