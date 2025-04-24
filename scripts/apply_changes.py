#!/usr/bin/env python3

import os
import re
import sys
from pathlib import Path
from types import SimpleNamespace

# Load configuration from config.py
config_path = "/var/www/yunorunner/yunorunner/config.py"
config_dict = {}
exec(open(config_path).read(), config_dict)

# Convert the config dictionary into an object with attributes
config = SimpleNamespace(**config_dict)

# Define paths
package_check_dir = Path("/var/www/yunorunner/package_check")
common_sh_path = package_check_dir / "lib/common.sh"
test_catalog_path = package_check_dir / "package_linter/tests/test_catalog.py"

# Function to replace content in a file
def replace_in_file(file_path, pattern, replacement):
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return

    with file_path.open("r") as file:
        content = file.read()

    # Replace the pattern with the replacement
    new_content = re.sub(pattern, replacement, content)

    with file_path.open("w") as file:
        file.write(new_content)

    print(f"Updated: {file_path}")

# Function to add safe directories to common.sh
def add_safe_directories():
    if not common_sh_path.exists():
        print(f"File not found: {common_sh_path}")
        return

    with common_sh_path.open("r") as file:
        content = file.read()

    # Check if one of the safe directory lines already exists
    if "git config --global --add safe.directory /var/www/yunorunner/package_check" in content:
        print("Safe directories are already configured.")
        return

    # Add safe directory lines after the git clone line
    new_content = re.sub(
        r'(git clone --quiet \$git_repository "\./package_linter")',
        r'\1\n    git config --global --add safe.directory /var/www/yunorunner/package_check\n'
        r'    git config --global --add safe.directory /var/www/yunorunner/package_check/package_linter/.apps\n'
        r'    git config --global --add safe.directory /var/www/yunorunner/package_check/package_linter\n'
        r'    /usr/bin/env python3 /var/www/yunorunner/yunorunner/apply_changes.py test_catalog',
        content,
    )

    with common_sh_path.open("w") as file:
        file.write(new_content)

    print(f"Safe directories added to: {common_sh_path}")

# Function to apply changes to test_catalog.py
def apply_test_catalog_changes():
    if not test_catalog_path.exists():
        print(f"File not found: {test_catalog_path}")
        return

    print(f"Checking for necessary changes in {test_catalog_path}...")

    # Replace URLs with dynamic values from config
    replace_in_file(
        test_catalog_path,
        r"https://github.com/YunoHost-Apps",
        f"https://github.com/{config.EXECUTOR}",
    )
    replace_in_file(
        test_catalog_path,
        r"https://github.com/labriqueinternet",
        f"https://github.com/{config.EXECUTOR}",
    )
    replace_in_file(
        test_catalog_path,
        r'"https://github.com/YunoHost/apps"',
        f'"{config.APPSREPO}"',
    )

# Main entry point
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "safe_directories":
            add_safe_directories()
        elif sys.argv[1] == "test_catalog":
            apply_test_catalog_changes()
        else:
            print(f"Unknown function: {sys.argv[1]}")
    else:
        print("No function specified. Usage: apply_changes.py [safe_directories|test_catalog]")