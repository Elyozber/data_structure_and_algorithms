"""An algorithm that returns the sum of two numbers"""
# 1.Start
# 2.We create the variables x, y and sum
# 3.We load or accept values for the variables x and y
# 4.We load their sum into the sum variable:
#     sum=x+y
# 5.Return the value in the sum variable
# 6.Stop

def first_algorithm(x,y):
    sum=x+y
    return sum

print(first_algorithm(657, 657))
print(first_algorithm(3254,345234))
print(first_algorithm(6,4))


"""An algorithm that returns the largest of the three numbers"""
# 1.Start
# 2.We can create variables a, b, and c
# 3.We load values on them
# 4.If a>b:
#     if a>c:
#         We return a as the largest value
#     else (a<c):
#         We return c as the largest value
# 5.Else (a<b):
#              if b>c:
#                 We return b as the largest value
#              else (b<c):
#                 We return c as the largest value
                        
def second_algorithm(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
        
print(second_algorithm(1,2,3))
print(second_algorithm(3,6,1))
print(second_algorithm(2,1,0))

"""N factorial return algorithm"""
# 1.Start
# 2.We create the variables n, factorial, and i
# 3.We load the value of 1 on the factorial and i variables
#     factorial = 1,i = 1
# 4.Operations are performed up to i = N:
#     factorial = factorial * i
#     i = i+1
# 5.return the factorial value

def factorial(N):
    faktorial = 1
    i = 1
    while True:
        if i==N+1:
            break
        else:
            faktorial = faktorial*i
            i = i+1
    return faktorial

print(factorial(5))