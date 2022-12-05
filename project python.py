#                                           Project 19: [Roll numbers:62,63,64]
#                                          Arman Soni          12206043       62
#                                          Diwakar Sharma      12206055       63
#                                          Sachin Yaduwanshi   12206059       64
'''
Your task is to write a program to find the nth prime palindrome number, n is the input user 
will give.
A prime number, such as 127, has no factors other than itself and one. A palindrome, such as 
121, is the same number when its digits are reversed. A prime palindrome, such as 131, is both 
prime and a palindrome. 
'''
n=int(input("enter the place value of prime-palindrome number: "))
a=[]
for i in range(n*1000):
    if(i==1 or i==0):
        continue
    else:
        for j in range(2,i):
            if(i%j==0 ):
                break
        else:
            p=i
            r=0
            while i>0:#121,12,1
                r=r*10+(i%10)#1,12,121
                i=i//10
            if(r==p):
                a.append(r)
            else:
                pass
print("the list of prime-palindrome numbers : {} ".format(a))
print("The {}th prime-palindrome number is : {}".format(n,a[n-1]))






