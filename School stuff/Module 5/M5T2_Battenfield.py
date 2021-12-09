"""
CSC-221
M5T2 - Recursion Info (done in class)
Elizabeth Battenfield
11/15/2021

Program shows off recursion as per 11.1-11.5
"""

def iterativeFactorial(number):
    print("Iterative factorial")
    factorial = 1
    for number in range(number, 0, -1): # for 5!
        factorial *= number
        # so... 5*4*3*2*!
    print("5! =",factorial)
    
def factorial(number):
    """ "Recursion is calling the functoin i'm in"
    recursively finding factorial works
    because each step builds on the next.
    ex: 2! = 2 *1
        3! = 3*2*1 or 3 *2!, etc.    
    """
    #print("\tfactorial(",number,") is", number, " times...")
    if number <=1: #base case
        #print("\t\tfactorial(1) is just 1.")
        return 1 # 1! and 0! are defined as 1
    #recursive base
    return number * factorial(number -1)

def infiniteRecursion():
    """ i really hope you guyes dont do this (XD)"""
    print("We're still going...", end=" ")
    infiniteRecursion()

def fibonacci(n):
    #slower but very easy to follow
    if n in (0,1): #base cases
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
 
def iterative_fibonacci(n) :
    #fast, but who wants to explain this one?
    result = 0
    temp =1
    for j in range(0,n):
        temp, result = result, result +temp
    return result

def memoFib(n):
    """
    Use "memoizatoin" to speed up the recursive method
    while keeping it easy to follow
    """
    fibList = [0, 1] #store all our previous answers
    
    def fib(num):
        """
        yes, this is a function inside a function
        """
        if num < len(fibList):
            return fibList[num] + fibList[num-1]
        else:
            newFib = fib(num-1) + fib(num-2)
            fibList[num] = newFib #save for later
            return newFib
    
# #gave up and got it from stack overflow #DOESNT WORK 
# #https://stackoverflow.com/questions/29570870/memoization-fibonacci-algorithm-in-python
# def fastFib(n, memo):
#     global numCalls
#     numCalls += 1
#     print ('fib1 called with', n)
#     if not n in memo:
#         memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
#     #this should be outside of the if clause:
#     return memo[n] #<<<<<< THIS

def main():
    # factoral examples
    #iterativeFactorial(5)
    #print("5! recursive =", factorial(5))
    
    #infiniteRecursion() #turned off so program will run, and not exceed the recursion depth
    #print("50! recursive = ", factorial(50))
    
    # fibonacci series examples
    for n in range(35): #example, 0 to 40
        print(f'Fibonacci({n}) = {fibonacci(n)}') #takes forever to finish after 35
    print("Iterative:")
    for n in range(35): #example, 0 to 40
        print(f'Fibonacci({n}) = {iterative_fibonacci(n)}')
    # print("With Memoization")
    # memo = []
    # for n in range(35): #example, 0 to 40
    #     print(f'Fibonacci({n}) = {fastFib(n)}') #DOESNT WORK
    
    
    
if __name__ == "__main__":
    main()
    
    
    
    