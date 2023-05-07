import os
import subprocess

print("JUST THE NAME not the exe extenstion")
exe_name = input()

def erun(exe_name):
    os.system(f"nim c -d:release {exe_name}.nim")
    exe_path = os.path.join(os.getcwd(), f"{exe_name}.exe")
    try:
        output = subprocess.check_output(exe_path, shell=True, stderr=subprocess.STDOUT)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Error executing the EXE file: {e.output.decode('utf-8')}"

# Execute the EXE file and get the output
output = erun(exe_name)

# Print the output
print(output)
