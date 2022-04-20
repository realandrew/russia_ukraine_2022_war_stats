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

for i in range(0, rows.__len__()):
    for j in range(1, 15):
        newRow = []
        newRow.append(header[j]) # Type
        newRow.append(rows[i][0]) # Date
        if (i == 0):
            newRow.append(int(rows[i][j]) - 0) # Losses
        else:
            newRow.append(int(rows[i][j]) - int(rows[i-1][j])) # Losses
        newRows.append(newRow)

filename = 'format2.csv'
with open(filename, 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(newHeader)
    csvwriter.writerows(newRows)