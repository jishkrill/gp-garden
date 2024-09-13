import os
import re

# Define a regular expression to match lines starting with "up::"
up_pattern = re.compile(r'^up:.*$', re.MULTILINE)

# Get the current working directory
root_dir = os.getcwd()

# Walk through the directory
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(subdir, file)
            
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove lines starting with "up::"
            new_content = re.sub(up_pattern, '', content)
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Lines starting with 'up::' have been removed!")
