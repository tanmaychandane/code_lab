# Automation: Creating Multiple Empty Text Files

import os

# config
file_base_name = "report_"
num_files_to_create = 10
file_extension = ".txt"
output_directory = "."

# automation logic
print(f"Starting to create {num_files_to_create} files...")

for i in range(1, num_files_to_create + 1):
    file_name = f"{file_base_name}{i}{file_extension}"
    file_path = os.path.join(output_directory, file_name)

    try:
        with open(file_path, 'w') as f:
            pass
        print(f"Created: {file_name}")
    except IOError as e:
        print(f"Error creating {file_name}: {e}")

print("File creation process completed.")


# created using gemini. URL: https://g.co/gemini/share/5128549c2d59
