import json
import csv
import os


folder_path = "/Users/soumya/Desktop/Data stuff/Spotify/SpotifyDataAnalysis"
merged_data = []

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        with open(os.path.join(folder_path, filename), 'r') as f:
            try:
                data = json.load(f)
                merged_data += data
            except json.JSONDecodeError:
                print(f"Could not parse {filename}")

# Write to CSV
print(merged_data[0])
if merged_data:
    fieldnames = merged_data[0].keys()
    with open('merged_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(merged_data)

print("Done! CSV saved as merged_data.csv")