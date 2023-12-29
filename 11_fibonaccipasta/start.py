#!/usr/bin/python3


def generate_fibonacci_phone_number():
    phone_number = []
    a, b = 21, 34

    while len(phone_number) < 4:
        phone_number.append(a)
        a, b = b, a + b

    return " ".join(map(str, phone_number))


fibonacci_phone_number = generate_fibonacci_phone_number()
print(f"The generated Fibonacci phone number is: {fibonacci_phone_number}")
