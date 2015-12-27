# divisibel by 3 say fizz
# divisible by 5 say buzz 
# divisible by both 3 and 5 say fizzbuzz

def fizzbuzz(number):
  if number % 5 == 0 and number % 3 == 0:
    return "Fizzbuzz"
  elif number % 5 == 0:
    return "Buzz"
  elif number % 3 == 0:
    return "Fizz"

#test code 
#print fizzbuzz(3)
#print fizzbuzz(5)
#print fizzbuzz(15)
