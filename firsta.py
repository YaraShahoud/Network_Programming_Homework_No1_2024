# initializing lists
L1 = ["HTTP", "HTTPS", "FTP", "DNS"]
L2 = [80, 443, 21, 53]

# Printing original keys-value lists
print("Original L1 list is : " + str(L1))
print("Original L2 list is : " + str(L2))

# using dictionary comprehension
# to convert lists to dictionary
res = {L1[i]: L2[i] for i in range(len(L1))}

# Printing resulting dictionary
print("d  =  " + str(res))
