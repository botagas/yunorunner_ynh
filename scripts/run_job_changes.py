#!/usr/bin/env python3

import re
from pathlib import Path

# Define the path to run.py
run_py_path = Path("/var/www/yunorunner/yunorunner/run.py")

# Function to add os.system logic to run_job
def add_os_system_to_run_job():
    if not run_py_path.exists():
        print(f"File not found: {run_py_path}")
        return

    with run_py_path.open("r") as file:
        content = file.read()

    # Check if the os.system line is already present
    if 'os.system("/usr/bin/env python3 /var/www/yunorunner/yunorunner/apply_changes.py test_catalog")' in content:
        print("os.system logic already exists in run_job.")
        return

    # Add the os.system line at the start of the run_job function
    new_content = re.sub(
        r"(async def run_job\(worker, job\):)",
        r'\1\n'
        r'    result = os.system("/usr/bin/env python3 /var/www/yunorunner/yunorunner/apply_changes.py test_catalog")\n'
        r'    if result != 0:\n'
        r'        task_logger.error("Failed to apply changes to test_catalog.py")\n'
        r'        return\n'
        r'    task_logger.info("Successfully applied changes to test_catalog.py")',
        content,
    )

    with run_py_path.open("w") as file:
        file.write(new_content)

    print("Added os.system logic to run_job.")

# Function to modify the cmd line
def modify_cmd_line():
    if not run_py_path.exists():
        print(f"File not found: {run_py_path}")
        return

    with run_py_path.open("r") as file:
        content = file.read()

    # Check if the cmd line is already modified
    if "/usr/bin/env python3 /var/www/yunorunner/yunorunner/apply_changes.py safe_directories" in content:
        print("cmd line already includes safe_directories logic.")
        return

    # Modify the cmd line to include safe_directories
    new_content = re.sub(
        r'cmd = f"nice --adjustment=10 script -qefc \'/bin/bash \{app\.config\.PACKAGE_CHECK_PATH\} \{job\.url_or_path\} 2>&1\'"',
        r'cmd = f"nice --adjustment=10 script -qefc \'/usr/bin/env python3 /var/www/yunorunner/yunorunner/apply_changes.py safe_directories && /bin/bash {app.config.PACKAGE_CHECK_PATH} {job.url_or_path} 2>&1\'"',
        content,
    )

    with run_py_path.open("w") as file:
        file.write(new_content)

    print("Modified cmd line to include safe_directories logic.")

# Main entry point
if __name__ == "__main__":
    add_os_system_to_run_job()
    modify_cmd_line()