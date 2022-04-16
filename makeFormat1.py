import csv

file = open('default.csv', 'r')

csvreader = csv.reader(file)

header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

file.close()

newHeader = ['Type', 'Date', 'Losses']
newRows = []

for row in rows:
    for j in range(1, 15):
      newRow = []
      newRow.append(header[j]) # Type
      newRow.append(row[0]) # Date
      newRow.append(row[j]) # Losses
      newRows.append(newRow)

filename = 'format1.csv'
with open(filename, 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(newHeader)
    csvwriter.writerows(newRows)