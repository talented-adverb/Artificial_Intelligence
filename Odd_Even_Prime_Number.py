#Q1

# def series():
#     sum=0
#     x=int(input("Enter a x"))
#     n=int(input("Enter a n"))
#     sum=1
#     for i in range(1,1+n):
#         sum+=sum*(x/i)
#     return sum

# print(series())

#Q2

import random

def randomList():
    list=[]
    Length=int(input("Enter the Length of the list"))
    for i in range(Length):
        list.append(random.randint(100,900)) 
    print(list)
    return  list

def odd_Even_prime_no_list():
    oddlist=[]
    evenlist=[]
    primelist=[]
    for i in randomList():
        if(i%2==0):
            evenlist.append(i)
        else:
            oddlist.append(i)
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            primelist.append(i)
    print(oddlist)
    print(evenlist)
    print(primelist)

print(odd_Even_prime_no_list())


            
    