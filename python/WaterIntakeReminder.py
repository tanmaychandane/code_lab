import time
import random

messages = [
    "Time to drink water!",
    "Stay hydrated, you’ve got this!",
    "Hydration check",
    "Take a sip, refresh yourself",
    "Your body will thank you for this!"
]

hours = int(input("Enter how many hours you'll be working:  "))

interval = int(input("Enter reminder interval in minutes:   "))

total_minutes = hours * 60

reminders = total_minutes // interval

print(f"\nStarting your hydration reminder for {hours} hour(s).\n")

for i in range(reminders):
    time.sleep(interval * 60)
    message = random.choice(messages)
    print(f"\nReminder {i+1}: {message}")
