import math

if __name__ == "__main__":
    
    a, b = map(int, input().split())
    
    print(math.gcd(a, b))
    print((a * b) // math.gcd(a, b))