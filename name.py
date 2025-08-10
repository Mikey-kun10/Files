with open("name.txt", "r") as file:
    full_name = file.read().strip()

name_parts = full_name.split()

first_name = name_parts[0] if len(name_parts) > 0 else ""
middle_name = name_parts[1] if len(name_parts) > 2 else ""
last_name = name_parts[-1] if len(name_parts) > 1 else ""

print("First Name:", first_name)
print("Middle Name:", middle_name if middle_name else "None")
print("Last Name:", last_name)
