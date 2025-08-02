import pandas as pd

# Read the CSV log
df = pd.read_csv("life_log.csv")

# Rename columns with cute emoji headers
df = df.rename(columns={
    "Study": "📚 Study",
    "Sleep": "😴 Sleep",
    "Phone": "📱 Phone",
    "Chill": "🛋️ Chill",
    "Exercise": "🏃‍♀️ Exercise",
    "Projects": "💻 Projects",
    "Total": "⏱️ Total"
})

# Define color styling for specific columns
def highlight_cells(val, col):
    if col == "📚 Study" and val >= 5:
        return "background-color: #E6F4EA"  # mint green
    elif col == "📱 Phone" and val > 3:
        return "background-color: #FFEBEE; color: #C62828;"  # soft red
    elif col == "💻 Projects" and val >= 2:
        return "background-color: #E3F2FD"  # baby blue
    else:
        return ""

def style_row(row):
    return [highlight_cells(row[col], col) if isinstance(row[col], float) else "" for col in row.index]

# Apply all styles
styled = df.style \
    .set_table_styles([{
        'selector': 'th',
        'props': [('background-color', '#F8BBD0'), ('color', '#333'), ('font-weight', 'bold'), ('text-align', 'center')]
    }]) \
    .apply(style_row, axis=1)

# Save it as fancy Excel file
styled.to_excel("✨Suhani_Life_Tracker.xlsx", index=False, engine='openpyxl')

print("💅 Tracker styled and saved as '✨Suhani_Life_Tracker.xlsx'")

