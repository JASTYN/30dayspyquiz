#day one 30 days of code
#write a program to print all prime numbers from 1-10


for x in range(1, 10):
    if x > 1:
        for i in range(2,x):
            if(x%i==0):
                break
        else:
            print(x)