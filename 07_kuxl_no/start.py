#!/usr/bin/python3

with open("bids-26-11-2023.dat", "r") as file:
    rows = file.read().strip().split("\n")

rowemojis, columns = rows[0].split(), [[] for _ in range(len(rows[0].split()))]

for row in rows[1:]:
    for i, value in enumerate(row.split()):
        columns[i].append(int(value))

highest_numbers = [max(column) for column in columns]

for emoji, highest_number in zip(rowemojis, highest_numbers):
    print(f"Highest number in column {emoji}: {highest_number}")
