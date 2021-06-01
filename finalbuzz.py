
#day one 30 days of codefor x in range (1,100):
    if x > 1:
        for i in range(2,x):
            if x%i == 0:
                break
        else:
                print(x)