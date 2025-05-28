task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time bound? (yes or no): ").lower()
match priority:
  case _ if priority == "high" and time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
  case _ if priority == "low" and time_bound == "no":
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
  case _:
    print("I do not care")