import matplotlib.pyplot as plt

# August 2023 temperature data values from Athens in Celsius
celsius_temperatures = [+34, +35, +33, +31, +30, +31, +32, +32, +32, +32, +32, +34, +36, +36, +35, +37, +34, +33, +34, +36, +35, +36, +38, +37, +35, +33, +29, +30, +32, +31]

# Task 1: Convert temperatures from Celsius to Fahrenheit
fahrenheit_temperatures = [(c * 9/5) + 32 for c in celsius_temperatures]

# Task 2: Sort and display temperatures in descending order as (°C, °F) pairs
sorted_temp_pairs = sorted(zip(celsius_temperatures, fahrenheit_temperatures), key=lambda pair: pair[1], reverse=True)
print("Temperatures in Descending Order:")
for c, f in sorted_temp_pairs:
    print(f"{c}°C = {f}°F")

# Task 3: Compute the average temperature in both scales
avg_celsius = sum(celsius_temperatures) / len(celsius_temperatures)
avg_fahrenheit = (avg_celsius * 9/5) + 32
print(f"Average Temperature: {avg_celsius:.2f}°C, {avg_fahrenheit:.2f}°F")

# August dates for the heatmap
dates = ["01-08-2023", "02-08-2023", "03-08-2023", "04-08-2023", "05-08-2023",
         "06-08-2023", "07-08-2023", "08-08-2023", "09-08-2023", "10-08-2023",
         "11-08-2023", "12-08-2023", "13-08-2023", "14-08-2023", "15-08-2023",
         "16-08-2023", "17-08-2023", "18-08-2023", "19-08-2023", "20-08-2023",
         "21-08-2023", "22-08-2023", "23-08-2023", "24-08-2023", "25-08-2023",
         "26-08-2023", "27-08-2023", "28-08-2023", "29-08-2023", "30-08-2023", "31-08-2023"]

# Creating a heatmap using Matplotlib
fig, ax = plt.subplots(figsize=(18, 8))
heatmap_data = [celsius_temperatures, fahrenheit_temperatures]
im = ax.imshow(heatmap_data, cmap="coolwarm", aspect="auto")  # Changed color map for a different look

# Customize labels and titles
ax.set_xticks(range(len(dates)))
ax.set_yticks([0, 1])
ax.set_xticklabels(dates, rotation=45, fontsize=12)  # Changed rotation and font size for better readability
ax.set_yticklabels(["Celsius", "Fahrenheit"])
ax.set_xlabel("Date in August 2023")
ax.set_ylabel("Temperature Scale")

# Adding temperature values on the heatmap
for i in range(2):
    for j in range(len(dates)):
        text = ax.text(j, i, f"{heatmap_data[i][j]:.1f}", ha="center", va="center", color="white")  # Changed text color

plt.title("Athens Temperature Heatmap for August 2023")
plt.tight_layout()
plt.show()