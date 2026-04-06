import subprocess

print("calling to api")
subprocess.run(["python", "api_test.py"])

print("cleaning and adding to db")
subprocess.run(["python", "scripts.py"])


# subprocess.run(["python","check_db.py"])
# print("checking database")