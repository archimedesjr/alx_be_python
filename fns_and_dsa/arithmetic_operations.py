def perform_operation(num1, num2, operation):
  if operation == "+":
    result = float(num1) + float(num2)
    return result
  elif operation == "-":
    result = float(num1) - float(num2)
    return result
  elif operation == "/":
    if float(num2) == 0:
      result = "Undefined"
      return result
    else:
      result = float(num1) / float(num2)
      return result
  else:
    result = float(num1) * float(num2)
    return result

answer = perform_operation(5,0,"/")
print(answer)