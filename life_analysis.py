import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style

# Load CSV
df = pd.read_csv("life_log.csv")

# Normalize column names (strip spaces + lowercase)
df.columns = df.columns.str.strip().str.lower()

print("✅ Cleaned Columns:", df.columns.tolist())

# Make sure required columns exist
required_columns = ['timestamp', 'activity', 'duration (mins)']
if not all(col in df.columns for col in required_columns):
    print(Fore.RED + "❌ CSV does not have the required columns: timestamp, activity, duration (mins)" + Style.RESET_ALL)
    exit()

# Convert duration to numeric
df['duration (mins)'] = pd.to_numeric(df['duration (mins)'], errors='coerce')
df.dropna(subset=['duration (mins)'], inplace=True)

# Group total time by activity
if df['activity'].isnull().all():
    print(Fore.YELLOW + "⚠️ No valid 'activity' entries found in CSV. Cannot analyze." + Style.RESET_ALL)
    exit()

summary = df.groupby("activity")['duration (mins)'].sum()

if summary.empty:
    print(Fore.YELLOW + "⚠️ No valid duration data to analyze. Fill in life_log.csv with entries." + Style.RESET_ALL)
    exit()

# Alert if scroll time exceeds 2 hours
if 'scroll' in summary and summary['scroll'] > 120:
    print(Fore.RED + "⚠️ You’ve scrolled more than 2 hours today!" + Style.RESET_ALL)
else:
    print(Fore.GREEN + "✅ Screen time is under control!" + Style.RESET_ALL)

# Show top activity
top = summary.idxmax()
print(Fore.CYAN + f"🏆 Most time spent on: {top} – {summary[top]} mins" + Style.RESET_ALL)

# Plot bar chart
plt.figure(figsize=(8, 5))
summary.plot(kind='bar', color='orchid')
plt.title("Total Time Spent per Activity")
plt.ylabel("Minutes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("life_bar_chart.png")
plt.close()

# Plot pie chart
plt.figure(figsize=(6, 6))
summary.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Activity Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("life_pie_chart.png")
plt.close()

print(Fore.GREEN + "🎉 Charts saved: life_bar_chart.png and life_pie_chart.png" + Style.RESET_ALL)

