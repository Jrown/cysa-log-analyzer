# log_analyzer.py

with open("auth.log", "r") as log:
    for line in log:
        if "Failed password" in line:
            print("Suspicious login attempt:", line.strip())
