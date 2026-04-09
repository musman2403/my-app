# This is our build automation script
# It runs main.py automatically and checks if it succeeded or failed

import subprocess  # Used to run other programs/scripts from Python
import sys         # Used to get the current Python interpreter path

print("Running tests...")

# Run main.py using the same Python that is running this script
# capture_output=True means we capture what main.py prints
# text=True means the output is returned as a string (not bytes)
result = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)

# returncode 0 means the program ran without errors
if result.returncode == 0:
    print("Build successful!")
    print("Output:", result.stdout)  # Print what main.py printed
else:
    print("Build failed!")
    print("Error:", result.stderr)   # Print the error message if it failed