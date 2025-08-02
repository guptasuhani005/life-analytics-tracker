import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("life_log.csv")

# Latest entry = last row
latest = df.iloc[-1]
date = latest["Date"]

# Donut Chart – time breakdown for that day
labels = ['📚 Study', '😴 Sleep', '📱 Phone', '🛋️ Chill', '🏃‍♀️ Exercise', '💻 Projects']
values = latest[1:-1]  # skip Date and Total

colors = ['#F8BBD0', '#C5CAE9', '#FFE0B2', '#DCEDC8', '#B2EBF2', '#E1BEE7']

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%',
                                   startangle=90, pctdistance=0.85)
# Donut center
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)
plt.title(f'💖 Suhani’s Day Breakdown ({date})', fontsize=14)
plt.tight_layout()
plt.savefig("🍩suhani_day_donut.png")
plt.show()
