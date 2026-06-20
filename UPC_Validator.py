"""
UPC_Valiator.py
By Jack Verdin
This program was made for a CSCC Python course, and is meant to validate a UPC-A code.
"""

#Need find_UPC() function
def find_UPC(upc_string):
    sum_a = 0
    sum_b = 0
    string_spot = 1
    for digit in upc_string:
        if string_spot % 2 == 0:
            sum_b += int(digit)
        else:
            sum_a += int(digit) * 3
        string_spot += 1
    calc_check = (sum_a + sum_b) % 10
    if calc_check == 0:
        return 0
    else:
        return 10 - calc_check


#Need input logic
upc_code = ""
while len(upc_code) != 12:
    upc_code = input("Enter a UPC code: ")
    if len(upc_code) != 12:
        print("That is not the valid length for a UPC code.")
        upc_code = ""
    elif not(upc_code.isdigit()):
        print("UPC codes cannot contain any letters.")
        upc_code = ""
print(f"\nThe first 11 digits of the UPC code are: {upc_code[:-1]}")
print(f"The given check digit is: {upc_code[-1]}")

#Need output logic