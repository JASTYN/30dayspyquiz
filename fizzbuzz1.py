#day one 30 days of code
# Typical loop
for i in range(1,65):
  if i%3 == 0 and i%5 == 0:
    print("FizzBuzz")  
  elif i%3 == 0:
    print("Fizz")
  elif i%5 == 0:
    print("Buzz")
  else:
    print(i)
 
# Interesting list comprehension
# using string concatenation
[print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i) 
  for i in range(65)]
