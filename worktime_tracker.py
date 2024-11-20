import sys
from datetime import datetime
import os

# Pfad zur Datei, in der die Start- und Endzeit für jeden Tag gespeichert wird
log_path = os.path.expanduser("~\\Desktop\\time_tracker_log.txt")

def save_time(action):
    """Speichert die aktuelle Zeit mit einer Aktion (Start/Ende) in die Log-Datei."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as file:
        file.write(f"{action} Zeit: {current_time}\n")
    print(f"{action} Zeit gespeichert: {current_time}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1]  # Erwartet "start" oder "ende" als Argument
        save_time(action)
    else:
        print("Bitte geben Sie ein Argument an: 'start' oder 'ende'.")
