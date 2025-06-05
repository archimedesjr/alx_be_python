from datetime import datetime, timedelta
current_date = datetime.now()

def display_current_datetime():
  print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date(number_of_days):
  future_date = current_date + timedelta(days=number_of_days)
  print(future_date.strftime("%Y-%m-%d"))