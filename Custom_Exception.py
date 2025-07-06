class Error(Exception):
  pass

class AgeError(Error):
  pass

Age = int(input("Enter your age: "))

try:
  if Age>=18 or Age<=30:
    print("You are eligible to vote")
  else:
    raise AgeError
except AgeError:
  print("not eligible to vote")
