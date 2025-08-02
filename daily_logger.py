import csv
from datetime import datetime

# Ask for today's date (or auto-fill)
date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
if not date:
    date = datetime.now().strftime("%Y-%m-%d")

# Define categories to track
categories = ['Study', 'Sleep', 'Phone', 'Chill', 'Exercise', 'Projects']
data = {}

# Get time spent on each
for cat in categories:
    while True:
        try:
            hours = float(input(f"Hours spent on {cat}: "))
            data[cat] = hours
            break
        except ValueError:
            print("Please enter a valid number.")

# Calculate total
total = round(sum(data.values()), 2)

# Write to CSV
filename = "life_log.csv"
header = ["Date"] + categories + ["Total"]

# Create file if not exists
try:
    with open(filename, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
except FileExistsError:
    pass

# Append today’s entry
with open(filename, "a", newline="") as f:
    writer = csv.writer(f)
    row = [date] + [data[cat] for cat in categories] + [total]
    writer.writerow(row)

print(f"\n📅 Day logged for {date}. Total hours: {total}")
