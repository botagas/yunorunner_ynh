#!/usr/bin/env python3

import re
from pathlib import Path

# Define the paths to the files
run_py_path = Path("/var/www/yunorunner/yunorunner/run.py")
package_check_sh_path = Path("/var/www/yunorunner/package_check/package_check.sh")

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

# Function to replace the shebang in run.py
def replace_shebang_in_run_py():
    if not run_py_path.exists():
        print(f"File not found: {run_py_path}")
        return

    with run_py_path.open("r") as file:
        content = file.readlines()

    # Replace the shebang with the virtual environment's Python interpreter
    if content[0].startswith("#!/"):
        content[0] = "#!/var/www/yunorunner/venv/bin/python\n"
    else:
        content.insert(0, "#!/var/www/yunorunner/venv/bin/python\n")

    with run_py_path.open("w") as file:
        file.writelines(content)

    print("Replaced shebang in run.py.")

# Function to add source to package_check.sh
def add_source_to_package_check_sh():
    if not package_check_sh_path.exists():
        print(f"File not found: {package_check_sh_path}")
        return

    with package_check_sh_path.open("r") as file:
        content = file.read()

    # Check if the source line is already present
    if "source /var/www/yunorunner/venv/bin/activate" in content:
        print("Virtual environment activation already present in package_check.sh.")
        return

    # Replace `source "./lib/common.sh"` with itself and add the source line after it
    new_content = re.sub(
        r'(source "./lib/common.sh")',
        r'\1\nsource /var/www/yunorunner/venv/bin/activate',
        content,
    )

    with package_check_sh_path.open("w") as file:
        file.write(new_content)

    print("Added virtual environment activation to package_check.sh.")

# Main entry point
if __name__ == "__main__":
    add_os_system_to_run_job()
    modify_cmd_line()
    replace_shebang_in_run_py()
    add_source_to_package_check_sh()