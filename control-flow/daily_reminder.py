# Prompt the user to input the task description
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ")

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")

# Match Case to handle different priority levels
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level. Please choose high, medium, or low."

# Check if the task is time-bound and adjust the reminder
if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the final reminder
print("Reminder:", reminder)
