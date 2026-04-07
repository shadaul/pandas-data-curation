import subprocess
import time


while True:
    print("calling to api")
    subprocess.run(["python", "api_test.py"])

    print("cleaning and adding to db")
    subprocess.run(["python", "scripts.py"])

    print("waiting 10 hours before running it again")
    time.sleep(36000)

# subprocess.run(["python","check_db.py"])
# print("checking database")