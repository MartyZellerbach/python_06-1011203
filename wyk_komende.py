import subprocess

# Execute the 'hostname' command
result = subprocess.run(['hostname'], capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Print the output of the command
    print("Hostname:", result.stdout.strip())
else:
    # Print an error message
    print("Error:", result.stderr)
