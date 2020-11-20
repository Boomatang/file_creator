from datetime import time
from os.path import join, dirname
from time import sleep
import os

try:
    from dotenv import load_dotenv
    # Create .env file path.
    dotenv_path = join(dirname(__file__), '.env')
    # Load file from the path.
    load_dotenv(dotenv_path)
except ModuleNotFoundError:
    print("No dotenv file found")

# Accessing variables.
COUNT = int(os.getenv('COUNT'))
SIZE = float(os.getenv('SIZE'))
TRIES = int(os.getenv('TRIES'))
SLEEP = float(os.getenv('SLEEP'))
LOG = bool(os.getenv('LOG'))
ALIVE = bool(os.getenv('ALIVE'))

# Using variables.
number = 0
print("Creating dummy files")
while number < COUNT:
    with open(f"out/{number}_dummy_{number}", "wb") as out:
        if LOG:
            print(f"create file out/{number}_dummy{number}")
        out.seek(int((1024 * 1024 * SIZE)) - 1)
        out.write(b'\0')
    number += 1

while TRIES > 0:
    if LOG:
        print(f"Starting to update all files: {TRIES}")
    number = 0
    while number < COUNT:
        with open(f"out/{number}_dummy_{number}", "a") as out:
            out.write("Dummy line\n")
        number += 1

    TRIES -= 1
    sleep(SLEEP)

if ALIVE:
    print("going to sleep forever")
    while True:
        sleep(SLEEP)
