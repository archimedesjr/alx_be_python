def safe_divide(numerator, denominator):
  try:
    result = float(numerator) / float(denominator)
    return f"The result of the division is {result}"
  except ZeroDivisionError:
    return "Error: Cannot divide by zero"
  
  