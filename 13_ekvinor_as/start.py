#!/usr/bin/python3

# Hexadecimal to Decimal
# A=10, B=11, C=12, 04D2=1243

hex_codes = ["A", "B", "C", "04D2"]

pin = sum([int(hex_code, 16) for hex_code in hex_codes])

print(pin)
