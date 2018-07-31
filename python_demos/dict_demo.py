ages = {"Alice": 22, "Bob": 27}
print(f"ages without update{ages}")
ages["Charlie"] = 30 # insert new item into dict

ages["Alice"] += 1 # update Alice age

print(f"ages after adding new item and upate of value {ages}")
