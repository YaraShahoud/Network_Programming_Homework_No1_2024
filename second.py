# binary to decimal
def binaryToDecimal(n):
    number = n;
    decimal_value = 0;#inal decimal number
     
    # Initializing base 
    # value to 1, i.e 2 ^ 0
    base = 1;#2^base for example bit zero has 2^0=1
     
    len1 = len(number);#get length of number
    for i in range(len1 - 1, -1, -1):#loop number from reight to left
        if (number[i] != '1') and (number[i] != '0'): #if digit is not 1 and not 0 print error and exit    
            print("Wrong Binary number");
            exit();
        if (number[i] == '1'): #if digit is 1 multiply it by 2 ^ base    
            decimal_value += base;#add it to final decimal
        base = base * 2;#update base value
     
    return decimal_value;#return final number
 
# Test Code
number = str(input("Enter the binary number:"))  #ask user to input binary number
print(binaryToDecimal(number));