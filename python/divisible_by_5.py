def check_divisibility(num):
  # // Expected output is "TRUE" or "FALSE"

  if num % 5 == 0:
    return "TRUE"
  else:
    return "FALSE"

num = int(input("Enter a number: "))
print(check_divisibility(num))
