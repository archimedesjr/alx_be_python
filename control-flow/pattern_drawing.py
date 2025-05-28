size = int(input("Enter the size of the pattern: "))
j = 0
while j < size:
  for i in range(1, size + 1):
    print("*", end="")
  print()
  j += 1
