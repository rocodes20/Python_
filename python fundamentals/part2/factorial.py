
def factorial(n):
    if n < 0:
        print("error")
    fact = 1
    while n > 0:
        fact *= n 
        n-=1
    return fact

print(factorial(5))