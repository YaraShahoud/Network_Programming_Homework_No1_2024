#Define Factorial function that is 1 if number is 0 or 1 or n * n-1 * n-2 ... else
def factorial(n):

    # Recursive way to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 

number = int(input("Enter the number:"))  #ask user to input number
f = factorial(number)  #cal function to calculate factorial
print("The Factorial of", number, "is: ", f)  #print result to user