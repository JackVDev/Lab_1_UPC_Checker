"""
UPC_Valiator.py
By Jack Verdin
This program was made for a CSCC Python course, and is meant to validate a UPC-A code.
"""

#Need find_UPC() function

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
print("Loop over")
#Need output logic