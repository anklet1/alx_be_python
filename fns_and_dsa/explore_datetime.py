# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date inside current_date
    current_date = datetime.now()
    # Format and print the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days):
    # Save the future date inside future_date
    future_date = current_date + timedelta(days=days)
    # Print the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

if __name__ == "__main__":
    # Part 1: Display current datetime
    current_date = display_current_datetime()

    # Part 2: Prompt user for number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date, days_to_add)
