import os
import subprocess
import json

def load_config(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def run_command(command):
    try:
        print(f"Running command: {' '.join(command)}")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def main(option):
    # configName.json
    config = load_config(option)

    devices = "0" # typically 0 through n
    os.environ["CUDA_VISIBLE_DEVICES"] = devices
    print("CUDA_VISIBLE_DEVICES:", os.environ.get("CUDA_VISIBLE_DEVICES"))

    command = ["python", "train.py"]
    for key, value in config.items():
        command.append(f"--{key}")
        command.append(str(value[0]))

    run_command(command)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python run.py <option>")
    else:
        main(sys.argv[1])