from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Calculate a future date by adding a specified number of days to the current date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
