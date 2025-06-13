def single_digit(n):
  while n >= 10:
    s = 0
    while n > 0:
      s += n % 10
      n //= 10
    n = s
  return n

# Example:
num = 38
result = single_digit(num)
print(f"The single digit of {num} is: {result}")