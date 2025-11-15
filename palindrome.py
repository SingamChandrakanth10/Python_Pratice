res = input("Enter Number : ")

"""Method-1 for palindrom"""
a = True;
for i in range(round(len(res) / 2)):
    print(f" Value : {i} , {res[i]} ")
    if(res[i] != res[len(res) - 1 - i] ):
        a = False

if(a):
    print("Its an palindorm")        
else:
    print("Its Not a palindorm")


""" Method-2 for palindorm"""
if(res == res[::-1]):
    print("Its an palindorm")        
else:
    print("Its Not a palindorm")