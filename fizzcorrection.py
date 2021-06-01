for x in range(100):
    if x%3==0:
       print ("Fizz", x)
    
    elif x%5==0:
      print ("buzz",x)
    
    elif x%3==0 and x%5 == 0:
        
        print ("FizzBuzz",x)

    elif x%2==1:
          print ("odd number not a buzz or Fizz",x)
    