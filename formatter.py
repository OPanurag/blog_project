import re

def refactor_requirements(file_path):
    """
    Refactor the requirements.txt file to remove any local file paths
    and leave only the package names.

    :param file_path: Path to the requirements.txt file
    """
    # Read the current contents of the requirements file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Open the file in write mode to update it
    with open(file_path, 'w') as file:
        for line in lines:
            # Check if the line contains a package with a local file path
            match = re.match(r'(\S+)\s+@ file://.*', line)
            if match:
                package_name = match.group(1)
                file.write(f'{package_name}\n')
            else:
                file.write(line)

# Usage
requirements_file_path = 'requirements.txt'
refactor_requirements(requirements_file_path)
