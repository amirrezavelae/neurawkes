import re

# Define the file path
file_path = "modules/organizers.py"

# Read the contents of the file
with open(file_path, 'r') as file:
    file_contents = file.read()

# Define the regex pattern and replacement
pattern = r'print\s+"([^"]+)"'
replacement = r'print("\1")'

# Perform the replacement
new_contents = re.sub(pattern, replacement, file_contents)

# Write the updated contents back to the file
with open(file_path, 'w') as file:
    file.write(new_contents)

print(f"Updated {file_path} successfully.")
